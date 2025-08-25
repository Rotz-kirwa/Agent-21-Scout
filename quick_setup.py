#!/usr/bin/env python3
"""
Quick setup script for Agent-21 Payment Bot
"""

import os
import subprocess
import sys

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "payment_requirements.txt"])
        print("✅ Dependencies installed!")
        return True
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_environment():
    """Check if environment variables are set"""
    print("🔧 Checking environment configuration...")
    
    required_vars = [
        "PAYMENT_BOT_TOKEN",
        "GROUP_INVITE_LINK", 
        "MPESA_PHONE",
        "PAYMENT_AMOUNT"
    ]
    
    missing = []
    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)
    
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        print("📝 Please update your .env.payment file")
        return False
    else:
        print("✅ Environment configured!")
        return True

def create_test_env():
    """Create test environment file"""
    print("📝 Creating test environment...")
    
    test_env = """# Test Environment for Agent-21 Payment Bot
PAYMENT_BOT_TOKEN=TEST_TOKEN_REPLACE_ME
GROUP_INVITE_LINK=https://t.me/+TEST_LINK_REPLACE_ME
MPESA_PHONE=0791260817
PAYMENT_AMOUNT=50
WEBHOOK_PORT=5000
"""
    
    with open('.env.payment', 'w') as f:
        f.write(test_env)
    
    print("✅ Test environment created!")
    print("📋 Please update .env.payment with your actual values")

def main():
    """Main setup function"""
    print("🚀 Agent-21 Payment Bot Setup\n")
    
    # Step 1: Install dependencies
    if not install_dependencies():
        return
    
    # Step 2: Create test environment if not exists
    if not os.path.exists('.env.payment'):
        create_test_env()
    
    # Step 3: Check environment
    from dotenv import load_dotenv
    load_dotenv('.env.payment')
    
    env_ok = check_environment()
    
    # Step 4: Instructions
    print("\n📋 Next Steps:")
    print("1. Update .env.payment with your bot token and group link")
    print("2. Set up SMS forwarder app (see sms_forwarder_guide.md)")
    print("3. Deploy to Render.com or run locally")
    print("4. Test with: python test_payment_bot.py")
    
    if env_ok:
        print("\n🎯 Ready to deploy!")
    else:
        print("\n⚠️ Please configure environment first")

if __name__ == "__main__":
    main()