#!/usr/bin/env python3
"""
Debug the categorization system
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram_jobs import JobScout, ORGANIZED_JOB_CATEGORIES

def debug_categories():
    """Debug the categorization system"""
    print("🔍 Debugging Job Categorization System")
    print("=" * 50)
    
    scout = JobScout()
    
    # Check if the categories exist
    print("1. Checking category structure:")
    print("-" * 30)
    
    for level_name, level_data in ORGANIZED_JOB_CATEGORIES.items():
        print(f"\n{level_name}:")
        for cat_name in level_data['categories'].keys():
            print(f"  - {cat_name}")
    
    # Test a sales job specifically
    sales_job = {
        "title": "Sales Development Representative",
        "company": "HubSpot",
        "location": "Remote - Worldwide",
        "url": "https://hubspot.com/careers",
        "source": "HubSpot",
        "salary": "$25/hour + commission"
    }
    
    print(f"\n2. Testing sales job categorization:")
    print("-" * 30)
    print(f"Job: {sales_job['title']}")
    print(f"Company: {sales_job['company']}")
    
    job_text = f"{sales_job['title'].lower()} {sales_job['company'].lower()}"
    print(f"Job text: '{job_text}'")
    
    # Check if sales keywords match
    sales_keywords = ["sales", "business", "account", "executive"]
    matches = [word for word in sales_keywords if word in job_text]
    print(f"Matching keywords: {matches}")
    
    # Try categorization
    try:
        categorization = scout.categorizer.categorize_job(sales_job)
        print(f"Categorization successful!")
        print(f"Level: {categorization['level']}")
        print(f"Category: {categorization['category']}")
    except Exception as e:
        print(f"Categorization failed: {e}")
        
        # Check if the category exists
        if "intermediate_level" in ORGANIZED_JOB_CATEGORIES:
            print("intermediate_level exists")
            if "categories" in ORGANIZED_JOB_CATEGORIES["intermediate_level"]:
                print("categories exists")
                cats = ORGANIZED_JOB_CATEGORIES["intermediate_level"]["categories"]
                print(f"Available categories: {list(cats.keys())}")
                if "sales_business_development" in cats:
                    print("sales_business_development exists!")
                else:
                    print("sales_business_development NOT found!")
            else:
                print("categories NOT found")
        else:
            print("intermediate_level NOT found")

if __name__ == "__main__":
    debug_categories()