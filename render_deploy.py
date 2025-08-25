#!/usr/bin/env python3
"""
Render.com deployment version of Agent-21 Payment Bot
Simplified for easy deployment
"""

import os
import json
import sqlite3
import asyncio
from datetime import datetime
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

# Configuration
BOT_TOKEN = os.getenv("PAYMENT_BOT_TOKEN")
GROUP_INVITE_LINK = os.getenv("GROUP_INVITE_LINK", "https://t.me/+YourGroupLink")
MPESA_PHONE = os.getenv("MPESA_PHONE", "0791260817")
PAYMENT_AMOUNT = int(os.getenv("PAYMENT_AMOUNT", "50"))

app = Flask(__name__)

# Database functions (same as before)
def init_db():
    conn = sqlite3.connect('payments.db')
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

def get_pending_payment(reference_code):
    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT user_id, username FROM payments 
        WHERE reference_code = ? AND payment_status = 'pending'
    ''', (reference_code,))
    result = cursor.fetchone()
    conn.close()
    return result

def mark_payment_completed(reference_code):
    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE payments 
        SET payment_status = 'completed', paid_at = CURRENT_TIMESTAMP, invite_sent = TRUE
        WHERE reference_code = ?
    ''', (reference_code,))
    conn.commit()
    conn.close()

def send_telegram_message(chat_id, text):
    """Send message via Telegram API"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=data, timeout=10)
        return response.json()
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

# Flask routes
@app.route('/')
def home():
    return jsonify({
        "service": "Agent-21 Scout Payment Bot",
        "status": "running",
        "endpoints": ["/webhook/sms", "/webhook/test", "/health"]
    })

@app.route('/webhook/sms', methods=['POST'])
def handle_sms():
    """Handle SMS from forwarder app"""
    try:
        data = request.get_json()
        sms_text = data.get('message', '').lower()
        
        # Check for M-Pesa confirmation
        if 'confirmed' in sms_text and f'ksh{PAYMENT_AMOUNT}' in sms_text.replace(' ', ''):
            
            import re
            ref_match = re.search(r'reference[:\s]*(\d{6})', sms_text)
            
            if ref_match:
                reference_code = ref_match.group(1)
                payment_info = get_pending_payment(reference_code)
                
                if payment_info:
                    user_id, username = payment_info
                    mark_payment_completed(reference_code)
                    
                    # Send invite
                    invite_msg = f"""
🎉 *Payment Confirmed!*

Welcome to Agent-21 Scout Premium, {username}!

🔗 *Join our exclusive group:*
{GROUP_INVITE_LINK}

✅ Daily job alerts start tomorrow at 6 AM
🌟 Thank you for subscribing!
                    """
                    
                    send_telegram_message(user_id, invite_msg)
                    
                    return jsonify({"status": "success", "message": "Payment processed"})
        
        return jsonify({"status": "ignored"})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/webhook/test', methods=['POST'])
def test_webhook():
    return jsonify({
        "status": "success",
        "message": "Webhook working!",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)