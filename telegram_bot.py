import os
from requests import post, RequestException
from dotenv import load_dotenv
import time

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message: str, delay: float = 0.5):
    """
    Send a message to Telegram with rate limiting.
    Agent-21 Scout Bot - Professional Job Alerts
    """
    if not TOKEN or not CHAT_ID:
        raise ValueError("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID in environment")
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": message, 
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    
    try:
        response = post(url, data=payload, timeout=15)
        response.raise_for_status()
        time.sleep(delay)  # Rate limiting
        return response.json()
    except RequestException as e:
        print(f"❌ Failed to send message: {e}")
        return None

def send_job_summary(total_jobs: int, sources: list):
    """
    Send daily job summary header.
    """
    summary = f"🤖 *Agent-21 Scout Daily Report*\n\n"
    summary += f"📊 Found *{total_jobs}* new opportunities\n"
    summary += f"🔍 Sources: {', '.join(sources)}\n"
    summary += f"⏰ {time.strftime('%Y-%m-%d %H:%M UTC')}\n"
    summary += "━━━━━━━━━━━━━━━━━━━━━━━━"
    
    return send_telegram_message(summary)
