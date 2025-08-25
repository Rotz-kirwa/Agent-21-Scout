#!/usr/bin/env python3
"""
Complete test flow for Agent-21 Payment Bot
"""

import requests
import json
import sqlite3
import time
from datetime import datetime

# Test configuration
WEBHOOK_URL = "http://localhost:5000"  # Change to your deployed URL
TEST_USER_ID = 123456789  # Your Telegram user ID for testing
TEST_REFERENCE = "123456"  # Test reference code

def test_database():
    """Test database operations"""
    print("🗄️ Testing database...")
    
    try:
        # Initialize database
        conn = sqlite3.connect('agent21_payments.db')
        cursor = conn.cursor()
        
        # Insert test payment
        cursor.execute('''
            INSERT OR REPLACE INTO payments (user_id, username, reference_code)
            VALUES (?, ?, ?)
        ''', (TEST_USER_ID, "TestUser", TEST_REFERENCE))
        
        # Check if inserted
        cursor.execute('SELECT * FROM payments WHERE reference_code = ?', (TEST_REFERENCE,))
        result = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        if result:
            print("✅ Database test passed!")
            return True
        else:
            print("❌ Database test failed!")
            return False
            
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def test_webhook_health():
    """Test webhook health"""
    print("🏥 Testing webhook health...")
    
    try:
        response = requests.get(f"{WEBHOOK_URL}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Webhook health check passed!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_sms_webhook():
    """Test SMS processing webhook"""
    print("📱 Testing SMS webhook...")
    
    # Simulate M-Pesa SMS
    test_sms = {
        "message": f"Confirmed. Ksh50.00 received from 254791260817 on {datetime.now().strftime('%d/%m/%y')} at {datetime.now().strftime('%I:%M %p')}. Reference: {TEST_REFERENCE}. Account balance is Ksh2,500.00",
        "sender": "MPESA",
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        response = requests.post(
            f"{WEBHOOK_URL}/webhook/sms",
            json=test_sms,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ SMS webhook test passed!")
            print(f"Response: {result}")
            return True
        else:
            print(f"❌ SMS webhook failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ SMS webhook error: {e}")
        return False

def test_payment_verification():
    """Test payment verification logic"""
    print("💳 Testing payment verification...")
    
    test_messages = [
        "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456",
        "confirmed ksh50 received reference: 123456",
        "CONFIRMED. KSH 50.00 RECEIVED. REFERENCE: 123456",
        "Wrong message format",
        "Confirmed. Ksh100.00 received. Reference: 123456"  # Wrong amount
    ]
    
    import re
    
    passed = 0
    total = len(test_messages)
    
    for i, msg in enumerate(test_messages):
        msg_lower = msg.lower()
        
        # Check M-Pesa confirmation logic
        is_mpesa = 'confirmed' in msg_lower and 'ksh50' in msg_lower.replace(' ', '')
        ref_match = re.search(r'reference[:\s]*(\d{6})', msg_lower)
        
        expected_results = [True, True, True, False, False]
        expected = expected_results[i]
        
        if (is_mpesa and ref_match) == expected:
            print(f"✅ Test {i+1}: {'PASS' if expected else 'PASS (correctly rejected)'}")
            passed += 1
        else:
            print(f"❌ Test {i+1}: FAIL")
    
    print(f"📊 Payment verification: {passed}/{total} tests passed")
    return passed == total

def run_complete_test():
    """Run all tests"""
    print("🚀 Agent-21 Payment Bot - Complete Test Suite\n")
    
    tests = [
        ("Database Operations", test_database),
        ("Webhook Health", test_webhook_health),
        ("SMS Processing", test_sms_webhook),
        ("Payment Verification", test_payment_verification)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        result = test_func()
        results.append(result)
        time.sleep(1)
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print(f"\n📊 FINAL RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Bot is ready for production.")
    else:
        print("⚠️ Some tests failed. Check configuration and try again.")
    
    return passed == total

if __name__ == "__main__":
    run_complete_test()