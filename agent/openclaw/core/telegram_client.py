import requests
from ..utils.logging import log


TELEGRAM_URL = "https://api.telegram.org/bot{token}/sendMessage"
MAX_LENGTH = 4000  # Telegram hard limit is 4096, keep safe margin


def _split_message(text: str):
    """
    Split long messages into Telegram-safe chunks.
    """
    if len(text) <= MAX_LENGTH:
        return [text]

    parts = []
    while len(text) > MAX_LENGTH:
        chunk = text[:MAX_LENGTH]
        parts.append(chunk)
        text = text[MAX_LENGTH:]
    parts.append(text)
    return parts


def send_telegram_message(bot_token: str, chat_id: str, text: str):
    """
    Send a message to Telegram. Auto-splits if needed.
    """
    url = TELEGRAM_URL.format(token=bot_token)
    chunks = _split_message(text)

    for idx, chunk in enumerate(chunks, start=1):
        try:
            response = requests.post(
                url,
                json={
                    "chat_id": chat_id,
                    "text": chunk,
                    "parse_mode": "HTML",
                    "disable_web_page_preview": True,
                },
                timeout=10,
            )
            response.raise_for_status()
        except Exception as e:
            log(f"❌ Telegram send error on chunk {idx}: {e}")
            return False

    log("📨 Telegram message sent successfully")
    return True
