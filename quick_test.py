#!/usr/bin/env python3
"""
Quick test for Agent-21 Scout without API timeouts
"""

from telegram_bot import send_telegram_message

# Test message
try:
    result = send_telegram_message("🧪 *Agent-21 Scout Quick Test*\n\nTesting reliable job sources...")
    if result:
        print("✅ Test message sent!")
    else:
        print("❌ Test failed")
except Exception as e:
    print(f"Error: {e}")

# Test job scout with limited scope
try:
    from telegram_jobs import JobScout
    scout = JobScout()
    
    # Add some test jobs
    test_jobs = [
        {
            "title": "Remote Python Developer",
            "company": "TechCorp Global",
            "location": "Remote - Worldwide",
            "url": "https://example.com/job1",
            "source": "Test Source",
            "salary": "$50k-80k/year"
        }
    ]
    
    scout.jobs_found = test_jobs
    scout.total_jobs = len(test_jobs)
    scout.sources = ["Test Source"]
    
    # Send test job
    send_telegram_message(scout.format_job(test_jobs[0]))
    print("✅ Job formatting test passed!")
    
except Exception as e:
    print(f"❌ Job test error: {e}")

print("🎯 Quick test completed!")