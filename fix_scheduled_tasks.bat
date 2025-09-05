@echo off
echo Fixing Agent-21 Scout Scheduled Tasks...
echo.

REM Get current directory
set CURRENT_DIR=%~dp0

REM Delete existing broken tasks
echo Removing broken scheduled tasks...
schtasks /delete /tn "AI Job Scout" /f >nul 2>&1
schtasks /delete /tn "Argentic AI job scout" /f >nul 2>&1

REM Create new working task
echo Creating new Agent-21 Scout task...
schtasks /create /tn "Agent-21 Scout" /tr "python.exe telegram_jobs.py" /sc daily /st 06:00 /sd %date% /ru SYSTEM /f /rl HIGHEST /it /np

REM Set working directory for the task
echo Setting working directory...
schtasks /change /tn "Agent-21 Scout" /tr "cmd /c cd /d \"%CURRENT_DIR%\" && python telegram_jobs.py >> scout.log 2>&1"

echo.
echo ✅ Agent-21 Scout scheduled task created successfully!
echo 📅 Will run daily at 6:00 AM
echo 📁 Working directory: %CURRENT_DIR%
echo 📝 Logs will be saved to scout.log
echo.
echo To test the task manually, run:
echo schtasks /run /tn "Agent-21 Scout"
echo.
pause