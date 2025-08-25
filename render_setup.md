# 🌐 Render.com Deployment Guide

## 1. Prepare for Deployment

```bash
# Install dependencies
pip install -r payment_requirements.txt

# Run setup
python quick_setup.py

# Test locally (optional)
python render_deploy.py
```

## 2. Push to GitHub

```bash
# Initialize git (if not done)
git init
git add .
git commit -m "Agent-21 Payment Bot"

# Push to GitHub
git remote add origin https://github.com/yourusername/agent21-payment-bot.git
git push -u origin main
```

## 3. Deploy on Render.com

### Create Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Connect your repository

### Create Web Service
1. Click "New" → "Web Service"
2. Connect your GitHub repo
3. Configure:
   - **Name:** `agent21-payment-bot`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r payment_requirements.txt`
   - **Start Command:** `python render_deploy.py`

### Add Environment Variables
In Render dashboard, add these environment variables:

```
PAYMENT_BOT_TOKEN=your_actual_bot_token
GROUP_INVITE_LINK=https://t.me/+your_group_link
MPESA_PHONE=0791260817
PAYMENT_AMOUNT=50
PORT=10000
```

### Deploy
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Get your webhook URL: `https://your-app-name.onrender.com`

## 4. Configure SMS Forwarder

Use your Render URL in the SMS forwarder app:
- **Webhook URL:** `https://your-app-name.onrender.com/webhook/sms`

## 5. Test the System

```bash
# Test webhook
curl -X POST https://your-app-name.onrender.com/webhook/test

# Test payment processing
curl -X POST https://your-app-name.onrender.com/webhook/sms \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456",
    "sender": "MPESA"
  }'
```

## 6. Monitor

- **Logs:** Render dashboard → Logs tab
- **Health:** `https://your-app-name.onrender.com/health`
- **Database:** SQLite file persists on Render

## 🎯 You're Live!

Your payment bot is now running 24/7 and ready to:
1. Accept `/join` commands
2. Process M-Pesa payments
3. Send automatic group invites
4. Track all transactions

**Revenue starts flowing!** 💰