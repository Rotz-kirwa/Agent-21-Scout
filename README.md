# 🤖 Agent-21 Scout - Advanced Telegram Job Bot & Payment System

Agent-21 Scout is an intelligent Telegram bot that automatically scouts and delivers job opportunities from 15+ global platforms, with integrated M-Pesa payment system for premium subscriptions.

## 🚀 Features

### Job Scouting System:
- **15+ Job Sources**: Remotive, WeWorkRemotely, RemoteOK, Wellfound, NoWhiteboard, WorkingNomads, Toptal, Upwork, Arc.dev
- **Kenya-Friendly Focus**: Worldwide remote jobs accessible from Kenya
- **17 Job Categories**: Tech, IT Support, Virtual Assistant, Content Writing, Finance, AI Training, BPO, and more
- **Smart Filtering**: Recent jobs (last 7 days) with salary ranges $15-120/hour
- **Professional Formatting**: Clean Markdown with emojis and direct application links
- **Daily Automation**: Runs at 6:00 AM with 15-30 curated opportunities

### Payment & Monetization System:
- **M-Pesa Integration**: Automatic payment verification via SMS forwarding
- **Phone-Based Matching**: Users register M-Pesa number, bot matches payments automatically
- **Premium Group Access**: Instant invite links after payment confirmation
- **Subscription Model**: Ksh 50/month for exclusive job alerts
- **Revenue Tracking**: Complete payment logs and user management

## 📋 Prerequisites

### For Job Scouting:
- Python 3.7+
- Telegram Bot Token
- Your Telegram Chat ID

### For Payment System:
- M-Pesa account (Kenya)
- Android phone with SMS forwarder app
- Premium Telegram group
- Payment bot token (separate from job bot)

## 🛠️ Installation

### Job Scouting Setup:
1. **Clone and navigate:**
   ```bash
   cd telegram-automation
   source venv/bin/activate  # Activate virtual environment
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure job bot:**
   ```bash
   # Update .env file
   TELEGRAM_BOT_TOKEN=your_job_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

### Payment System Setup:
1. **Configure payment bot:**
   ```bash
   python setup_test_env.py  # Interactive setup
   ```

2. **Start payment system:**
   ```bash
   python start_payment_bot.py
   ```

3. **Test locally:**
   ```bash
   python test_local_payment.py
   ```

## 🎯 Usage

### Job Scouting:
```bash
# Manual job scout
python telegram_jobs.py

# Test bot connection
python test_agent21.py

# Set up daily automation
chmod +x setup_cron.sh
./setup_cron.sh
```

### Payment System:
```bash
# Start payment bot
python start_payment_bot.py

# Test payment flow
python test_local_payment.py

# Deploy to production (Render.com)
# See render_setup.md for deployment guide
```

### User Experience:
1. User: `/join` → Registers M-Pesa number
2. User pays Ksh 50 to your M-Pesa
3. SMS forwarded → Bot matches payment → Sends group invite
4. User gets daily job alerts at 6 AM

## 📁 File Structure

```
telegram-automation/
├── Job Scouting System:
│   ├── telegram_bot.py          # Core messaging functionality
│   ├── telegram_jobs.py         # Job scouting from 15+ sources
│   ├── kenya_jobs.py           # Kenya-friendly job sources
│   ├── test_agent21.py         # Comprehensive bot testing
│   └── quick_test.py           # Quick functionality test
│
├── Payment System:
│   ├── start_payment_bot.py    # M-Pesa payment bot
│   ├── setup_test_env.py       # Interactive payment setup
│   ├── test_local_payment.py   # Local payment testing
│   ├── render_deploy.py        # Production deployment
│   └── .env.payment           # Payment bot configuration
│
├── Utilities:
│   ├── get_chat_id.py          # Get Telegram Chat ID
│   ├── setup_cron.sh           # Daily automation setup
│   ├── requirements.txt        # Dependencies
│   └── DEPLOYMENT_GUIDE.md     # Complete setup guide
```

## 🔧 Configuration

