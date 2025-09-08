#!/usr/bin/env python3
"""
Send jobs immediately to test notifications
"""

from telegram_jobs import JobScout
from telegram_bot import send_telegram_message
from datetime import datetime

def send_jobs_now():
    print("🚀 Sending jobs immediately...")
    
    # Get guaranteed jobs (always work)
    scout = JobScout()
    guaranteed_jobs = scout.get_guaranteed_working_jobs()
    
    # Send summary first
    summary_msg = f"🤖 **Agent-21 Scout - Manual Test**\n\n"
    summary_msg += f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}\n"
    summary_msg += f"📊 Sending {len(guaranteed_jobs)} job opportunities\n"
    summary_msg += f"🎯 Testing notification system...\n\n"
    summary_msg += f"🚀 Individual jobs coming next..."
    
    send_telegram_message(summary_msg)
    print("✅ Summary sent")
    
    # Send first 5 jobs individually
    for i, job in enumerate(guaranteed_jobs[:5], 1):
        job_msg = f"🏢 **{job['company']}**\n"
        job_msg += f"💼 *{job['title']}*\n\n"
        job_msg += f"📍 **Location:** {job['location']}\n"
        job_msg += f"💰 **Salary:** {job['salary']}\n"
        job_msg += f"🔗 **Apply:** [Click Here]({job['url']})\n"
        job_msg += f"📊 **Source:** {job['source']}\n\n"
        job_msg += f"🚀 *Job {i}/5 - Manual Test*"
        
        send_telegram_message(job_msg)
        print(f"✅ Job {i} sent: {job['title']}")
    
    # Send completion message
    completion_msg = f"✅ **Manual Test Complete**\n\n"
    completion_msg += f"📤 Sent 5 sample job notifications\n"
    completion_msg += f"🔧 If you received these, your bot is working!\n"
    completion_msg += f"💡 Daily notifications should arrive at 6:00 AM\n\n"
    completion_msg += f"🎯 **Next Steps:**\n"
    completion_msg += f"• Check if you received all messages above\n"
    completion_msg += f"• If yes, cron job might need fixing\n"
    completion_msg += f"• If no, there's a Telegram issue"
    
    send_telegram_message(completion_msg)
    print("✅ Test complete!")

if __name__ == "__main__":
    send_jobs_now()