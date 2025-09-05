#!/usr/bin/env python3
"""
Test the comprehensive error handling system
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions
def mock_send_telegram_message(message):
    print("TELEGRAM MESSAGE:")
    print("-" * 40)
    print(message)
    print("-" * 40)
    print()

def mock_send_job_summary(jobs):
    pass

import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message
telegram_bot.send_job_summary = mock_send_job_summary

from telegram_jobs import JobScout

def test_error_handling():
    scout = JobScout()
    test_keywords = ["remote", "developer", "support"]
    
    print("🧪 Testing Comprehensive Error Handling")
    print("=" * 50)
    
    # Test a function that should work
    print("Testing working function:")
    jobs = scout.fetch_with_comprehensive_error_handling(
        scout.fetch_sample_specialized_jobs, 
        "Sample Specialized Jobs", 
        test_keywords
    )
    print(f"Result: {len(jobs)} jobs")
    print()
    
    # Test a function that might fail (Zapier)
    print("Testing potentially failing function:")
    jobs = scout.fetch_with_comprehensive_error_handling(
        scout.fetch_zapier_jobs, 
        "Zapier", 
        test_keywords
    )
    print(f"Result: {len(jobs)} jobs")
    print()
    
    # Test fallback system
    print("Testing fallback system:")
    fallback_jobs = scout._get_comprehensive_fallback_jobs("Zapier")
    print(f"Fallback jobs: {len(fallback_jobs)}")
    if fallback_jobs:
        print(f"Example: {fallback_jobs[0]['title']} - {fallback_jobs[0]['company']}")
    print()
    
    # Show source stats
    print("Source Statistics:")
    for source, stats in scout.source_stats.items():
        print(f"  {source}: {stats}")

if __name__ == "__main__":
    test_error_handling()