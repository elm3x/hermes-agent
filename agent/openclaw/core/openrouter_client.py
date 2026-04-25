import requests

HF_MODEL = "google/gemma-2b-it"
HF_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"


def generate_reflection(prompt: str) -> str:
    """
    Generate a reflection using HuggingFace's free inference API.
    No API key required for public models.
    """

    payload = {
        "inputs": f"Write a short Stoic reflection based on this quote:\n\n{prompt}\n\nReflection:",
        "parameters": {
            "max_new_tokens": 120,
            "temperature": 0.7,
        }
    }

    try:
        response = requests.post(HF_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        # HF returns a list of dicts with 'generated_text'
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"].strip()

        # Some models return a dict with 'generated_text'
        if isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"].strip()

        return "Reflect on how small actions shape your character each day."

    except Exception as e:
        print(f"⚠️ HuggingFace error: {e} — using fallback reflection")
        return "Reflect on how small actions shape your character each day."
