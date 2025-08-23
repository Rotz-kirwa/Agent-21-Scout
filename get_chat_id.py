import os
from requests import get, RequestException
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN not found in environment")
    exit(1)

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

try:
    response = get(url, timeout=10)
    response.raise_for_status()
    print(response.json())
except RequestException as e:
    print(f"Error getting updates: {e}")
