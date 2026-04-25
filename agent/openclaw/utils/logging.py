def log(message: str):
    """
    Minimal logging utility.
    Prints small status messages only — never the digest content.
    """
    print(message, flush=True)
