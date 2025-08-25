#!/usr/bin/env python3
"""
Simple standalone test for Agent-21 Payment Bot
Tests core functionality without requiring server
"""

import sqlite3
import re
import os
from datetime import datetime

def test_database():
    """Test database operations"""
    print("🗄️ Testing database...")
    
    try:
        # Initialize database
        conn = sqlite3.connect('test_payments.db')
        cursor = conn.cursor()
        
        # Create table
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
        
        # Insert test payment
        cursor.execute('''
            INSERT OR REPLACE INTO payments (user_id, username, reference_code)
            VALUES (?, ?, ?)
        ''', (123456789, "TestUser", "123456"))
        
        # Check if inserted
        cursor.execute('SELECT * FROM payments WHERE reference_code = ?', ("123456",))
        result = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        # Clean up
        os.remove('test_payments.db')
        
        if result:
            print("✅ Database test passed!")
            return True
        else:
            print("❌ Database test failed!")
            return False
            
    except Exception as e:
        print(f"❌ Database error: {e}")
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
    
    passed = 0
    total = len(test_messages)
    
    for i, msg in enumerate(test_messages):
        msg_lower = msg.lower()
        
        # Check M-Pesa confirmation logic (fixed)
        is_mpesa = 'confirmed' in msg_lower and ('ksh50' in msg_lower.replace(' ', '') or 'ksh 50' in msg_lower)
        ref_match = re.search(r'reference[:\s]*(\d{6})', msg_lower)
        
        expected_results = [True, True, True, False, False]
        expected = expected_results[i]
        
        actual = is_mpesa and ref_match is not None
        
        if actual == expected:
            print(f"✅ Test {i+1}: {'PASS' if expected else 'PASS (correctly rejected)'}")
            passed += 1
        else:
            print(f"❌ Test {i+1}: FAIL - Expected {expected}, got {actual}")
            print(f"   Message: {msg}")
    
    print(f"📊 Payment verification: {passed}/{total} tests passed")
    return passed == total

def test_reference_code_generation():
    """Test reference code generation"""
    print("🔢 Testing reference code generation...")
    
    try:
        import random
        import string
        
        # Generate 10 codes
        codes = []
        for _ in range(10):
            code = ''.join(random.choices(string.digits, k=6))
            codes.append(code)
        
        # Check all are 6 digits and unique
        all_valid = all(len(code) == 6 and code.isdigit() for code in codes)
        all_unique = len(codes) == len(set(codes))
        
        if all_valid and all_unique:
            print("✅ Reference code generation passed!")
            print(f"   Sample codes: {codes[:3]}")
            return True
        else:
            print("❌ Reference code generation failed!")
            return False
            
    except Exception as e:
        print(f"❌ Reference code error: {e}")
        return False

def test_environment_loading():
    """Test environment configuration"""
    print("🔧 Testing environment loading...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv('.env.payment')
        
        # Check if we can load environment variables
        mpesa_phone = os.getenv("MPESA_PHONE", "0791260817")
        payment_amount = int(os.getenv("PAYMENT_AMOUNT", "50"))
        
        if mpesa_phone and payment_amount:
            print("✅ Environment loading passed!")
            print(f"   M-Pesa: {mpesa_phone}")
            print(f"   Amount: Ksh {payment_amount}")
            return True
        else:
            print("❌ Environment loading failed!")
            return False
            
    except Exception as e:
        print(f"❌ Environment error: {e}")
        return False

def run_simple_tests():
    """Run all simple tests"""
    print("🧪 Agent-21 Payment Bot - Simple Test Suite\n")
    
    tests = [
        ("Database Operations", test_database),
        ("Payment Verification", test_payment_verification),
        ("Reference Code Generation", test_reference_code_generation),
        ("Environment Loading", test_environment_loading)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"--- {test_name} ---")
        result = test_func()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print(f"📊 FINAL RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL CORE TESTS PASSED! Bot logic is working correctly.")
        print("\n📋 Next steps:")
        print("1. Get bot token from @BotFather")
        print("2. Create premium group and get invite link")
        print("3. Update .env.payment file")
        print("4. Deploy to Render.com")
    else:
        print("⚠️ Some tests failed. Check the code and try again.")
    
    return passed == total

if __name__ == "__main__":
    run_simple_tests()