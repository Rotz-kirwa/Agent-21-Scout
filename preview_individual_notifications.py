#!/usr/bin/env python3
"""
Preview Individual Notifications - Show what the new notification format looks like
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions to show preview
def mock_send_telegram_message(message):
    print("📱 TELEGRAM NOTIFICATION:")
    print("─" * 50)
    print(message)
    print("─" * 50)
    print()

import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message

from telegram_jobs import JobScout

def preview_notifications():
    """Preview what the individual notifications will look like"""
    print("🎯 PREVIEW: Individual Job Notifications")
    print("=" * 60)
    print("This is what you'll receive tomorrow at 6 AM:")
    print()
    
    scout = JobScout()
    
    # Sample jobs from different categories
    sample_jobs = [
        {
            "title": "Python Developer - Remote",
            "company": "GitLab",
            "location": "Remote - Global",
            "salary": "$70-90k/year",
            "url": "https://about.gitlab.com/jobs/",
            "source": "GitLab Careers"
        },
        {
            "title": "Customer Support Specialist",
            "company": "Automattic",
            "location": "Remote - Worldwide",
            "salary": "$25-35/hour",
            "url": "https://automattic.com/work-with-us/",
            "source": "Automattic"
        },
        {
            "title": "Virtual Assistant",
            "company": "Belay Solutions",
            "location": "Remote - US/Canada",
            "salary": "$15-20/hour",
            "url": "https://www.belay.com/careers/",
            "source": "Belay"
        },
        {
            "title": "Content Moderator",
            "company": "ModSquad",
            "location": "Remote - Worldwide",
            "salary": "$16-22/hour",
            "url": "https://modsquad.com/careers",
            "source": "ModSquad"
        },
        {
            "title": "AI Training Specialist",
            "company": "Scale AI",
            "location": "Remote - Global",
            "salary": "$20-30/hour",
            "url": "https://scale.com/careers",
            "source": "Scale AI"
        }
    ]
    
    # Show the notification flow
    print("1️⃣ INITIAL SUMMARY MESSAGE:")
    summary_msg = f"🤖 *Agent-21 Scout Daily Report*\n"
    summary_msg += f"📅 2025-09-06 06:00 UTC\n"
    summary_msg += f"📊 Found 290 new job opportunities\n"
    summary_msg += f"🚀 Sending individual job notifications...\n\n"
    summary_msg += f"💡 Each job includes company details and direct application link"
    
    mock_send_telegram_message(summary_msg)
    
    print("2️⃣ INDIVIDUAL JOB NOTIFICATIONS:")
    print("(You'll receive 25 individual messages like these)")
    print()
    
    for i, job in enumerate(sample_jobs, 1):
        print(f"Job Notification #{i}:")
        job_msg = scout.format_individual_job(job)
        mock_send_telegram_message(job_msg)
    
    print("3️⃣ COMPLETION MESSAGE:")
    completion_msg = f"✅ *Job Notifications Complete*\n\n"
    completion_msg += f"📤 Sent 25 individual job notifications\n"
    completion_msg += f"📋 265 additional jobs available\n"
    completion_msg += f"🔄 Next scan: Tomorrow 6:00 AM\n"
    completion_msg += f"🎯 Good luck with your applications!"
    
    mock_send_telegram_message(completion_msg)
    
    print("🎉 SUMMARY OF CHANGES:")
    print("=" * 40)
    print("✅ Jobs now come as individual messages")
    print("✅ Each message focuses on company and job details")
    print("✅ Direct application links for every job")
    print("✅ No more categorized summaries")
    print("✅ 25 individual job notifications daily")
    print("✅ Company name prominently displayed")
    print("✅ Clean, focused format for each job")
    print()
    print("📱 You'll receive these notifications at 6:00 AM daily!")

def main():
    """Main preview function"""
    preview_notifications()

if __name__ == "__main__":
    main()