import random
import requests

from ..utils.logging import log


# Local fallback quotes (never breaks)
FALLBACK_QUOTES = [
    (
        "You have power over your mind — not outside events. Realize this, and you will find strength.",
        "Marcus Aurelius",
    ),
    (
        "We suffer more often in imagination than in reality.",
        "Seneca",
    ),
    (
        "First say to yourself what you would be; and then do what you have to do.",
        "Epictetus",
    ),
    (
        "The happiness of your life depends upon the quality of your thoughts.",
        "Marcus Aurelius",
    ),
    (
        "If it is not right, do not do it; if it is not true, do not say it.",
        "Marcus Aurelius",
    ),
]


def fetch_stoic_quote():
    """
    Fetch a Stoic quote from an online API.
    If the API fails, return a random fallback quote.
    """
    url = "https://stoic-quotes.com/api/quote"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            quote = data.get("text")
            author = data.get("author", "Unknown")
            if quote:
                return quote, author
        log("⚠️ Stoic API returned invalid data, using fallback")
    except Exception as e:
        log(f"⚠️ Stoic API error: {e} — using fallback")

    # Fallback
    return random.choice(FALLBACK_QUOTES)
