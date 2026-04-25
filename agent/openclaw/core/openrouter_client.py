import requests
from ..utils.logging import log


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openrouter/auto"  # Stable, high‑quality default


def generate_reflection(api_key: str, quote: str, source: str) -> str:
    """
    Generate a Stoic reflection using OpenRouter.
    Returns a clean text reflection.
    """

    prompt = (
        "You are a Stoic philosophy guide. Write a calm, modern, leadership‑oriented "
        "reflection based on the following Stoic quote. Keep it concise, insightful, "
        "and grounded in practical wisdom.\n\n"
        f"Quote: \"{quote}\"\n"
        f"Author: {source}\n\n"
        "Write 2–3 short paragraphs."
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com",  # Required by OpenRouter
        "X-Title": "Daily Digest Agent",
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
    }

    try:
        response = requests.post(OPENROUTER_URL, json=body, headers=headers, timeout=20)
        response.raise_for_status()
        data = response.json()

        # Extract text safely
        content = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )

        if not content:
            log("⚠️ OpenRouter returned empty content — using fallback reflection")
            return _fallback_reflection(quote, source)

        return content.strip()

    except Exception as e:
        log(f"⚠️ OpenRouter error: {e} — using fallback reflection")
        return _fallback_reflection(quote, source)


def _fallback_reflection(quote: str, source: str) -> str:
    """
    Simple fallback reflection if OpenRouter fails.
    """
    return (
        f"The Stoic teaching from {source} reminds us to pause and examine our inner life. "
        f"\"{quote}\" encourages a mindset of clarity and self‑command — qualities that "
        "remain essential in modern leadership. When we focus on what we can control, "
        "we create space for better decisions and calmer action.\n\n"
        "Let this quote guide your day with steadiness and intention."
    )
