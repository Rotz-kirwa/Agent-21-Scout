# Agent-21 Scout - Fix Scheduled Tasks (PowerShell)
Write-Host "🤖 Fixing Agent-21 Scout Scheduled Tasks..." -ForegroundColor Green

# Get current directory
$currentDir = Get-Location

# Remove existing broken tasks
Write-Host "🗑️ Removing broken scheduled tasks..." -ForegroundColor Yellow
try {
    Unregister-ScheduledTask -TaskName "AI Job Scout" -Confirm:$false -ErrorAction SilentlyContinue
    Unregister-ScheduledTask -TaskName "Argentic AI job scout" -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "✅ Old tasks removed" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Some tasks may not have existed" -ForegroundColor Yellow
}

# Create new task action
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "telegram_jobs.py" -WorkingDirectory $currentDir

# Create trigger for daily at 6:00 AM
$trigger = New-ScheduledTaskTrigger -Daily -At "06:00"

# Create task settings
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Create principal (run as current user)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive

# Register the new task
try {
    Register-ScheduledTask -TaskName "Agent-21 Scout" -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Daily job scouting bot for remote opportunities"
    Write-Host "✅ Agent-21 Scout task created successfully!" -ForegroundColor Green
    Write-Host "📅 Scheduled to run daily at 6:00 AM" -ForegroundColor Cyan
    Write-Host "📁 Working directory: $currentDir" -ForegroundColor Cyan
} catch {
    Write-Host "❌ Failed to create scheduled task: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "💡 Try running PowerShell as Administrator" -ForegroundColor Yellow
}

# Test the task
Write-Host ""
Write-Host "🧪 Testing the task..." -ForegroundColor Yellow
try {
    Start-ScheduledTask -TaskName "Agent-21 Scout"
    Write-Host "✅ Task started successfully!" -ForegroundColor Green
    Write-Host "📝 Check scout.log for output" -ForegroundColor Cyan
} catch {
    Write-Host "⚠️ Could not start task immediately, but it should run at 6:00 AM" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📋 Task Summary:" -ForegroundColor Magenta
Get-ScheduledTask -TaskName "Agent-21 Scout" | Get-ScheduledTaskInfo | Format-List

Write-Host ""
Write-Host "🔧 Manual Commands:" -ForegroundColor Blue
Write-Host "  Test manually: python telegram_jobs.py" -ForegroundColor White
Write-Host "  Run task now:  Start-ScheduledTask -TaskName 'Agent-21 Scout'" -ForegroundColor White
Write-Host "  View logs:     Get-Content scout.log -Tail 20" -ForegroundColor White

Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")