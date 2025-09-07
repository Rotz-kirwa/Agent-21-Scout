#!/usr/bin/env python3
"""
Test software engineering jobs
"""

from telegram_jobs import JobScout

def test_software_jobs():
    print("🧪 Testing Software Engineering Jobs...")
    
    scout = JobScout()
    
    # Test software dev jobs
    print("\n1. Testing software development jobs...")
    software_jobs = scout.fetch_automattic_jobs(["developer", "software", "programming"])
    print(f"   Found {len(software_jobs)} Automattic software jobs")
    
    # Test tech company jobs
    print("\n2. Testing tech company jobs...")
    buffer_jobs = scout.fetch_buffer_jobs(["developer", "programming"])
    doist_jobs = scout.fetch_doist_jobs(["developer", "mobile", "backend"])
    print(f"   Found {len(buffer_jobs)} Buffer + {len(doist_jobs)} Doist jobs")
    
    # Test Amazon software jobs
    print("\n3. Testing Amazon software jobs...")
    amazon_jobs = scout.fetch_amazon_jobs(["developer", "software", "python"])
    print(f"   Found {len(amazon_jobs)} Amazon software jobs")
    
    # Show sample jobs
    all_software_jobs = software_jobs + buffer_jobs + doist_jobs + amazon_jobs
    
    if all_software_jobs:
        print(f"\n📋 Sample Software Engineering Jobs:")
        for i, job in enumerate(all_software_jobs[:8], 1):
            print(f"   {i}. {job['title']}")
            print(f"      Company: {job['company']}")
            print(f"      Salary: {job['salary']}")
            print(f"      Location: {job['location']}")
            print()
    
    return len(all_software_jobs)

if __name__ == "__main__":
    total_jobs = test_software_jobs()
    print(f"\n🎉 Found {total_jobs} total software engineering jobs!")
    print("💡 These are included in your daily notifications!")