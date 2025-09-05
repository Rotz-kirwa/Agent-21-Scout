#!/usr/bin/env python3
"""
Test the expanded job categorization system with new categories
"""

import sys
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram_jobs import JobScout, ORGANIZED_JOB_CATEGORIES

def test_expanded_categories():
    """Test the expanded job categorization system"""
    print("🧪 Testing Expanded Job Categorization System")
    print("=" * 60)
    
    scout = JobScout()
    
    # Test jobs from all new categories
    test_jobs = [
        # Entry Level
        {
            "title": "Customer Support Representative",
            "company": "LiveWorld",
            "location": "Remote - Worldwide",
            "url": "https://liveworld.com/careers",
            "source": "LiveWorld",
            "salary": "$15/hour"
        },
        {
            "title": "Data Entry Specialist",
            "company": "Clickworker",
            "location": "Remote - Worldwide",
            "url": "https://clickworker.com/jobs",
            "source": "Clickworker",
            "salary": "$12/hour"
        },
        
        # Intermediate Level - New Categories
        {
            "title": "Sales Development Representative",
            "company": "HubSpot",
            "location": "Remote - Worldwide",
            "url": "https://hubspot.com/careers",
            "source": "HubSpot",
            "salary": "$25/hour + commission"
        },
        {
            "title": "Product Manager - Remote",
            "company": "Tech Startup",
            "location": "Remote - Worldwide",
            "url": "https://example-startup.com/careers",
            "source": "Tech Startups",
            "salary": "$35-45/hour"
        },
        {
            "title": "Shopify Store Manager",
            "company": "E-commerce Agency",
            "location": "Remote - Worldwide",
            "url": "https://shopify-agency.com/careers",
            "source": "Shopify Partners",
            "salary": "$20-30/hour"
        },
        
        # Expert Level - New Categories
        {
            "title": "Medical Transcriptionist",
            "company": "3M Health Information Systems",
            "location": "Remote - Worldwide",
            "url": "https://3m.com/careers",
            "source": "3M Health",
            "salary": "$22-30/hour"
        },
        {
            "title": "Remote Translator",
            "company": "Lionbridge",
            "location": "Remote - Worldwide",
            "url": "https://lionbridge.com/careers",
            "source": "Lionbridge",
            "salary": "$25-35/hour"
        },
        {
            "title": "AI Prompt Engineer",
            "company": "Scale AI",
            "location": "Remote - Worldwide",
            "url": "https://scale.com/careers",
            "source": "Scale AI",
            "salary": "$35/hour"
        },
        
        # Flexible Opportunities - New Category
        {
            "title": "Online Research Participant",
            "company": "Prolific",
            "location": "Remote - Worldwide",
            "url": "https://prolific.co",
            "source": "Prolific",
            "salary": "$12-18/hour"
        },
        {
            "title": "User Experience Tester",
            "company": "UserTesting",
            "location": "Remote - Worldwide",
            "url": "https://usertesting.com/careers",
            "source": "UserTesting",
            "salary": "$15/hour"
        }
    ]
    
    print("\n1. Testing Individual Job Categorization:")
    print("-" * 50)
    
    for job in test_jobs:
        categorization = scout.categorizer.categorize_job(job)
        print(f"Job: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Level: {categorization['level'].replace('_', ' ').title()}")
        print(f"Category: {categorization['category'].replace('_', ' ').title()}")
        print(f"Salary Range: {categorization['category_data']['salary_range']}")
        print(f"Requirements: {categorization['category_data']['requirements']}")
        print()
    
    print("\n2. Testing Organized Job Summary:")
    print("-" * 50)
    
    organized_jobs = scout.categorizer.organize_jobs_by_category(test_jobs)
    summary = scout.categorizer.format_organized_job_summary(organized_jobs)
    
    print(summary)
    
    print("\n3. Category Distribution:")
    print("-" * 50)
    
    for level, jobs in organized_jobs.items():
        if jobs:
            level_data = scout.categorizer.organized_categories[level]
            print(f"\n{level_data['emoji']} {level.replace('_', ' ').title()} ({len(jobs)} jobs):")
            
            categories = {}
            for job in jobs:
                cat = job["categorization"]["category"]
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(job)
            
            for category, category_jobs in categories.items():
                cat_data = category_jobs[0]["categorization"]["category_data"]
                print(f"  💼 {category.replace('_', ' ').title()} ({len(category_jobs)} jobs)")
                print(f"     💰 {cat_data['salary_range']}")
                print(f"     📋 {cat_data['requirements']}")
                for job in category_jobs:
                    print(f"     • {job['title']} - {job['company']}")
    
    print("\n4. All Available Categories:")
    print("-" * 50)
    
    total_categories = 0
    for level_name, level_data in ORGANIZED_JOB_CATEGORIES.items():
        print(f"\n{level_data['emoji']} {level_name.replace('_', ' ').title()}:")
        print(f"   Requirements: {level_data['skill_requirements']}")
        print("   Categories:")
        for cat_name, cat_data in level_data['categories'].items():
            print(f"     • {cat_name.replace('_', ' ').title()}: {cat_data['salary_range']}")
            total_categories += 1
    
    print(f"\n📊 Total Categories Available: {total_categories}")
    print(f"📈 Total Jobs Tested: {len(test_jobs)}")
    print(f"🎯 Categories Used: {len(set(job['categorization']['category'] for job in test_jobs if 'categorization' in job))}")
    
    print("\n✅ Expanded Category Test Complete!")

if __name__ == "__main__":
    test_expanded_categories()