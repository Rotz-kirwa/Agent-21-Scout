#!/usr/bin/env python3
"""
Daily Job Scheduler - Ensures reliable 6 AM job notifications
This script provides multiple layers of reliability for daily job notifications
"""

import os
import sys
import time
import schedule
import threading
from datetime import datetime, timedelta
import subprocess
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log'),
        logging.StreamHandler()
    ]
)

class ReliableJobScheduler:
    def __init__(self):
        self.script_dir = Path(__file__).parent.absolute()
        self.job_script = self.script_dir / "telegram_jobs.py"
        self.last_run_file = self.script_dir / "last_run.txt"
        self.running = True
        
    def run_job_bot(self):
        """Run the job bot with error handling and logging"""
        try:
            logging.info("🚀 Starting daily job notification...")
            
            # Change to script directory
            os.chdir(self.script_dir)
            
            # Run the job bot
            result = subprocess.run([
                sys.executable, str(self.job_script)
            ], capture_output=True, text=True, timeout=600)  # 10 minute timeout
            
            if result.returncode == 0:
                logging.info("✅ Job bot completed successfully")
                logging.info(f"Output: {result.stdout}")
                
                # Record successful run
                with open(self.last_run_file, 'w') as f:
                    f.write(datetime.now().isoformat())
                    
            else:
                logging.error(f"❌ Job bot failed with return code {result.returncode}")
                logging.error(f"Error: {result.stderr}")
                
                # Try fallback notification
                self.send_fallback_notification()
                
        except subprocess.TimeoutExpired:
            logging.error("⏰ Job bot timed out after 10 minutes")
            self.send_fallback_notification()
            
        except Exception as e:
            logging.error(f"💥 Unexpected error running job bot: {e}")
            self.send_fallback_notification()
    
    def send_fallback_notification(self):
        """Send a fallback notification if main bot fails"""
        try:
            from telegram_bot import send_telegram_message
            send_telegram_message(
                "⚠️ Job Bot Alert: There was an issue with today's job notification. "
                "Please check the logs and run the bot manually if needed."
            )
            logging.info("📱 Fallback notification sent")
        except Exception as e:
            logging.error(f"Failed to send fallback notification: {e}")
    
    def check_missed_runs(self):
        """Check if we missed any scheduled runs and catch up"""
        try:
            if not self.last_run_file.exists():
                logging.info("No previous run record found")
                return
                
            with open(self.last_run_file, 'r') as f:
                last_run_str = f.read().strip()
                
            last_run = datetime.fromisoformat(last_run_str)
            now = datetime.now()
            
            # If last run was more than 25 hours ago, we missed a day
            if (now - last_run).total_seconds() > 25 * 3600:
                logging.warning("⚠️ Missed scheduled run detected, running now...")
                self.run_job_bot()
                
        except Exception as e:
            logging.error(f"Error checking missed runs: {e}")
    
    def start_scheduler(self):
        """Start the reliable scheduler"""
        logging.info("🕕 Starting reliable job scheduler for 6:00 AM daily")
        
        # Schedule the main job at 6:00 AM
        schedule.every().day.at("06:00").do(self.run_job_bot)
        
        # Add backup schedules in case main one fails
        schedule.every().day.at("06:05").do(self.check_missed_runs)
        schedule.every().day.at("06:15").do(self.check_missed_runs)
        
        # Check for missed runs on startup
        self.check_missed_runs()
        
        # Run scheduler loop
        while self.running:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
            except KeyboardInterrupt:
                logging.info("🛑 Scheduler stopped by user")
                self.running = False
                break
                
            except Exception as e:
                logging.error(f"Scheduler error: {e}")
                time.sleep(60)  # Continue running even if there's an error

def main():
    """Main function to start the scheduler"""
    scheduler = ReliableJobScheduler()
    
    # Check if job script exists
    if not scheduler.job_script.exists():
        logging.error(f"❌ Job script not found: {scheduler.job_script}")
        sys.exit(1)
    
    logging.info("🤖 Agent-21 Scout Reliable Scheduler Starting...")
    logging.info(f"📁 Working directory: {scheduler.script_dir}")
    logging.info(f"🎯 Target script: {scheduler.job_script}")
    logging.info("⏰ Scheduled for 6:00 AM daily")
    
    try:
        scheduler.start_scheduler()
    except Exception as e:
        logging.error(f"💥 Fatal scheduler error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()