from telegram_bot import send_telegram_message

try:
    result = send_telegram_message("Hello Eliud 🚀! Your bot is working ✅")
    if result:
        print("Message sent successfully!")
    else:
        print("Failed to send message")
except Exception as e:
    print(f"Error: {e}")
