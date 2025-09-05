#!/usr/bin/env python3
"""
Test Script for Organized Telegram Job Bot
Run this to see the organized job categorization in action
"""

import sys
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the JobScout class
from telegram_jobs import JobScout, ORGANIZED_JOB_CATEGORIES

def test_organized_bot():
    """Test the organized job categorization system"""
    print("🧪 Testing Organized Telegram Job Bot")
    print("=" * 50)
    
    # Create a JobScout instance
    scout = JobScout()
    
    # Test the categorizer with sample jobs
    print("\n1. Testing Job Categorization:")
    print("-" * 30)
    
    sample_jobs = [
        {
            "title": "Customer Support Representative",
            "company": "LiveWorld",
            "location": "Remote - Worldwide",
            "url": "https://liveworld.com/careers",
            "source": "LiveWorld",
            "salary": "$15/hour"
        },
        {
            "title": "TikTok Content Moderator",
            "company": "ByteDance",
            "location": "Remote - Global",
            "url": "https://careers.tiktok.com",
            "source": "TikTok",
            "salary": "$20/hour"
        },
        {
            "title": "AI Prompt Engineer",
            "company": "Scale AI",
            "location": "Remote - Worldwide",
            "url": "https://scale.com/careers",
            "source": "Scale AI",
            "salary": "$35/hour"
        },
        {
            "title": "Microtask Worker",
            "company": "Amazon MTurk",
            "location": "Remote - Flexible",
            "url": "https://mturk.com",
            "source": "Amazon MTurk",
            "salary": "$8-15/hour"
        }
    ]
    
    # Test categorization
    for job in sample_jobs:
        categorization = scout.categorizer.categorize_job(job)
        print(f"Job: {job['title']}")
        print(f"Level: {categorization['level'].replace('_', ' ').title()}")
        print(f"Category: {categorization['category'].replace('_', ' ').title()}")
        print(f"Salary Range: {categorization['category_data']['salary_range']}")
        print()
    
    # Test organized job summary
    print("\n2. Testing Organized Job Summary:")
    print("-" * 30)
    
    organized_jobs = scout.categorizer.organize_jobs_by_category(sample_jobs)
    summary = scout.categorizer.format_organized_job_summary(organized_jobs)
    
    print(summary)
    
    # Show category system overview
    print("\n3. Available Job Categories:")
    print("-" * 30)
    
    for level_name, level_data in ORGANIZED_JOB_CATEGORIES.items():
        print(f"\n{level_data['emoji']} {level_name.replace('_', ' ').title()}:")
        print(f"   Description: {level_data['description']}")
        print(f"   Requirements: {level_data['skill_requirements']}")
        print("   Categories:")
        for cat_name, cat_data in level_data['categories'].items():
            print(f"     • {cat_name.replace('_', ' ').title()}: {cat_data['salary_range']}")
    
    print("\n4. Testing Sample Specialized Job Fetching:")
    print("-" * 30)
    
    # Test sample specialized job fetching
    test_keywords = ["customer-support", "technical-support", "prompt-engineering", "microtasks"]
    specialized_jobs = scout.fetch_sample_specialized_jobs(test_keywords)
    
    print(f"Found {len(specialized_jobs)} sample specialized jobs:")
    for job in specialized_jobs:
        print(f"• {job['title']} - {job['company']} ({job['salary']})")
    
    print("\n✅ Organized Job Bot Test Complete!")
    print("\nTo run the full bot with Telegram integration:")
    print("python telegram_jobs.py")

if __name__ == "__main__":
    test_organized_bot()