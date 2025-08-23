#!/usr/bin/env python3
"""
Agent-21 Scout Test Suite
Quick test to verify all components are working
"""

from telegram_bot import send_telegram_message, send_job_summary
import time

def test_agent21():
    """Test Agent-21 Scout functionality"""
    
    print("🤖 Testing Agent-21 Scout...")
    
    # Test 1: Basic message
    try:
        result = send_telegram_message("🧪 *Agent-21 Scout Test Initiated*\n\nTesting all systems...")
        if result:
            print("✅ Basic messaging: PASSED")
        else:
            print("❌ Basic messaging: FAILED")
            return False
    except Exception as e:
        print(f"❌ Basic messaging error: {e}")
        return False
    
    time.sleep(1)
    
    # Test 2: Job summary
    try:
        result = send_job_summary(5, ["Test Source", "Demo API"])
        if result:
            print("✅ Job summary: PASSED")
        else:
            print("❌ Job summary: FAILED")
    except Exception as e:
        print(f"❌ Job summary error: {e}")
    
    time.sleep(1)
    
    # Test 3: Sample job format
    sample_job = {
        "title": "Senior Python Developer",
        "company": "Tech Corp",
        "location": "Remote",
        "url": "https://example.com/job",
        "source": "Test API",
        "salary": "$80k - $120k"
    }
    
    try:
        from telegram_jobs import JobScout
        scout = JobScout()
        formatted_job = scout.format_job(sample_job)
        
        result = send_telegram_message(formatted_job)
        if result:
            print("✅ Job formatting: PASSED")
        else:
            print("❌ Job formatting: FAILED")
    except Exception as e:
        print(f"❌ Job formatting error: {e}")
    
    time.sleep(1)
    
    # Test completion
    send_telegram_message("✅ *Agent-21 Scout Test Complete*\n\nAll systems operational! Ready for job scouting. 🎯")
    print("\n🎉 Agent-21 Scout test completed!")
    print("📋 Check your Telegram for test messages")
    print("🚀 Ready to run: python telegram_jobs.py")
    
    return True

if __name__ == "__main__":
    test_agent21()