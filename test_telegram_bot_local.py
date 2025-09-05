#!/usr/bin/env python3
"""
Local Test for Telegram Job Bot - Shows output without sending to Telegram
"""

import sys
import os
from datetime import datetime

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

def mock_send_job_summary(total_jobs, sources):
    print(f"📊 Job Summary: {total_jobs} jobs from {len(sources)} sources")

# Replace the telegram functions
import telegram_bot
telegram_bot.send_telegram_message = mock_send_telegram_message
telegram_bot.send_job_summary = mock_send_job_summary

# Import after mocking
from telegram_jobs import JobScout

def test_local_bot():
    """Test the bot locally without sending to Telegram"""
    print("🧪 Testing Telegram Job Bot Locally")
    print("=" * 50)
    print(f"Started at: {datetime.now()}")
    print()
    
    # Create a JobScout instance
    scout = JobScout()
    
    # Add some sample jobs to test categorization
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
            "title": "Search Quality Evaluator",
            "company": "TELUS International",
            "location": "Remote - Worldwide",
            "url": "https://telusinternational.com/careers",
            "source": "TELUS International",
            "salary": "$18/hour"
        },
        {
            "title": "Microtask Worker",
            "company": "Amazon MTurk",
            "location": "Remote - Flexible",
            "url": "https://mturk.com",
            "source": "Amazon MTurk",
            "salary": "$8-15/hour"
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
    
    # Add sample jobs to the scout
    scout.jobs_found = sample_jobs
    scout.total_jobs = len(sample_jobs)
    
    # Test the organized categorization
    print("🎯 Organizing jobs by skill level and requirements...")
    organized_jobs = scout.categorizer.organize_jobs_by_category(sample_jobs)
    
    # Show the organized summary
    organized_summary = scout.categorizer.format_organized_job_summary(organized_jobs)
    mock_send_telegram_message(organized_summary)
    
    # Show source stats (mock)
    scout.source_stats = {
        "LiveWorld": {"status": "success", "jobs": 1},
        "ModSquad": {"status": "success", "jobs": 1},
        "GitLab": {"status": "success", "jobs": 1},
        "TikTok": {"status": "success", "jobs": 1},
        "Scale AI": {"status": "success", "jobs": 1},
        "TELUS International": {"status": "success", "jobs": 1},
        "Amazon MTurk": {"status": "success", "jobs": 1},
        "UserTesting": {"status": "success", "jobs": 1},
        "Failed Source": {"status": "api_error", "jobs": 0}
    }
    
    # Test source performance stats
    stats_msg = "📊 **Source Performance Report**\n\n"
    successful_sources = 0
    failed_sources = 0
    
    for source, stats in scout.source_stats.items():
        if stats["status"] == "success" and stats["jobs"] > 0:
            stats_msg += f"✅ {source}: {stats['jobs']} jobs\n"
            successful_sources += 1
        elif stats["status"] in ["api_error", "error"]:
            stats_msg += f"❌ {source}: Failed\n"
            failed_sources += 1
    
    stats_msg += f"\n📈 Active Sources: {successful_sources}\n"
    stats_msg += f"⚠️ Failed Sources: {failed_sources}\n"
    
    total_sources = successful_sources + failed_sources
    if total_sources > 0:
        stats_msg += f"🎯 Success Rate: {(successful_sources/total_sources*100):.1f}%"
    else:
        stats_msg += f"🎯 Success Rate: N/A"
    
    mock_send_telegram_message(stats_msg)
    
    # Show jobs by category
    print("\n📋 Jobs by Category:")
    print("-" * 30)
    
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
                print(f"  💼 {category.replace('_', ' ').title()}:")
                for job in category_jobs:
                    print(f"    • {job['title']} - {job['company']} ({job['salary']})")
    
    print(f"\n✅ Local Test Complete!")
    print(f"Total Jobs Processed: {len(sample_jobs)}")
    print(f"Categories Used: {len(set(job['categorization']['category'] for job in sample_jobs if 'categorization' in job))}")

if __name__ == "__main__":
    test_local_bot()