# 🤖 Agent-21 Scout - Advanced Telegram Job Bot

Agent-21 Scout is an intelligent Telegram bot that automatically scouts and delivers job opportunities from multiple platforms including Amazon, Remotive, and GitHub Jobs.

## 🚀 Features

- **Multi-Platform Integration**: Fetches jobs from Amazon Jobs API, Remotive, and GitHub Jobs
- **Smart Filtering**: Only shows recent jobs (last 7 days) to avoid outdated listings
- **Category-Based Search**: Monitors Python, AWS, JavaScript, Data Science, and Backend roles
- **Professional Formatting**: Clean Markdown formatting with emojis for easy reading
- **Rate Limiting**: Prevents API abuse and Telegram rate limits
- **Duplicate Removal**: Ensures no duplicate job postings
- **Daily Automation**: Runs automatically at 6:00 AM via cron job

## 📋 Prerequisites

- Python 3.7+
- Telegram Bot Token
- Your Telegram Chat ID

## 🛠️ Installation

1. **Clone and navigate to the project:**
   ```bash
   cd telegram-automation
   ```

2. **Install dependencies:**
   ```bash
   pip install requests python-dotenv
   ```

3. **Configure environment variables:**
   ```bash
   # Update .env file with your credentials
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```

4. **Get your Chat ID:**
   ```bash
   python get_chat_id.py
   ```

## 🎯 Usage

### Manual Testing
```bash
# Test the bot connection
python test_bot.py

# Run a manual job scout
python telegram_jobs.py
```

### Automated Daily Scouting
```bash
# Set up daily cron job at 6:00 AM
chmod +x setup_cron.sh
./setup_cron.sh
```

## 📁 File Structure

```
telegram-automation/
├── telegram_bot.py      # Core messaging functionality
├── telegram_jobs.py     # Job scouting and API integration
├── get_chat_id.py      # Utility to get Telegram Chat ID
├── test_bot.py         # Bot connection test
├── setup_cron.sh       # Automated cron job setup
├── .env               # Environment variables (create this)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## 🔧 Configuration

### Job Categories
Edit `CATEGORIES` in `telegram_jobs.py`:
```python
CATEGORIES = {
    "python": ["python", "django", "flask", "fastapi"],
    "aws": ["aws", "cloud", "devops", "kubernetes"],
    "javascript": ["javascript", "react", "node", "typescript"],
    "data": ["data-science", "machine-learning", "ai"],
    "backend": ["backend", "api", "microservices"]
}
```

### Cron Schedule
Default: Daily at 6:00 AM
```bash
# Edit cron schedule
crontab -e

# Current setting: 0 6 * * *
# Format: minute hour day month weekday
```

## 🔍 Job Sources

1. **Remotive API**: Remote job listings with detailed filtering
2. **Amazon Jobs API**: Direct integration with Amazon's job portal
3. **GitHub Jobs**: Tech-focused positions (when available)

## 📊 Output Format

Each job includes:
- 💼 Job Title
- 🏢 Company Name
- 🌍 Location (Remote/Onsite)
- 💰 Salary Information
- 🔗 Direct Application Link
- 🔍 Source Platform

## 🛡️ Error Handling

- Network timeouts and retries
- API rate limiting
- Graceful failure handling
- Comprehensive logging

## 📝 Logs

Check daily logs:
```bash
tail -f scout.log
```

## 🔒 Security

- Environment variables for sensitive data
- No hardcoded credentials
- Rate limiting to prevent abuse

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues or questions:
1. Check the logs: `tail scout.log`
2. Test manually: `python telegram_jobs.py`
3. Verify environment variables in `.env`

## 🎉 Success Metrics

Agent-21 Scout typically finds:
- 15-30 relevant jobs per day
- 3-5 different job sources
- Recent postings (within 7 days)
- Filtered by your specified categories

---

**Agent-21 Scout** - Your automated job hunting companion! 🎯# Agent-21-Scout
