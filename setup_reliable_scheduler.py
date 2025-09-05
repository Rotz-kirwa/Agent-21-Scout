#!/usr/bin/env python3
"""
Setup Reliable Scheduler - Cross-platform setup for daily job notifications
This script sets up the most reliable scheduling method for your system
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def install_schedule_package():
    """Install the schedule package if not available"""
    try:
        import schedule
        print("[SUCCESS] Schedule package already installed")
        return True
    except ImportError:
        print("📦 Installing schedule package...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "schedule"])
            print("[SUCCESS] Schedule package installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("[ERROR] Failed to install schedule package")
            return False

def setup_windows_service():
    """Setup Windows Task Scheduler for reliable daily execution"""
    script_dir = Path(__file__).parent.absolute()
    scheduler_script = script_dir / "daily_job_scheduler.py"
    
    print("[WINDOWS] Setting up Windows Task Scheduler...")
    
    # Create a batch file to run the scheduler
    batch_content = f'''@echo off
cd /d "{script_dir}"
python "{scheduler_script}"
'''
    
    batch_file = script_dir / "run_scheduler.bat"
    with open(batch_file, 'w') as f:
        f.write(batch_content)
    
    # Create the scheduled task
    task_cmd = [
        'schtasks', '/create', '/tn', 'Agent-21-Scout-Reliable',
        '/tr', f'"{batch_file}"',
        '/sc', 'daily', '/st', '05:55',  # Start 5 minutes early
        '/f'  # Force overwrite existing task
    ]
    
    try:
        subprocess.run(task_cmd, check=True, capture_output=True)
        print("[SUCCESS] Windows scheduled task created successfully")
        print("[TIME] Scheduler will start at 5:55 AM daily")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to create Windows task: {e}")
        return False

def setup_linux_cron():
    """Setup Linux cron job for reliable daily execution"""
    script_dir = Path(__file__).parent.absolute()
    scheduler_script = script_dir / "daily_job_scheduler.py"
    python_path = sys.executable
    
    print("[LINUX] Setting up Linux cron job...")
    
    # Create cron entry
    cron_entry = f"55 5 * * * cd {script_dir} && {python_path} {scheduler_script} >> {script_dir}/scheduler.log 2>&1"
    
    try:
        # Get current crontab
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_cron = result.stdout if result.returncode == 0 else ""
        
        # Remove any existing Agent-21 entries
        lines = [line for line in current_cron.split('\n') 
                if 'Agent-21' not in line and 'telegram_jobs.py' not in line and 'daily_job_scheduler.py' not in line]
        
        # Add new entry
        lines.append(cron_entry)
        new_cron = '\n'.join(line for line in lines if line.strip())
        
        # Install new crontab
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, text=True)
        process.communicate(input=new_cron)
        
        if process.returncode == 0:
            print("[SUCCESS] Linux cron job created successfully")
            print("[TIME] Scheduler will start at 5:55 AM daily")
            return True
        else:
            print("[ERROR] Failed to create cron job")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error setting up cron: {e}")
        return False

def setup_macos_launchd():
    """Setup macOS launchd for reliable daily execution"""
    script_dir = Path(__file__).parent.absolute()
    scheduler_script = script_dir / "daily_job_scheduler.py"
    python_path = sys.executable
    
    print("[MACOS] Setting up macOS launchd...")
    
    plist_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.agent21.scout</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{scheduler_script}</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{script_dir}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>5</integer>
        <key>Minute</key>
        <integer>55</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>{script_dir}/scheduler.log</string>
    <key>StandardErrorPath</key>
    <string>{script_dir}/scheduler_error.log</string>
</dict>
</plist>'''
    
    # Create plist file
    plist_path = Path.home() / "Library/LaunchAgents/com.agent21.scout.plist"
    plist_path.parent.mkdir(exist_ok=True)
    
    with open(plist_path, 'w') as f:
        f.write(plist_content)
    
    try:
        # Load the launch agent
        subprocess.run(['launchctl', 'load', str(plist_path)], check=True)
        print("[SUCCESS] macOS launch agent created successfully")
        print("[TIME] Scheduler will start at 5:55 AM daily")
        return True
    except subprocess.CalledProcessError:
        print("[ERROR] Failed to create macOS launch agent")
        return False

def create_manual_startup_script():
    """Create a manual startup script as fallback"""
    script_dir = Path(__file__).parent.absolute()
    
    if platform.system() == "Windows":
        startup_script = script_dir / "start_daily_scheduler.bat"
        content = f'''@echo off
echo Starting Agent-21 Scout Daily Scheduler...
cd /d "{script_dir}"
python daily_job_scheduler.py
pause
'''
    else:
        startup_script = script_dir / "start_daily_scheduler.sh"
        content = f'''#!/bin/bash
echo "Starting Agent-21 Scout Daily Scheduler..."
cd "{script_dir}"
python3 daily_job_scheduler.py
'''
        
    with open(startup_script, 'w') as f:
        f.write(content)
        
    if not platform.system() == "Windows":
        os.chmod(startup_script, 0o755)
    
    print(f"[MANUAL] Manual startup script created: {startup_script}")
    return startup_script

def main():
    """Main setup function"""
    print("[BOT] Agent-21 Scout Reliable Scheduler Setup")
    print("=" * 50)
    
    # Install required package
    if not install_schedule_package():
        print("[ERROR] Cannot proceed without schedule package")
        sys.exit(1)
    
    # Detect platform and setup appropriate scheduler
    system = platform.system()
    success = False
    
    if system == "Windows":
        success = setup_windows_service()
    elif system == "Linux":
        success = setup_linux_cron()
    elif system == "Darwin":  # macOS
        success = setup_macos_launchd()
    else:
        print(f"[WARNING] Unsupported platform: {system}")
    
    # Create manual fallback script
    manual_script = create_manual_startup_script()
    
    print("\n" + "=" * 50)
    if success:
        print("[SUCCESS] SETUP COMPLETE!")
        print("[TARGET] Your job notifications are now scheduled for 6:00 AM daily")
        print("[PLATFORM] You'll receive notifications automatically every day")
        print("[STATS] The system includes multiple reliability layers:")
        print("   • Main scheduler runs at 5:55 AM")
        print("   • Job bot runs at 6:00 AM")
        print("   • Backup checks at 6:05 AM and 6:15 AM")
        print("   • Fallback notifications if main bot fails")
        
    else:
        print("[WARNING] AUTOMATIC SETUP FAILED")
        print("[MANUAL] Manual setup required:")
        print(f"   Run this script manually: {manual_script}")
        print("   Or set up your system's scheduler to run:")
        print("   python daily_job_scheduler.py")
    
    print(f"\n[FOLDER] All files are in: {Path(__file__).parent.absolute()}")
    print("[LOG] Log files: scheduler.log, telegram_jobs.log")
    
    # Test the setup
    print("\n[TEST] Testing the job bot...")
    try:
        result = subprocess.run([sys.executable, "telegram_jobs.py"], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("[SUCCESS] Job bot test successful!")
        else:
            print("[WARNING] Job bot test had issues, but scheduler is set up")
    except Exception as e:
        print(f"[WARNING] Could not test job bot: {e}")
    
    print("\n[COMPLETE] Setup complete! You'll get job notifications at 6 AM daily.")

if __name__ == "__main__":
    main()