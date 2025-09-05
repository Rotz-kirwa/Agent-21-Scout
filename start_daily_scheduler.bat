@echo off
echo Starting Agent-21 Scout Daily Scheduler...
cd /d "\\wsl.localhost\Ubuntu-24.04\home\risinglion\telegram-automation"
python daily_job_scheduler.py
pause
