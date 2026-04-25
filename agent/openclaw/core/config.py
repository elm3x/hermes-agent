import os
import yaml
from pathlib import Path

from ..utils.logging import log


def _resolve_env(value: str) -> str:
    """
    Replace ${VAR} with environment variable values.
    """
    if not isinstance(value, str):
        return value

    if value.startswith("${") and value.endswith("}"):
        env_name = value[2:-1]
        resolved = os.getenv(env_name)
        if resolved is None:
            raise RuntimeError(f"Missing required environment variable: {env_name}")
        return resolved

    return value


def _resolve_env_in_dict(d: dict) -> dict:
    """
    Recursively resolve environment variables in a nested dict.
    """
    resolved = {}
    for key, value in d.items():
        if isinstance(value, dict):
            resolved[key] = _resolve_env_in_dict(value)
        elif isinstance(value, list):
            resolved[key] = [_resolve_env(v) for v in value]
        else:
            resolved[key] = _resolve_env(value)
    return resolved


def load_config(path: Path) -> dict:
    """
    Load config.yaml and resolve environment variables.
    """
    log(f"📄 Loading config from {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    if not isinstance(raw, dict):
        raise RuntimeError("Invalid config.yaml format — expected a dictionary at root.")

    resolved = _resolve_env_in_dict(raw)

    # Validate required env vars
    required_env = [
        "OPENROUTER_API_KEY",
        "TAVILY_API_KEY",
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_CHAT_ID",
    ]

    for var in required_env:
        if os.getenv(var) is None:
            raise RuntimeError(f"Missing required environment variable: {var}")

    log("✅ Config loaded and environment variables resolved")
    return resolved
