import secrets

def create_iv(mode="cbc"):
    mode = mode.lower()

    sizes = {
        "cbc": 16,
        "cfb": 16,
        "ofb": 16,
        "ctr": 16,
        "gcm": 12,
    }

    if mode == "ecb":
        return None

    if mode not in sizes:
        raise ValueError(f"Unsupported mode: {mode}")

    return secrets.token_bytes(sizes[mode])