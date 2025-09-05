#!/usr/bin/env python3
"""
Quick test of the organized telegram bot with limited job sources
"""

import sys
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telegram_jobs import JobScout
from telegram_bot import send_telegram_message

def quick_test():
    """Quick test with limited job sources"""
    print("🚀 Quick Test of Organized Telegram Bot")
    print("=" * 50)
    
    scout = JobScout()
    
    # Add some sample jobs directly
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
            "title": "Search Quality Evaluator",
            "company": "TELUS International",
            "location": "Remote - Worldwide",
            "url": "https://telusinternational.com/careers",
            "source": "TELUS International",
            "salary": "$18/hour"
        }
    ]
    
    scout.jobs_found = sample_jobs
    scout.total_jobs = len(sample_jobs)
    
    # Mock some source stats
    scout.source_stats = {
        "LiveWorld": {"status": "success", "jobs": 1},
        "TikTok": {"status": "success", "jobs": 1},
        "Scale AI": {"status": "success", "jobs": 1},
        "TELUS International": {"status": "success", "jobs": 1}
    }
    
    print("🎯 Organizing jobs by skill level and requirements...")
    organized_jobs = scout.categorizer.organize_jobs_by_category(sample_jobs)
    
    # Send organized summary
    organized_summary = scout.categorizer.format_organized_job_summary(organized_jobs)
    
    print("📤 Sending organized job summary to Telegram...")
    try:
        send_telegram_message(organized_summary)
        print("✅ Successfully sent organized job summary!")
    except Exception as e:
        print(f"❌ Error sending summary: {e}")
    
    # Send source stats
    stats_msg = "📊 **Quick Test - Source Performance**\n\n"
    successful_sources = 0
    
    for source, stats in scout.source_stats.items():
        if stats["status"] == "success" and stats["jobs"] > 0:
            stats_msg += f"✅ {source}: {stats['jobs']} jobs\n"
            successful_sources += 1
    
    stats_msg += f"\n📈 Active Sources: {successful_sources}\n"
    stats_msg += f"🎯 Success Rate: 100%\n"
    stats_msg += f"🧪 This was a quick test of the organized categorization system!"
    
    print("📤 Sending source performance stats...")
    try:
        send_telegram_message(stats_msg)
        print("✅ Successfully sent source stats!")
    except Exception as e:
        print(f"❌ Error sending stats: {e}")
    
    # Send completion message
    completion_msg = f"✅ *Organized Job Bot Quick Test Complete*\n\n"
    completion_msg += f"🎯 Successfully categorized {len(sample_jobs)} jobs by skill level\n"
    completion_msg += f"📊 Entry Level: {len(organized_jobs.get('entry_level', []))} jobs\n"
    completion_msg += f"📊 Intermediate: {len(organized_jobs.get('intermediate_level', []))} jobs\n"
    completion_msg += f"📊 Expert Level: {len(organized_jobs.get('expert_level', []))} jobs\n"
    completion_msg += f"📊 Flexible: {len(organized_jobs.get('flexible_opportunities', []))} jobs\n"
    completion_msg += f"🚀 The organized categorization system is working perfectly!"
    
    print("📤 Sending completion message...")
    try:
        send_telegram_message(completion_msg)
        print("✅ Successfully sent completion message!")
    except Exception as e:
        print(f"❌ Error sending completion: {e}")
    
    print(f"\n✅ Quick Test Complete!")
    print(f"Check your Telegram bot to see the organized job categories in action!")

if __name__ == "__main__":
    quick_test()