# 🚀 Agent-21 Scout Payment Bot Deployment Guide

## 📋 Overview
This system handles M-Pesa payments and automatically sends Telegram group invites for Agent-21 Scout Premium subscriptions.

## 🛠️ Setup Steps

### 1. Create Payment Bot
1. Message @BotFather on Telegram
2. Create new bot: `/newbot`
3. Name it: `Agent21 Payment Bot`
4. Username: `@Agent21PaymentBot` (or similar)
5. Copy the bot token

### 2. Create Premium Group
1. Create a Telegram group for premium subscribers
2. Add your payment bot as admin
3. Generate invite link: Group Settings → Invite Links → Create Link
4. Copy the invite link

### 3. Environment Configuration
Copy `payment_env_template.env` to `.env` and update:

```env
PAYMENT_BOT_TOKEN=your_bot_token_here
GROUP_INVITE_LINK=https://t.me/+your_group_invite_link
MPESA_PHONE=0791260817
PAYMENT_AMOUNT=50
WEBHOOK_PORT=5000
```

## 🌐 Deployment Options

### Option A: Render.com (Recommended - Free Tier)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Agent-21 Payment Bot"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Connect GitHub repository
   - Create new Web Service
   - Use `render_deploy.py` as start command: `python render_deploy.py`
   - Add environment variables from your `.env` file
   - Deploy!

3. **Get Webhook URL:**
   - Your webhook will be: `https://your-app-name.onrender.com/webhook/sms`

### Option B: AWS Lambda (Serverless)

1. **Create Lambda Function:**
   - Use `lambda_handler.py`
   - Runtime: Python 3.9+
   - Add environment variables

2. **Create API Gateway:**
   - Create REST API
   - Add POST method for `/webhook/sms`
   - Deploy API

3. **Set up SNS (Optional):**
   - For Telegram message sending

## 📱 SMS Forwarder Setup

### Android App Configuration
Use any SMS forwarder app (like "SMS Forwarder" or "SMS to URL"):

**Webhook URL:** `https://your-domain.com/webhook/sms`

**POST Data Format:**
```json
{
  "message": "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456",
  "sender": "MPESA",
  "timestamp": "2025-01-23 10:30:00"
}
```

**Filter Settings:**
- Sender contains: "MPESA"
- Message contains: "Confirmed"

## 🧪 Testing

### 1. Test Webhook
```bash
curl -X POST https://your-domain.com/webhook/test \
  -H "Content-Type: application/json" \
  -d '{"test": "message"}'
```

### 2. Test Payment Flow
```bash
curl -X POST https://your-domain.com/webhook/sms \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456",
    "sender": "MPESA"
  }'
```

### 3. Test Bot Commands
- `/start` - Welcome message
- `/join` - Get payment instructions
- `/status` - Check payment status

## 💰 Business Flow

1. **User subscribes:** `/join` command
2. **Bot responds:** Payment instructions + unique reference code
3. **User pays:** Ksh 50 to 0791260817 with reference code
4. **SMS forwarded:** Android app sends M-Pesa SMS to webhook
5. **Bot verifies:** Checks reference code and amount
6. **Auto-invite:** Sends group invite link to user

## 🔒 Security Features

- ✅ Environment variables for sensitive data
- ✅ Unique reference codes per user
- ✅ Payment verification via M-Pesa SMS
- ✅ Database tracking of all transactions
- ✅ Automatic invite link generation

## 📊 Monitoring

### Database Queries
```sql
-- Check recent payments
SELECT * FROM payments ORDER BY created_at DESC LIMIT 10;

-- Count successful payments
SELECT COUNT(*) FROM payments WHERE payment_status = 'completed';

-- Revenue calculation
SELECT COUNT(*) * 50 as total_revenue FROM payments WHERE payment_status = 'completed';
```

### Health Checks
- `GET /health` - Service status
- `POST /webhook/test` - Webhook test

## 🚀 Scaling Tips

1. **Multiple Payment Methods:**
   - Add Airtel Money support
   - Add PayPal for international users

2. **Subscription Tiers:**
   - Basic: Ksh 50/month
   - Premium: Ksh 100/month (more job sources)
   - Enterprise: Ksh 200/month (custom alerts)

3. **Analytics:**
   - Track conversion rates
   - Monitor popular job categories
   - User engagement metrics

## 🆘 Troubleshooting

### Common Issues:
1. **Bot not responding:** Check bot token
2. **Webhook not receiving:** Verify SMS forwarder setup
3. **Database errors:** Check SQLite permissions
4. **Payment not detected:** Verify reference code format

### Logs:
- Check application logs in Render dashboard
- Monitor webhook calls
- Track database transactions

## 💡 Revenue Projections

**Conservative Estimates:**
- 100 users/month × Ksh 50 = Ksh 5,000/month
- 500 users/month × Ksh 50 = Ksh 25,000/month
- 1000 users/month × Ksh 50 = Ksh 50,000/month

**Growth Strategy:**
1. Start with job seekers in Kenya
2. Expand to other East African countries
3. Add premium features (CV review, interview prep)
4. Partner with recruitment agencies

---

🎯 **Agent-21 Scout Premium** - Your automated path to remote job success!