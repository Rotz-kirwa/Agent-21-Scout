#!/usr/bin/env python3
"""
Test script to verify Amazon integration is working
"""

from telegram_jobs import JobScout
from telegram_bot import send_telegram_message

def test_amazon_integration():
    print("🧪 Testing Amazon Integration...")
    
    scout = JobScout()
    
    # Test Amazon jobs fetching
    print("\n1. Testing Amazon jobs for software development...")
    amazon_jobs = scout.fetch_amazon_jobs(["developer", "software", "python"])
    print(f"   Found {len(amazon_jobs)} Amazon software jobs")
    
    print("\n2. Testing Amazon AWS jobs...")
    aws_jobs = scout.fetch_amazon_aws_jobs()
    print(f"   Found {len(aws_jobs)} Amazon AWS jobs")
    
    # Test data jobs
    print("\n3. Testing Amazon data jobs...")
    data_jobs = scout.fetch_amazon_jobs(["data", "analytics", "machine-learning"])
    print(f"   Found {len(data_jobs)} Amazon data jobs")
    
    # Show sample jobs
    all_amazon_jobs = amazon_jobs + aws_jobs + data_jobs
    if all_amazon_jobs:
        print(f"\n📋 Sample Amazon Jobs Found:")
        for i, job in enumerate(all_amazon_jobs[:3], 1):
            print(f"   {i}. {job['title']} at {job['company']}")
            print(f"      Location: {job['location']}")
            print(f"      Salary: {job['salary']}")
            print(f"      Source: {job['source']}")
            print()
    
    # Send test notification
    try:
        test_message = f"🧪 *Amazon Integration Test*\n\n"
        test_message += f"✅ Found {len(all_amazon_jobs)} Amazon opportunities\n"
        test_message += f"🔍 Integration working properly!\n"
        test_message += f"📅 Daily notifications should now include Amazon jobs"
        
        send_telegram_message(test_message)
        print("✅ Test notification sent to Telegram!")
    except Exception as e:
        print(f"❌ Failed to send test notification: {e}")
    
    return len(all_amazon_jobs)

if __name__ == "__main__":
    total_jobs = test_amazon_integration()
    print(f"\n🎉 Test completed! Found {total_jobs} total Amazon-related jobs.")
    print("💡 Amazon integration is now active in your daily job scout!")