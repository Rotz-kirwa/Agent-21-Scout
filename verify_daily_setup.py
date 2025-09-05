#!/usr/bin/env python3
"""
Verify Daily Setup - Final verification that daily job notifications are ready
"""

import os
import sys
import platform
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

def check_scheduled_task():
    """Check if the scheduled task is properly set up"""
    system = platform.system()
    
    if system == "Windows":
        try:
            result = subprocess.run([
                'schtasks', '/query', '/tn', 'Agent-21-Scout-Reliable'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("[SUCCESS] Windows scheduled task is active")
                # Extract next run time
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'Agent-21-Scout-Reliable' in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            next_run = ' '.join(parts[1:3])
                            print(f"[TIME] Next run: {next_run}")
                return True
            else:
                print("[ERROR] Windows scheduled task not found")
                return False
                
        except Exception as e:
            print(f"[ERROR] Could not check Windows task: {e}")
            return False
    
    elif system == "Linux":
        try:
            result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
            if result.returncode == 0 and 'daily_job_scheduler.py' in result.stdout:
                print("[SUCCESS] Linux cron job is active")
                return True
            else:
                print("[ERROR] Linux cron job not found")
                return False
        except Exception as e:
            print(f"[ERROR] Could not check Linux cron: {e}")
            return False
    
    elif system == "Darwin":  # macOS
        try:
            plist_path = Path.home() / "Library/LaunchAgents/com.agent21.scout.plist"
            if plist_path.exists():
                print("[SUCCESS] macOS launch agent is active")
                return True
            else:
                print("[ERROR] macOS launch agent not found")
                return False
        except Exception as e:
            print(f"[ERROR] Could not check macOS launch agent: {e}")
            return False
    
    else:
        print(f"[WARNING] Unknown platform: {system}")
        return False

def check_required_files():
    """Check if all required files exist"""
    required_files = [
        "telegram_jobs.py",
        "telegram_bot.py", 
        "daily_job_scheduler.py",
        ".env"
    ]
    
    all_present = True
    for file in required_files:
        if Path(file).exists():
            print(f"[SUCCESS] {file} found")
        else:
            print(f"[ERROR] {file} missing")
            all_present = False
    
    return all_present

def check_environment():
    """Check environment variables and dependencies"""
    try:
        # Check if .env file has required variables
        env_path = Path(".env")
        if env_path.exists():
            with open(env_path, 'r') as f:
                env_content = f.read()
                
            if 'TELEGRAM_BOT_TOKEN' in env_content and 'TELEGRAM_CHAT_ID' in env_content:
                print("[SUCCESS] Telegram configuration found")
            else:
                print("[WARNING] Telegram configuration may be incomplete")
                return False
        
        # Check dependencies
        import requests
        import schedule
        print("[SUCCESS] All dependencies available")
        return True
        
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Environment check failed: {e}")
        return False

def calculate_next_run():
    """Calculate when the next job notification will be sent"""
    now = datetime.now()
    
    # Next 6 AM
    next_6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
    if now.hour >= 6:
        next_6am += timedelta(days=1)
    
    time_until = next_6am - now
    hours = int(time_until.total_seconds() // 3600)
    minutes = int((time_until.total_seconds() % 3600) // 60)
    
    return next_6am, hours, minutes

def main():
    """Main verification function"""
    print("Daily Job Notification Setup Verification")
    print("=" * 50)
    print(f"[TIME] Current time: {datetime.now()}")
    print(f"[FOLDER] Working directory: {Path.cwd()}")
    
    # Run all checks
    checks = [
        ("Required Files", check_required_files),
        ("Environment Setup", check_environment),
        ("Scheduled Task", check_scheduled_task)
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n[RUNNING] Checking {check_name}...")
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"[ERROR] {check_name} check failed: {e}")
            results.append((check_name, False))
    
    # Calculate next run time
    next_run, hours, minutes = calculate_next_run()
    
    # Summary
    print("\n" + "=" * 50)
    print("VERIFICATION SUMMARY")
    print("=" * 50)
    
    passed = 0
    for check_name, result in results:
        status = "[SUCCESS] PASS" if result else "[ERROR] FAIL"
        print(f"{status} - {check_name}")
        if result:
            passed += 1
    
    print(f"\n[STATS] Checks passed: {passed}/{len(results)}")
    
    if passed == len(results):
        print("\n[COMPLETE] ALL SYSTEMS READY!")
        print("[SUCCESS] Your daily job notifications are fully configured")
        print(f"[TIME] Next notification: {next_run.strftime('%Y-%m-%d at 6:00 AM')}")
        print(f"[TIME] Time until next run: {hours}h {minutes}m")
        print("\n[TARGET] What to expect:")
        print("• Job bot will run automatically at 6:00 AM daily")
        print("• You'll receive a Telegram message with job listings")
        print("• All jobs will have clickable links")
        print("• The system includes backup checks for reliability")
        
        # Show manual test command
        print(f"\n[TIP] To test manually anytime:")
        print("python telegram_jobs.py")
        
    else:
        print("\n[WARNING] SETUP INCOMPLETE!")
        print("[ERROR] Some checks failed. Please fix the issues above.")
        print("[TIP] You may need to:")
        print("• Run setup_reliable_scheduler.py again")
        print("• Check your .env file configuration")
        print("• Install missing dependencies")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)