#!/usr/bin/env python3
"""
Agent-21 Scout Payment Bot Creator
Creates and configures the complete payment system
"""

import os
import subprocess
import sys

def create_bot_instructions():
    """Create step-by-step bot creation guide"""
    
    instructions = """
🤖 STEP 1: CREATE TELEGRAM BOT

1. Open Telegram and message @BotFather
2. Send: /newbot
3. Bot name: Agent-21 Scout Payment Bot
4. Username: @Agent21PaymentBot (or similar available)
5. Copy the bot token (looks like: 123456789:ABCdefGhIjKlMnOpQrStUvWxYz)

🏢 STEP 2: CREATE PREMIUM GROUP

1. Create new Telegram group
2. Name: "Agent-21 Scout Premium Jobs"
3. Add your payment bot as admin
4. Go to Group Settings → Invite Links
5. Create invite link and copy it

📝 STEP 3: UPDATE CONFIGURATION

Edit the .env.payment file with your actual values:
- PAYMENT_BOT_TOKEN=your_bot_token_here
- GROUP_INVITE_LINK=https://t.me/+your_group_link

🚀 STEP 4: DEPLOY

Choose one:
A) Local testing: python render_deploy.py
B) Production: Deploy to Render.com (see render_setup.md)

📱 STEP 5: SMS FORWARDER

Install SMS forwarder app on Android and configure webhook
    """
    
    print(instructions)
    
    # Create environment file
    env_content = """# Agent-21 Scout Payment Bot Configuration
# Replace with your actual values

PAYMENT_BOT_TOKEN=YOUR_BOT_TOKEN_FROM_BOTFATHER
GROUP_INVITE_LINK=https://t.me/+YOUR_GROUP_INVITE_LINK
MPESA_PHONE=0791260817
PAYMENT_AMOUNT=50
WEBHOOK_PORT=5000
"""
    
    with open('.env.payment', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env.payment file")
    print("📝 Please update it with your actual bot token and group link")

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "payment_requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def test_system():
    """Test the payment system"""
    print("🧪 Testing payment system...")
    
    try:
        # Run simple test
        result = subprocess.run([sys.executable, "simple_test.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ System tests passed!")
            print(result.stdout)
            return True
        else:
            print("❌ System tests failed!")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def create_startup_script():
    """Create easy startup script"""
    
    startup_script = """#!/usr/bin/env python3
# Agent-21 Scout Payment Bot Startup

import os
import sys
from dotenv import load_dotenv

# Load environment
load_dotenv('.env.payment')

# Check configuration
bot_token = os.getenv('PAYMENT_BOT_TOKEN')
group_link = os.getenv('GROUP_INVITE_LINK')

if not bot_token or bot_token == 'YOUR_BOT_TOKEN_FROM_BOTFATHER':
    print("❌ Please update PAYMENT_BOT_TOKEN in .env.payment")
    sys.exit(1)

if not group_link or 'YOUR_GROUP' in group_link:
    print("❌ Please update GROUP_INVITE_LINK in .env.payment")
    sys.exit(1)

print("🚀 Starting Agent-21 Payment Bot...")
print(f"💳 M-Pesa: {os.getenv('MPESA_PHONE')}")
print(f"💰 Amount: Ksh {os.getenv('PAYMENT_AMOUNT')}")

# Start the bot
from render_deploy import app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
"""
    
    with open('start_payment_bot.py', 'w') as f:
        f.write(startup_script)
    
    print("✅ Created start_payment_bot.py")

def main():
    """Main setup function"""
    print("🎯 Agent-21 Scout Payment Bot Creator\n")
    
    # Step 1: Install dependencies
    if not install_dependencies():
        return
    
    # Step 2: Create configuration
    create_bot_instructions()
    
    # Step 3: Create startup script
    create_startup_script()
    
    # Step 4: Test system
    test_system()
    
    print("\n🎉 SETUP COMPLETE!")
    print("\n📋 NEXT STEPS:")
    print("1. Follow the instructions above to create your bot")
    print("2. Update .env.payment with your bot token and group link")
    print("3. Test locally: python start_payment_bot.py")
    print("4. Deploy to production: Follow render_setup.md")
    
    print("\n💰 REVENUE POTENTIAL:")
    print("• 100 users/month = Ksh 5,000")
    print("• 500 users/month = Ksh 25,000") 
    print("• 1000 users/month = Ksh 50,000")

if __name__ == "__main__":
    main()