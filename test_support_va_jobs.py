#!/usr/bin/env python3
"""
Test customer support and virtual assistant jobs
"""

from telegram_jobs import JobScout

def test_support_va_jobs():
    print("🧪 Testing Customer Support & Virtual Assistant Jobs...")
    
    scout = JobScout()
    
    # Test customer support jobs
    print("\n1. Testing customer support jobs...")
    support_jobs = scout.fetch_customer_support_jobs(["customer-support", "technical-support"])
    print(f"   Found {len(support_jobs)} customer support jobs")
    
    # Test virtual assistant jobs
    print("\n2. Testing virtual assistant jobs...")
    va_jobs = scout.fetch_va_support_jobs(["virtual-assistant", "admin-assistant"])
    print(f"   Found {len(va_jobs)} virtual assistant jobs")
    
    # Test guaranteed jobs (always included)
    print("\n3. Testing guaranteed support/VA jobs...")
    guaranteed = scout.get_guaranteed_working_jobs()
    support_va_guaranteed = [j for j in guaranteed if any(word in j['title'].lower() for word in ['support', 'assistant', 'moderator'])]
    print(f"   Found {len(support_va_guaranteed)} guaranteed support/VA jobs")
    
    # Show sample jobs
    all_jobs = support_jobs + va_jobs + support_va_guaranteed
    
    if all_jobs:
        print(f"\n📋 Sample Customer Support & VA Jobs:")
        for i, job in enumerate(all_jobs[:10], 1):
            print(f"   {i}. {job['title']}")
            print(f"      Company: {job['company']}")
            print(f"      Salary: {job['salary']}")
            print(f"      Location: {job['location']}")
            print()
    
    return len(all_jobs)

if __name__ == "__main__":
    total_jobs = test_support_va_jobs()
    print(f"\n🎉 Found {total_jobs} total customer support & VA jobs!")
    print("💡 These are included in your daily notifications!")