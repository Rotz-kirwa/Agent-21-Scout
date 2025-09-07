#!/usr/bin/env python3
"""
Test social media moderation jobs integration
"""

from telegram_jobs import JobScout

def test_moderation_jobs():
    print("🧪 Testing Social Media Moderation Jobs...")
    
    scout = JobScout()
    
    # Test TikTok moderation jobs
    print("\n1. Testing TikTok moderation jobs...")
    tiktok_jobs = scout.fetch_social_media_platform_jobs(["tiktok-moderator", "content-moderator"])
    print(f"   Found {len(tiktok_jobs)} TikTok moderation jobs")
    
    # Test general social media jobs
    print("\n2. Testing general social media moderation...")
    social_jobs = scout.fetch_bpo_outsourcing_jobs(["content-moderator", "trust-safety"])
    print(f"   Found {len(social_jobs)} BPO moderation jobs")
    
    # Test platform-specific jobs
    print("\n3. Testing platform-specific moderation...")
    platform_jobs = scout.fetch_customer_support_platform_jobs(["platform-support", "user-safety"])
    print(f"   Found {len(platform_jobs)} platform support jobs")
    
    # Show sample moderation jobs
    all_moderation_jobs = tiktok_jobs + social_jobs + platform_jobs
    
    if all_moderation_jobs:
        print(f"\n📋 Sample Social Media Moderation Jobs:")
        for i, job in enumerate(all_moderation_jobs[:8], 1):
            print(f"   {i}. {job['title']}")
            print(f"      Company: {job['company']}")
            print(f"      Salary: {job['salary']}")
            print(f"      Location: {job['location']}")
            print()
    
    return len(all_moderation_jobs)

if __name__ == "__main__":
    total_jobs = test_moderation_jobs()
    print(f"\n🎉 Found {total_jobs} total social media moderation jobs!")
    print("💡 These are included in your daily 25-30 job notifications!")