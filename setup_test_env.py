#!/usr/bin/env python3
"""
Setup test environment for Agent-21 Scout
"""

import os

def create_test_env():
    """Create test environment file"""
    
    print("🔧 Setting up test environment...")
    
    # Get user input
    print("\n📝 Please provide the following:")
    bot_token = input("Bot Token (from @BotFather): ").strip()
    group_link = input("Group Invite Link (optional, press Enter to skip): ").strip()
    your_phone = input("Your phone number (format: 0791234567): ").strip()
    
    # Create test environment
    env_content = f"""# Agent-21 Scout Test Environment
PAYMENT_BOT_TOKEN={bot_token}
GROUP_INVITE_LINK={group_link or 'https://t.me/+TEST_GROUP_LINK'}
GROUP_CHAT_ID=
MPESA_NUMBER=0791260817
PAYMENT_AMOUNT=50
ADMIN_CHAT_ID=
"""
    
    with open('.env.payment', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env.payment")
    
    # Update test script with user's phone
    if your_phone:
        test_script = f'''#!/usr/bin/env python3
"""
Local Payment Test for Agent-21 Scout
Test the payment flow with your own mobile number
"""

import requests
import json
from datetime import datetime

# Test configuration
LOCAL_URL = "http://localhost:5000"
YOUR_PHONE = "{your_phone}"  # Your actual phone number

def test_bot_registration():
    """Test the bot registration flow"""
    print("🤖 Testing bot registration...")
    print("1. Start your bot: python start_payment_bot.py")
    print("2. Message your bot: /start")
    print("3. Then: /join")
    print(f"4. Send your phone: {{YOUR_PHONE}}")
    print("5. Bot should confirm registration")
    print()

def simulate_mpesa_sms():
    """Simulate M-Pesa SMS for testing"""
    print("📱 Simulating M-Pesa SMS...")
    
    # Sample M-Pesa SMS format
    test_sms = {{
        "message": f"Confirmed. Ksh50.00 received from {{YOUR_PHONE.replace('0', '254', 1)}} on {{datetime.now().strftime('%d/%m/%y')}} at {{datetime.now().strftime('%I:%M %p')}}. Account balance is Ksh2,500.00",
        "sender": "MPESA",
        "timestamp": datetime.now().isoformat()
    }}
    
    try:
        response = requests.post(
            f"{{LOCAL_URL}}/sms",
            json=test_sms,
            headers={{"Content-Type": "application/json"}},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ SMS simulation successful!")
            print(f"Response: {{result}}")
            
            if result.get("status") == "ok":
                print("🎉 Payment processed! Check your Telegram for invite link.")
            else:
                print("⚠️ Payment not processed. Check if you registered your phone first.")
        else:
            print(f"❌ SMS simulation failed: {{response.status_code}}")
            print(f"Response: {{response.text}}")
            
    except Exception as e:
        print(f"❌ Error: {{e}}")

def test_webhook_health():
    """Test if webhook is running"""
    print("🏥 Testing webhook health...")
    
    try:
        response = requests.get(f"{{LOCAL_URL}}/", timeout=5)
        if response.status_code == 200:
            print("✅ Webhook is running!")
            return True
        else:
            print("❌ Webhook not responding")
            return False
    except Exception as e:
        print(f"❌ Webhook not running: {{e}}")
        print("Start the bot first: python start_payment_bot.py")
        return False

def main():
    """Main test function"""
    print("🧪 Agent-21 Scout Local Payment Test\\n")
    
    # Step 1: Check if bot is running
    if not test_webhook_health():
        return
    
    print()
    
    # Step 2: Instructions for bot registration
    test_bot_registration()
    
    # Step 3: Wait for user to register
    input("Press Enter after you've registered your phone with the bot...")
    
    # Step 4: Simulate payment
    simulate_mpesa_sms()
    
    print("\\n📋 What should happen:")
    print("1. ✅ Bot receives simulated M-Pesa SMS")
    print("2. ✅ Bot matches your phone number")
    print("3. ✅ Bot sends you the group invite link")
    print("4. ✅ You get access to premium group")

if __name__ == "__main__":
    main()'''
        
        with open('test_local_payment.py', 'w') as f:
            f.write(test_script)
        
        print(f"✅ Updated test script with your phone: {your_phone}")
    
    print("\n🚀 Setup complete!")
    print("\n📋 Next steps:")
    print("1. pip install -r requirements.txt")
    print("2. python start_payment_bot.py")
    print("3. In another terminal: python test_local_payment.py")

if __name__ == "__main__":
    create_test_env()