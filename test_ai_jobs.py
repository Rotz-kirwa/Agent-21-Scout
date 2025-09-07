#!/usr/bin/env python3
"""
Test AI training and related jobs
"""

from telegram_jobs import JobScout

def test_ai_jobs():
    print("🧪 Testing AI Training & Related Jobs...")
    
    scout = JobScout()
    
    # Test AI training jobs
    print("\n1. Testing AI training jobs...")
    ai_jobs = scout.fetch_ai_training_jobs(["ai-training", "data-annotation", "rater"])
    print(f"   Found {len(ai_jobs)} AI training jobs")
    
    # Test data labeling jobs
    print("\n2. Testing data labeling jobs...")
    data_jobs = scout.fetch_data_labeling_specialist_jobs(["image-labeling", "video-annotation"])
    print(f"   Found {len(data_jobs)} data labeling jobs")
    
    # Test guaranteed AI jobs
    print("\n3. Testing guaranteed AI jobs...")
    guaranteed = scout.get_guaranteed_working_jobs()
    ai_guaranteed = [j for j in guaranteed if any(word in j['title'].lower() for word in ['ai', 'search', 'data', 'annotation'])]
    print(f"   Found {len(ai_guaranteed)} guaranteed AI jobs")
    
    # Show sample jobs
    all_ai_jobs = ai_jobs + data_jobs + ai_guaranteed
    
    if all_ai_jobs:
        print(f"\n📋 Sample AI Training & Related Jobs:")
        for i, job in enumerate(all_ai_jobs[:10], 1):
            print(f"   {i}. {job['title']}")
            print(f"      Company: {job['company']}")
            print(f"      Salary: {job['salary']}")
            print(f"      Location: {job['location']}")
            print()
    
    return len(all_ai_jobs)

if __name__ == "__main__":
    total_jobs = test_ai_jobs()
    print(f"\n🎉 Found {total_jobs} total AI training & related jobs!")
    print("💡 These are included in your daily notifications!")