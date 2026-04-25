import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:1b"


def generate_reflection(prompt: str) -> str:
    """
    Generate a reflection using a local Ollama model.

    Requires:
      - Ollama running locally (`ollama serve`)
      - Model pulled: `ollama pull llama3.2:1b`
    """

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        # Ollama returns: { "model": "...", "created_at": "...", "response": "..." , ... }
        text = data.get("response", "")
        if not isinstance(text, str) or not text.strip():
            return "Reflect on how small actions shape your character each day."

        return text.strip()

    except Exception as e:
        print(f"⚠️ Local model error: {e} — using fallback reflection")
        return "Reflect on how small actions shape your character each day."
