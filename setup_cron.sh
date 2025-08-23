#!/bin/bash
# Agent-21 Scout - Cron Setup Script
# This script sets up daily job scouting at 6:00 AM

echo "🤖 Setting up Agent-21 Scout cron job..."

# Get the current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_PATH=$(which python3)

# Create the cron job entry
CRON_JOB="0 6 * * * cd $SCRIPT_DIR && $PYTHON_PATH telegram_jobs.py >> $SCRIPT_DIR/scout.log 2>&1"

# Add to crontab
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "✅ Agent-21 Scout scheduled to run daily at 6:00 AM"
echo "📁 Logs will be saved to: $SCRIPT_DIR/scout.log"
echo ""
echo "To check if cron job was added:"
echo "crontab -l"
echo ""
echo "To remove the cron job:"
echo "crontab -e"
echo ""
echo "To test the bot manually:"
echo "cd $SCRIPT_DIR && python3 telegram_jobs.py"