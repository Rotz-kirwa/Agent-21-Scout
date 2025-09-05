@echo off
echo Setting up Agent-21 Scout scheduled task...

REM Remove old tasks
schtasks /delete /tn "AI Job Scout" /f >nul 2>&1
schtasks /delete /tn "Argentic AI job scout" /f >nul 2>&1
echo Old tasks removed

REM Create new task
schtasks /create /tn "Agent-21 Scout" /tr "cmd /c cd /d \"%~dp0\" && python telegram_jobs.py >> scout.log 2>&1" /sc daily /st 06:00 /f
if %errorlevel% equ 0 (
    echo ✅ Task created successfully!
    echo 📅 Will run daily at 6:00 AM
    echo 📁 Working directory: %~dp0
    echo 📝 Logs will be saved to scout.log
    
    REM Test the task
    echo Testing task...
    schtasks /run /tn "Agent-21 Scout"
    echo ✅ Task test started
) else (
    echo ❌ Failed to create task
    echo 💡 Try running as Administrator
)

echo.
echo Manual test command: python telegram_jobs.py
pause