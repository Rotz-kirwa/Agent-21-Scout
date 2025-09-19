@echo off
REM Agent-21 Scout Daily Job Runner for Windows
echo Starting Agent-21 Scout at %date% %time%

REM Run the job scout in WSL
wsl -d Ubuntu-24.04 -e bash -c "cd /home/risinglion/telegram-automation && source venv/bin/activate && python quick_daily_jobs.py"

echo Agent-21 Scout completed at %date% %time%