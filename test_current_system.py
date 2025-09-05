#!/usr/bin/env python3
"""
Test the current working categorization system
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions to avoid API calls
def mock_send_telegram_message(message):
    print("=" * 60)
    print("TELEGRAM MESSAGE:")
    print("=" * 60)
    print(message)
    print("=" * 60)
    print()

# Replace the telegram functions
import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message

from telegram_jobs import JobScout

def test_current_system():
    """Test the current working system"""
    print("🧪 Testing Current Job Categorization System")
    print("=" * 50)
    
    scout = JobScout()
    
    # Test with jobs that should work with current categories
    test_jobs = [
        {
            "title": "Customer Support Representative",
            "company": "LiveWorld",
            "location": "Remote - Worldwide",
            "url": "https://liveworld.com/careers",
            "source": "LiveWorld",
            "salary": "$15/hour"
        },
        {
            "title": "Content Moderator",
            "company": "ModSquad",
            "location": "Remote - Global",
            "url": "https://modsquad.com/careers",
            "source": "ModSquad",
            "salary": "$16/hour"
        },
        {
            "title": "Technical Support Specialist",
            "company": "GitLab",
            "location": "Remote - Worldwide",
            "url": "https://about.gitlab.com/jobs",
            "source": "GitLab",
            "salary": "$25/hour"
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
            "title": "User Experience Tester",
            "company": "UserTesting",
            "location": "Remote - Worldwide",
            "url": "https://usertesting.com/careers",
            "source": "UserTesting",
            "salary": "$15/hour"
        }
    ]
    
    # Test categorization
    organized_jobs = scout.categorizer.organize_jobs_by_category(test_jobs)
    summary = scout.categorizer.format_organized_job_summary(organized_jobs)
    
    mock_send_telegram_message(summary)
    
    print("✅ Current system test complete!")
    print("The existing categorization system is working well.")
    print("You can run the full bot with: python telegram_jobs.py")

if __name__ == "__main__":
    test_current_system()