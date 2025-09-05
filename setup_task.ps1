# Agent-21 Scout - Setup Scheduled Task
Write-Host "Setting up Agent-21 Scout scheduled task..." -ForegroundColor Green

$currentDir = Get-Location
Write-Host "Working directory: $currentDir" -ForegroundColor Cyan

# Remove old tasks
try {
    Unregister-ScheduledTask -TaskName "AI Job Scout" -Confirm:$false -ErrorAction SilentlyContinue
    Unregister-ScheduledTask -TaskName "Argentic AI job scout" -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "Old tasks removed" -ForegroundColor Yellow
} catch {
    Write-Host "No old tasks to remove" -ForegroundColor Yellow
}

# Create new task
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "telegram_jobs.py" -WorkingDirectory $currentDir
$trigger = New-ScheduledTaskTrigger -Daily -At "06:00"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive

try {
    Register-ScheduledTask -TaskName "Agent-21 Scout" -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Daily job scouting bot"
    Write-Host "✅ Task created successfully!" -ForegroundColor Green
    Write-Host "📅 Will run daily at 6:00 AM" -ForegroundColor Cyan
    
    # Test the task
    Start-ScheduledTask -TaskName "Agent-21 Scout"
    Write-Host "✅ Task test started" -ForegroundColor Green
    
} catch {
    Write-Host "❌ Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "💡 Try running as Administrator" -ForegroundColor Yellow
}