### Job Categories (17 Categories):
```python
CATEGORIES = {
    "software-dev": ["developer", "programming", "software"],
    "python": ["python", "django", "flask", "backend"],
    "javascript": ["javascript", "react", "vue", "angular"],
    "mobile": ["mobile", "android", "ios", "react-native"],
    "data": ["data", "analytics", "machine-learning", "ai"],
    "it-support": ["technical-support", "helpdesk", "systems-admin"],
    "virtual-assistant": ["virtual-assistant", "executive-assistant"],
    "content-writing": ["content-writer", "copywriter", "writing"],
    "customer-support": ["customer-support", "community-manager"],
    "finance": ["finance-analyst", "accountant", "bookkeeper"],
    "ai-training": ["data-annotation", "ai-training", "rater"]
    # + 6 more categories
}
```

### Payment Configuration:
```bash
# .env.payment
PAYMENT_BOT_TOKEN=your_payment_bot_token
GROUP_INVITE_LINK=https://t.me/+your_premium_group
MPESA_NUMBER=0791260817
PAYMENT_AMOUNT=50
ADMIN_CHAT_ID=your_telegram_id  # Optional notifications
```

## 🔍 Job Sources (15+ Platforms)

### **Primary Remote Job Boards:**
1. **Remotive** - Global remote job marketplace
2. **WeWorkRemotely** - Remote-first companies
3. **RemoteOK** - Digital nomad jobs
4. **Wellfound (AngelList)** - Startup opportunities
5. **NoWhiteboard.org** - Tech jobs without coding tests
6. **WorkingNomads** - Location-independent work

### **Kenya-Friendly Freelance Platforms:**
7. **Toptal** - Elite freelance network ($30-80/hour)
8. **Upwork** - Global freelancing ($15-60/hour)
9. **Arc.dev** - Developer network ($40-120/hour)
10. **Freelancer.com** - Various skills ($20-50/hour)
11. **Guru.com** - Professional services ($25-70/hour)

### **Specialized Sources:**
12. **SupportNinja** - Customer support roles
13. **Fancy Hands** - Virtual assistant work
14. **Scripted** - Content writing ($15-40/hour)
15. **Contently** - Professional writing ($20-80/hour)

## 📊 Output Format

### Daily Job Alert Format:
```
🤖 Agent-21 Scout Daily Report

📊 Found 27 new opportunities
🔍 Sources: Remotive, WeWorkRemotely, Toptal, Upwork
⏰ 2025-08-23 06:00 UTC

💼 Remote Python Developer
🏢 Global Tech Co
🌍 Remote - Worldwide
💰 $40-80k/year
🔗 Apply Here
🔍 Source: WeWorkRemotely
```

### Job Categories Covered:
- 🖥️ **Tech & Development** (Python, JavaScript, Mobile, Data)
- 🛠️ **IT & Support** (Technical Support, Helpdesk, Systems Admin)
- 📝 **Content & Writing** (Copywriting, Technical Writing, Courses)
- 👩💼 **Business & Admin** (Virtual Assistant, Project Manager, HR)
- 💰 **Finance & Operations** (Analyst, Accountant, Operations)
- 🎯 **Specialized Remote** (AI Training, Content Moderation, BPO)

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

## 💰 Business Model & Revenue

### Subscription Pricing:
- **Premium Access**: Ksh 50/month
- **Target Market**: Remote workers in Kenya
- **Value Proposition**: 15-30 curated global opportunities daily

### Revenue Projections:
- 100 subscribers = Ksh 5,000/month
- 500 subscribers = Ksh 25,000/month  
- 1,000 subscribers = Ksh 50,000/month

### Success Metrics:
- **Job Volume**: 15-30 jobs per day
- **Job Sources**: 15+ platforms
- **Categories**: 17 job types
- **Freshness**: Last 7 days only
- **Accessibility**: Kenya-friendly remote positions
- **Salary Range**: $15-120/hour or $25k-100k/year

## 🚀 Deployment Options

### Local Testing:
```bash
python start_payment_bot.py  # Local testing
python test_local_payment.py  # Simulate payments
```

### Production Deployment:
1. **Render.com** (Recommended - Free tier)
2. **AWS Lambda** (Serverless)
3. **VPS/Cloud Server**

### SMS Forwarder Setup:
- Install SMS forwarder app on Android
- Forward M-Pesa SMS to webhook: `/sms`
- Automatic payment verification

---

**Agent-21 Scout** - Your automated job hunting & monetization system! 🎯💰
