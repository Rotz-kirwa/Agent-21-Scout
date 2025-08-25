#!/usr/bin/env python3
"""
Agent-21 Scout Payment Bot
Handles M-Pesa payments and Telegram group invites
"""

import os
import json
import time
import random
import string
from datetime import datetime, timedelta
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask, request, jsonify
import sqlite3
import threading
from dotenv import load_dotenv

load_dotenv()

# Configuration
BOT_TOKEN = os.getenv("PAYMENT_BOT_TOKEN")  # Your payment bot token
GROUP_INVITE_LINK = os.getenv("GROUP_INVITE_LINK", "https://t.me/+YourGroupInviteLink")
MPESA_PHONE = os.getenv("MPESA_PHONE", "0791260817")
PAYMENT_AMOUNT = int(os.getenv("PAYMENT_AMOUNT", "50"))
WEBHOOK_PORT = int(os.getenv("WEBHOOK_PORT", "5000"))

# Database setup
def init_db():
    conn = sqlite3.connect('agent21_payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            reference_code TEXT UNIQUE NOT NULL,
            payment_status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            paid_at TIMESTAMP,
            invite_sent BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    conn.close()

def generate_reference_code():
    """Generate unique 6-digit reference code"""
    return ''.join(random.choices(string.digits, k=6))

def save_payment_request(user_id, username, reference_code):
    """Save payment request to database"""
    conn = sqlite3.connect('agent21_payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payments (user_id, username, reference_code)
        VALUES (?, ?, ?)
    ''', (user_id, username, reference_code))
    conn.commit()
    conn.close()

def get_pending_payment(reference_code):
    """Get pending payment by reference code"""
    conn = sqlite3.connect('agent21_payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT user_id, username FROM payments 
        WHERE reference_code = ? AND payment_status = 'pending'
    ''', (reference_code,))
    result = cursor.fetchone()
    conn.close()
    return result

def mark_payment_completed(reference_code):
    """Mark payment as completed"""
    conn = sqlite3.connect('agent21_payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE payments 
        SET payment_status = 'completed', paid_at = CURRENT_TIMESTAMP, invite_sent = TRUE
        WHERE reference_code = ?
    ''', (reference_code,))
    conn.commit()
    conn.close()

# Telegram Bot Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command"""
    welcome_msg = """
🤖 *Welcome to Agent-21 Scout Premium!*

Get exclusive access to:
• 📊 Daily job alerts from 15+ sources
• 🌍 Worldwide remote opportunities
• 💼 IT Support, VA, Content Writing jobs
• 🎯 Kenya-friendly positions
• ⚡ Real-time job notifications

Use /join to subscribe for just Ksh 50/month!
    """
    await update.message.reply_text(welcome_msg, parse_mode='Markdown')

async def join_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /join command"""
    user_id = update.effective_user.id
    username = update.effective_user.username or "Unknown"
    
    # Generate unique reference code
    reference_code = generate_reference_code()
    
    # Save to database
    try:
        save_payment_request(user_id, username, reference_code)
        
        join_msg = f"""
💳 *Agent-21 Scout Premium Subscription*

To join our exclusive job alerts group:

1️⃣ Send *Ksh {PAYMENT_AMOUNT}* to: `{MPESA_PHONE}`
2️⃣ Use reference code: `{reference_code}`
3️⃣ You'll receive your invite link automatically!

⏰ Payment expires in 30 minutes
🔒 Secure M-Pesa verification system

*What you get:*
• Daily job alerts at 6 AM
• 15+ job sources worldwide
• Kenya-friendly remote positions
• IT, VA, Content Writing opportunities
        """
        
        await update.message.reply_text(join_msg, parse_mode='Markdown')
        
    except Exception as e:
        await update.message.reply_text(
            "❌ Error processing your request. Please try again.",
            parse_mode='Markdown'
        )

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Check payment status"""
    user_id = update.effective_user.id
    
    conn = sqlite3.connect('agent21_payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT reference_code, payment_status, created_at 
        FROM payments 
        WHERE user_id = ? 
        ORDER BY created_at DESC 
        LIMIT 1
    ''', (user_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        ref_code, status, created_at = result
        status_msg = f"""
📊 *Payment Status*

Reference Code: `{ref_code}`
Status: {status.title()}
Created: {created_at}

{f"✅ Payment confirmed! Check your messages for the invite link." if status == 'completed' else "⏳ Waiting for M-Pesa confirmation..."}
        """
    else:
        status_msg = "❌ No payment requests found. Use /join to subscribe."
    
    await update.message.reply_text(status_msg, parse_mode='Markdown')

# Flask Webhook for SMS
app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

@app.route('/webhook/sms', methods=['POST'])
def handle_sms():
    """Handle SMS webhook from SMS forwarder"""
    try:
        data = request.get_json()
        
        # Expected SMS format: "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456"
        sms_text = data.get('message', '').lower()
        sender = data.get('sender', '')
        
        # Check if it's an M-Pesa confirmation SMS
        if 'confirmed' in sms_text and f'ksh{PAYMENT_AMOUNT}' in sms_text.replace(' ', ''):
            
            # Extract reference code (6 digits)
            import re
            ref_match = re.search(r'reference[:\s]*(\d{6})', sms_text)
            
            if ref_match:
                reference_code = ref_match.group(1)
                
                # Check if payment exists
                payment_info = get_pending_payment(reference_code)
                
                if payment_info:
                    user_id, username = payment_info
                    
                    # Mark as completed
                    mark_payment_completed(reference_code)
                    
                    # Send invite link
                    invite_msg = f"""
🎉 *Payment Confirmed!*

Welcome to Agent-21 Scout Premium, {username}!

🔗 *Join our exclusive group:*
{GROUP_INVITE_LINK}

✅ You'll now receive daily job alerts
📅 Next alert: Tomorrow at 6:00 AM
🌟 Thank you for subscribing!
                    """
                    
                    # Send message to user
                    import asyncio
                    asyncio.create_task(
                        bot.send_message(
                            chat_id=user_id,
                            text=invite_msg,
                            parse_mode='Markdown'
                        )
                    )
                    
                    return jsonify({"status": "success", "message": "Payment processed"})
        
        return jsonify({"status": "ignored", "message": "SMS not relevant"})
        
    except Exception as e:
        print(f"Webhook error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/webhook/test', methods=['POST'])
def test_webhook():
    """Test webhook endpoint"""
    return jsonify({
        "status": "success", 
        "message": "Webhook is working!",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "Agent-21 Payment Bot"})

def run_telegram_bot():
    """Run Telegram bot"""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("join", join_command))
    application.add_handler(CommandHandler("status", status_command))
    
    # Start bot
    application.run_polling()

def run_flask_app():
    """Run Flask webhook server"""
    app.run(host='0.0.0.0', port=WEBHOOK_PORT, debug=False)

if __name__ == "__main__":
    # Initialize database
    init_db()
    
    # Run both Flask and Telegram bot
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()
    
    print(f"🚀 Agent-21 Payment Bot starting...")
    print(f"📱 Webhook running on port {WEBHOOK_PORT}")
    print(f"💳 M-Pesa: {MPESA_PHONE}")
    print(f"💰 Amount: Ksh {PAYMENT_AMOUNT}")
    
    # Run Telegram bot
    run_telegram_bot()