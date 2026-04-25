from datetime import datetime
from ..utils.logging import log
from .stoic import fetch_stoic_quote
from .openrouter_client import generate_reflection
from .tavily_client import fetch_ai_news, fetch_world_news
from .digest_builder import build_digest_message
from .telegram_client import send_telegram_message


def run_daily_digest(config: dict):
    """
    Main orchestrator for the daily digest workflow.
    Produces NO stdout digest output — Telegram only.
    """

    log("🚀 Starting Daily Digest workflow")

    # 1. Fetch Stoic quote
    log("📜 Fetching Stoic quote…")
    quote, source = fetch_stoic_quote()

    # 2. Generate reflection via OpenRouter
    log("🧠 Generating reflection…")
    reflection = generate_reflection(reflection_prompt)


    # 3. Fetch AI news via Tavily
    log("🤖 Fetching AI news…")
    ai_news = fetch_ai_news(api_key=config["env"]["TAVILY_API_KEY"])

    # 4. Fetch world news via Tavily
    log("🌍 Fetching world news…")
    world_news = fetch_world_news(api_key=config["env"]["TAVILY_API_KEY"])

    # 5. Build final digest message
    log("📝 Building digest message…")
    timestamp = datetime.now().strftime("%A, %B %d, %Y")
    message = build_digest_message(
        timestamp=timestamp,
        quote=quote,
        source=source,
        reflection=reflection,
        ai_news=ai_news,
        world_news=world_news,
    )

    # 6. Send to Telegram
    log("📨 Sending digest to Telegram…")
    send_telegram_message(
        bot_token=config["env"]["TELEGRAM_BOT_TOKEN"],
        chat_id=config["env"]["TELEGRAM_CHAT_ID"],
        text=message,
    )

    log("✅ Daily Digest sent successfully")
