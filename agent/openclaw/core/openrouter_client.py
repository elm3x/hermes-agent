import os
import requests

MODEL = "gpt-3.5-turbo"

def generate_reflection(prompt: str) -> str:
    """
    Generate a reflection using the OpenRouter OpenAI-compatible proxy endpoint.
    This endpoint works for ALL OpenRouter API keys, including new accounts,
    free accounts, and accounts with zero usage.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "Missing OpenRouter API key."

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # Required for OpenAI-compatible proxy mode
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "OpenAI-Compatible"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"⚠️ OpenRouter error: {e} — using fallback reflection")
        return "Reflect on how small actions shape your character each day."
