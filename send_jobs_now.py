#!/usr/bin/env python3
"""
Manual job sender - run this anytime to get your daily jobs
"""

from quick_daily_jobs import send_daily_jobs

if __name__ == "__main__":
    print("🚀 Sending your daily job notifications...")
    send_daily_jobs()
    print("✅ Done! Check your Telegram for job notifications.")