import requests
from ..utils.logging import log


TAVILY_URL = "https://api.tavily.com/search"


def _tavily_query(api_key: str, query: str, max_results: int = 5):
    """
    Internal helper to call Tavily API and return a list of summaries.
    """
    body = {
        "api_key": api_key,
        "query": query,
        "max_results": max_results,
        "include_answer": False,
        "include_images": False,
    }

    try:
        response = requests.post(TAVILY_URL, json=body, timeout=15)
        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])
        summaries = []

        for item in results:
            summary = item.get("content") or item.get("snippet") or ""
            if summary:
                summaries.append(summary.strip())

        if not summaries:
            log(f"⚠️ Tavily returned no summaries for query: {query}")

        return summaries[:max_results]

    except Exception as e:
        log(f"⚠️ Tavily error for query '{query}': {e}")
        return []


def fetch_ai_news(api_key: str):
    """
    Fetch AI-related news using Tavily.
    Returns a list of bullet-ready strings.
    """
    queries = [
        "latest news OpenAI",
        "latest news Anthropic",
        "latest news Google DeepMind",
        "AI research breakthroughs",
        "AI industry updates",
    ]

    all_results = []
    for q in queries:
        all_results.extend(_tavily_query(api_key, q))

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for item in all_results:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    # Limit to 5 bullets
    return unique[:5]


def fetch_world_news(api_key: str):
    """
    Fetch general world news using Tavily.
    Returns a list of bullet-ready strings.
    """
    query = "top world news today major global events breaking updates"
    results = _tavily_query(api_key, query, max_results=5)
    return results or ["No major world news available at the moment."]
