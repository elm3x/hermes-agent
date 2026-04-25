# OpenClaw (Reconstructed Minimal Runtime)
# Package initializer

# Patch for legacy OpenClaw versions that imported TimeoutError
# from cmdop.exceptions — this no longer exists in modern cmdop.
try:
    from cmdop.exceptions import TimeoutError  # Legacy import
except Exception:
    # Fallback to built‑in Exception so imports never break
    TimeoutError = Exception

__all__ = ["TimeoutError"]
