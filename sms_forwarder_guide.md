# 📱 SMS Forwarder Setup Guide

## Download SMS Forwarder App

**Recommended Apps:**
1. **SMS Forwarder** (by Triangular Apps)
2. **SMS to URL** (by Bogdan Mihai)
3. **HTTP SMS** (by Dmitry Kostenko)

## Configuration Steps

### 1. Install App
- Download from Google Play Store
- Grant SMS permissions
- Allow background running

### 2. Create Forwarding Rule

**Filter Settings:**
- Sender contains: `MPESA`
- Message contains: `Confirmed`
- Message contains: `Ksh50` (or your amount)

**Webhook Settings:**
- URL: `https://your-domain.com/webhook/sms`
- Method: `POST`
- Content-Type: `application/json`

**POST Body Template:**
```json
{
  "message": "{message}",
  "sender": "{sender}",
  "timestamp": "{timestamp}"
}
```

### 3. Test Configuration

**Sample M-Pesa SMS:**
```
Confirmed. Ksh50.00 received from 254791260817 on 23/1/25 at 10:30 AM. Reference: 123456. Account balance is Ksh2,500.00
```

**Expected Webhook Data:**
```json
{
  "message": "Confirmed. Ksh50.00 received from 254791260817 on 23/1/25 at 10:30 AM. Reference: 123456. Account balance is Ksh2,500.00",
  "sender": "MPESA",
  "timestamp": "2025-01-23 10:30:00"
}
```

## 🔧 Alternative: Manual Testing

If SMS forwarder isn't working, you can test manually:

```bash
curl -X POST https://your-domain.com/webhook/sms \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Confirmed. Ksh50.00 received from 254791260817. Reference: 123456",
    "sender": "MPESA",
    "timestamp": "2025-01-23 10:30:00"
  }'
```

## 📋 Troubleshooting

**Common Issues:**
1. **App not forwarding:** Check permissions and background running
2. **Wrong format:** Verify POST body template
3. **Network issues:** Test with mobile data and WiFi
4. **Filter not working:** Adjust sender/message filters

**Testing Steps:**
1. Send test SMS to yourself
2. Check if app captures it
3. Verify webhook receives data
4. Check bot response