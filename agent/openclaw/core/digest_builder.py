def _format_bullets(items):
    """
    Convert a list of strings into clean bullet points.
    """
    if not items:
        return "- No items available."
    return "\n".join(f"- {item}" for item in items)


def build_digest_message(timestamp: str, quote: str, source: str,
                         reflection: str, ai_news: list, world_news: list) -> str:
    """
    Build the final combined digest message with emojis and timestamp.
    Telegram-safe (HTML formatting).
    """

    ai_section = _format_bullets(ai_news)
    world_section = _format_bullets(world_news)

    message = f"""📅 <b>{timestamp}</b>

📜 <b>Stoic Quote</b>
“{quote}”
— {source}

🧠 <b>Reflection</b>
{reflection}

🤖 <b>AI News</b>
{ai_section}

🌍 <b>World News</b>
{world_section}
"""

    return message.strip()
