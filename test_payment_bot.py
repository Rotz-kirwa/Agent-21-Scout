#!/usr/bin/env python3
"""
Test script for Agent-21 Payment Bot
"""

import requests
import json
from datetime import datetime

# Configuration
WEBHOOK_URL = "http://localhost:5000"  # Change to your deployed URL

def test_health_check():
    """Test health endpoint"""
    try:
        response = requests.get(f"{WEBHOOK_URL}/health")
        print(f"✅ Health Check: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health Check Failed: {e}")
        return False

def test_webhook():
    """Test webhook endpoint"""
    try:
        test_data = {
            "test": "message",
            "timestamp": datetime.now().isoformat()
        }
        
        response = requests.post(
            f"{WEBHOOK_URL}/webhook/test",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"✅ Webhook Test: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Webhook Test Failed: {e}")
        return False

def test_sms_processing():
    """Test SMS processing"""
    try:
        # Simulate M-Pesa SMS
        sms_data = {
            "message": "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456",
            "sender": "MPESA",
            "timestamp": datetime.now().isoformat()
        }
        
        response = requests.post(
            f"{WEBHOOK_URL}/webhook/sms",
            json=sms_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"✅ SMS Processing: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ SMS Processing Failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("🧪 Testing Agent-21 Payment Bot...\n")
    
    tests = [
        ("Health Check", test_health_check),
        ("Webhook Test", test_webhook),
        ("SMS Processing", test_sms_processing)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        result = test_func()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! Bot is ready for deployment.")
    else:
        print("⚠️ Some tests failed. Check the configuration.")

if __name__ == "__main__":
    run_all_tests()