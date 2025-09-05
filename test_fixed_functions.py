#!/usr/bin/env python3
"""
Quick test of the fixed functions
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions
def mock_send_telegram_message(message):
    pass

def mock_send_job_summary(jobs):
    pass

import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message
telegram_bot.send_job_summary = mock_send_job_summary

from telegram_jobs import JobScout

def test_fixed_functions():
    scout = JobScout()
    test_keywords = ["remote", "developer", "support", "assistant", "data"]
    
    functions_to_test = [
        'fetch_sample_specialized_jobs',
        'fetch_sales_bizdev_jobs',
        'fetch_product_management_jobs',
        'fetch_ecommerce_jobs',
        'fetch_healthcare_remote_jobs',
        'fetch_translation_jobs',
        'fetch_research_survey_jobs'
    ]
    
    print("🧪 Testing Fixed Functions")
    print("=" * 40)
    
    for func_name in functions_to_test:
        try:
            func = getattr(scout, func_name)
            jobs = func(test_keywords)
            print(f"✅ {func_name}: {len(jobs)} jobs")
            
            # Show first job as example
            if jobs:
                job = jobs[0]
                print(f"   Example: {job['title']} - {job['company']} ({job.get('salary', 'N/A')})")
        except Exception as e:
            print(f"❌ {func_name}: ERROR - {e}")
        print()

if __name__ == "__main__":
    test_fixed_functions()