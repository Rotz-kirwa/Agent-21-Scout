#!/usr/bin/env python3
"""
Test Individual Job Notifications - Test the new individual job notification system
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock the telegram functions to avoid sending actual messages during testing
def mock_send_telegram_message(message):
    print("=" * 60)
    print("TELEGRAM MESSAGE:")
    print("=" * 60)
    print(message)
    print("=" * 60)
    print()

import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message

from telegram_jobs import JobScout

def test_individual_notifications():
    """Test the individual job notification system"""
    print("🧪 Testing Individual Job Notification System")
    print("=" * 60)
    
    scout = JobScout()
    
    # Test the individual job formatting
    sample_job = {
        "title": "Remote Customer Support Specialist",
        "company": "TechCorp Inc.",
        "location": "Remote - Worldwide",
        "salary": "$18-25/hour",
        "url": "https://example.com/apply",
        "source": "RemoteOK"
    }
    
    print("📝 Testing individual job formatting...")
    formatted_job = scout.format_individual_job(sample_job)
    print("Individual Job Format:")
    print("-" * 40)
    print(formatted_job)
    print("-" * 40)
    
    # Test with a few sample jobs to see the flow
    print("\n🚀 Testing notification flow with sample jobs...")
    
    # Create some sample jobs
    sample_jobs = [
        {
            "title": "Python Developer",
            "company": "GitLab",
            "location": "Remote - Global",
            "salary": "$70-90k/year",
            "url": "https://about.gitlab.com/jobs/",
            "source": "GitLab Careers"
        },
        {
            "title": "Virtual Assistant",
            "company": "Belay Solutions",
            "location": "Remote - US",
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
        }
    ]
    
    # Simulate the notification flow
    print("Simulating notification flow:")
    print()
    
    # Initial summary
    summary_msg = f"🤖 *Agent-21 Scout Daily Report*\n"
    summary_msg += f"📅 2025-09-06 06:00 UTC\n"
    summary_msg += f"📊 Found {len(sample_jobs)} new job opportunities\n"
    summary_msg += f"🚀 Sending individual job notifications...\n\n"
    summary_msg += f"💡 Each job includes company details and direct application link"
    
    mock_send_telegram_message(summary_msg)
    
    # Individual jobs
    for i, job in enumerate(sample_jobs, 1):
        print(f"Sending job {i}/{len(sample_jobs)}...")
        job_msg = scout.format_individual_job(job)
        mock_send_telegram_message(job_msg)
    
    # Completion message
    completion_msg = f"✅ *Job Notifications Complete*\n\n"
    completion_msg += f"📤 Sent {len(sample_jobs)} individual job notifications\n"
    completion_msg += f"🔄 Next scan: Tomorrow 6:00 AM\n"
    completion_msg += f"🎯 Good luck with your applications!"
    
    mock_send_telegram_message(completion_msg)
    
    print("✅ Individual notification test complete!")
    print(f"📊 Tested with {len(sample_jobs)} sample jobs")
    print("🎯 Each job is now sent as a separate message with company focus")

def main():
    """Main test function"""
    test_individual_notifications()

if __name__ == "__main__":
    main()