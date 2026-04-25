# Custom error types for the reconstructed OpenClaw runtime.

class OpenClawError(Exception):
    """Base class for all custom OpenClaw errors."""
    pass


class ConfigError(OpenClawError):
    """Raised when config.yaml is invalid or missing required fields."""
    pass


class NetworkError(OpenClawError):
    """Raised for network-related failures (OpenRouter, Tavily, Telegram)."""
    pass


# Legacy compatibility: some old OpenClaw versions referenced TimeoutError
try:
    from cmdop.exceptions import TimeoutError  # Legacy import
except Exception:
    TimeoutError = Exception
