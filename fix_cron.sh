#!/bin/bash
# Fix cron job for daily notifications

echo "🔧 Fixing cron job for daily notifications..."

# Remove old cron jobs
crontab -r 2>/dev/null || true

# Add new working cron job
(crontab -l 2>/dev/null; echo "0 6 * * * cd /home/risinglion/telegram-automation && /home/risinglion/telegram-automation/venv/bin/python /home/risinglion/telegram-automation/telegram_jobs.py >> /home/risinglion/telegram-automation/daily_jobs.log 2>&1") | crontab -

echo "✅ Cron job fixed!"
echo "📅 Daily notifications will now run at 6:00 AM"
echo "📋 Logs will be saved to: /home/risinglion/telegram-automation/daily_jobs.log"

# Test cron service
if systemctl is-active --quiet cron; then
    echo "✅ Cron service is running"
else
    echo "⚠️ Starting cron service..."
    sudo systemctl start cron
    sudo systemctl enable cron
fi

echo "🎉 Setup complete! You'll receive daily notifications at 6:00 AM"