import os
import re
import time
import json
import threading
import sqlite3
from datetime import datetime
from urllib.parse import urljoin

import requests
from flask import Flask, request
from dotenv import load_dotenv

# ---------- ENV ----------
load_dotenv(".env.payment")

BOT_TOKEN = os.getenv("PAYMENT_BOT_TOKEN", "").strip()
GROUP_INVITE_LINK = os.getenv("GROUP_INVITE_LINK", "").strip()
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID", "").strip()  # optional (for per-user invite links)
MPESA_NUMBER = os.getenv("MPESA_NUMBER", "0791260817").strip()
REQUIRED_AMOUNT = int(os.getenv("PAYMENT_AMOUNT", "50"))
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "").strip()

assert BOT_TOKEN, "PAYMENT_BOT_TOKEN missing in .env.payment"

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# ---------- DB ----------
DB_PATH = "payments.db"

def db_init():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            chat_id TEXT PRIMARY KEY,
            phone TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            amount INTEGER,
            tx_info TEXT,
            processed_at TEXT
        )
        """)
        conn.commit()

def set_user_phone(chat_id: str, phone: str):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO users (chat_id, phone, status, created_at) VALUES (?, ?, COALESCE((SELECT status FROM users WHERE chat_id=?),'pending'), COALESCE((SELECT created_at FROM users WHERE chat_id=?),?))",
                  (chat_id, phone, chat_id, chat_id, datetime.utcnow().isoformat()))
        conn.commit()

def mark_user_paid_by_phone(phone: str):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET status='paid' WHERE phone=?", (phone,))
        conn.commit()

def get_user_by_phone(phone: str):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT chat_id, status FROM users WHERE phone=?", (phone,))
        row = c.fetchone()
        if row:
            return {"chat_id": row[0], "status": row[1]}
    return None

def save_payment(phone: str, amount: int, tx_info: str):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO payments (phone, amount, tx_info, processed_at) VALUES (?, ?, ?, ?)",
                  (phone, amount, tx_info, datetime.utcnow().isoformat()))
        conn.commit()

# ---------- Telegram helpers ----------
def tg_send_text(chat_id: str, text: str, disable_preview=True):
    try:
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": disable_preview
        }, timeout=10)
    except Exception as e:
        print("sendMessage error:", e)

def tg_create_invite_link():
    """Create a one-time (single use) invite link if GROUP_CHAT_ID is set and bot is admin."""
    if not GROUP_CHAT_ID:
        return GROUP_INVITE_LINK  # fallback to static link
    try:
        # member_limit=1 makes it single-use; 3600s expiry to be safe
        res = requests.post(f"{TELEGRAM_API}/createChatInviteLink", json={
            "chat_id": GROUP_CHAT_ID,
            "member_limit": 1,
            "creates_join_request": False,
            "expire_date": int(time.time()) + 3600
        }, timeout=10)
        data = res.json()
        link = data.get("result", {}).get("invite_link")
        return link or GROUP_INVITE_LINK
    except Exception as e:
        print("createChatInviteLink error:", e)
        return GROUP_INVITE_LINK

# ---------- SMS parsing ----------
PHONE_RE = re.compile(r"(?:\+?254|0)\s*7[\s\d]{8,}", re.IGNORECASE)
AMOUNT_RE = re.compile(r"Ksh\s*([\d,]+(?:\.\d{1,2})?)", re.IGNORECASE)

def normalize_phone(raw: str) -> str:
    # Keep Kenyan mobile in "07XXXXXXXX" format
    digits = re.sub(r"\D", "", raw)
    if digits.startswith("2547") and len(digits) >= 12:
        return "0" + digits[3:12]
    if digits.startswith("07") and len(digits) >= 10:
        return digits[:10]
    # last resort: take last 9-10 if it ends with Kenyan pattern
    if len(digits) >= 9 and digits[-9:].startswith("7"):
        return "0" + digits[-9:]
    return digits  # as-is

def parse_sms(text: str):
    # amount
    amt = None
    m_amt = AMOUNT_RE.search(text)
    if m_amt:
        amt_str = m_amt.group(1).replace(",", "")
        try:
            amt = int(float(amt_str))
        except:
            amt = None
    # phone
    m_phone = PHONE_RE.search(text)
    phone = normalize_phone(m_phone.group(0)) if m_phone else None
    return phone, amt

# ---------- Bot logic (polling for /join, /start) ----------
POLL_STOP = False

def poll_updates():
    print("Telegram long-poll started…")
    offset = None
    while not POLL_STOP:
        try:
            params = {"timeout": 25}
            if offset:
                params["offset"] = offset
            resp = requests.get(f"{TELEGRAM_API}/getUpdates", params=params, timeout=30)
            data = resp.json()
            for upd in data.get("result", []):
                offset = upd["update_id"] + 1
                msg = upd.get("message") or {}
                chat_id = str((msg.get("chat") or {}).get("id"))
                text = (msg.get("text") or "").strip()

                if not chat_id or not text:
                    continue

                if text.lower() == "/start":
                    tg_send_text(chat_id, (
                        "👋 Hey! This is Agent-21 Payments Bot.\n"
                        f"To join the premium group, send *KSh {REQUIRED_AMOUNT}* to {MPESA_NUMBER}.\n\n"
                        "First, type /join to register the M-Pesa number you'll pay from."
                    ))
                elif text.lower() == "/join":
                    tg_send_text(chat_id, (
                        "✅ Step 1: Reply with the *M-Pesa number* you will pay from (format: 07XXXXXXXX).\n"
                        f"Then pay *KSh {REQUIRED_AMOUNT}* to {MPESA_NUMBER}. We'll auto-detect and DM your invite link."))
                elif re.fullmatch(r"0\d{9}", text):  # phone message
                    set_user_phone(chat_id, text)
                    tg_send_text(chat_id, (
                        f"📌 Got it! We registered {text}.\n"
                        f"Now pay *KSh {REQUIRED_AMOUNT}* to {MPESA_NUMBER}. You'll get your invite link automatically when payment lands."))
                else:
                    # ignore or help
                    if text.startswith("/"):
                        tg_send_text(chat_id, "Commands:\n/start – info\n/join – register your M-Pesa number")
            # loop again
        except Exception as e:
            print("poll error:", e)
            time.sleep(2)

# ---------- Flask app for SMS webhook ----------
app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/sms", methods=["POST"])
def sms_webhook():
    """
    Expected JSON body from SMS forwarder:
    {
      "message": "Confirmed. Ksh50.00 received from 07xx xxx xxx ...",
      "sender": "MPESA",   // optional
      "timestamp": "2025-08-25T09:12:00+03:00"  // optional
    }
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        raw = data.get("message", "") or ""
        if not raw:
            return {"status": "ignored", "reason": "no message"}, 200

        phone, amt = parse_sms(raw)
        print("SMS parsed:", {"phone": phone, "amount": amt})

        # Basic checks
        if not phone or not amt:
            return {"status": "ignored", "reason": "parse_fail"}, 200
        if amt < REQUIRED_AMOUNT:
            return {"status": "ignored", "reason": "amount_too_low", "amount": amt}, 200

        # find a user with that phone who isn't paid
        user = get_user_by_phone(phone)
        if not user:
            # store payment anyway for audit
            save_payment(phone, amt, raw[:500])
            # optionally notify admin
            if ADMIN_CHAT_ID:
                tg_send_text(ADMIN_CHAT_ID, f"💳 Payment {amt} from {phone}, but no user matched.")
            return {"status": "queued_no_user"}, 200

        # send invite link
        invite = tg_create_invite_link()
        tg_send_text(user["chat_id"], f"✅ Payment confirmed! Here's your invite link:\n{invite}")
        mark_user_paid_by_phone(phone)
        save_payment(phone, amt, raw[:500])

        # notify admin
        if ADMIN_CHAT_ID:
            tg_send_text(ADMIN_CHAT_ID, f"🎟️ Access granted to {phone} (chat {user['chat_id']}). Amount: {amt}")

        return {"status": "ok", "granted": True}, 200

    except Exception as e:
        print("sms_webhook error:", e)
        return {"status": "error", "detail": str(e)}, 500

def main():
    db_init()
    t = threading.Thread(target=poll_updates, daemon=True)
    t.start()
    # Flask server for SMS webhook
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()