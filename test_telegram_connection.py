#!/usr/bin/env python3
"""
Test Telegram bot connection and send test message
"""

import os
from dotenv import load_dotenv
import requests

def test_telegram_connection():
    print("🧪 Testing Telegram Bot Connection...")
    
    # Load environment variables
    load_dotenv()
    
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    print(f"Bot Token: {bot_token[:10]}...{bot_token[-10:] if bot_token else 'NOT FOUND'}")
    print(f"Chat ID: {chat_id}")
    
    if not bot_token or not chat_id:
        print("❌ Missing bot token or chat ID in .env file")
        return False
    
    # Test bot info
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            bot_info = response.json()
            print(f"✅ Bot connected: {bot_info['result']['first_name']}")
        else:
            print(f"❌ Bot connection failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Bot connection error: {e}")
        return False
    
    # Send test message
    try:
        test_message = "🧪 **Telegram Bot Test**\n\n✅ Connection working!\n📅 Ready to receive daily job notifications"
        
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': test_message,
            'parse_mode': 'Markdown'
        }
        
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            print("✅ Test message sent successfully!")
            return True
        else:
            print(f"❌ Failed to send message: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Message sending error: {e}")
        return False

if __name__ == "__main__":
    success = test_telegram_connection()
    if success:
        print("\n🎉 Telegram bot is working correctly!")
        print("💡 If you're not getting daily notifications, check your cron job setup")
    else:
        print("\n❌ Telegram bot has issues - this is why you're not getting notifications")