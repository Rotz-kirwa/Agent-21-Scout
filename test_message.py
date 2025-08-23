from telegram_bot import send_telegram_message

# Send a test message
try:
    result = send_telegram_message("✅ Telegram bot test message")
    if result:
        print("Test message sent successfully!")
    else:
        print("Failed to send test message")
except Exception as e:
    print(f"Error: {e}")
