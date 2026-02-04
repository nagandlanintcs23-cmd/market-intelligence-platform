def compress_text(text: str) -> str:
    """
    Simple rule-based text compressor (no AI, no dependencies).
    """
    if not text:
        return "No content provided."

    sentences = text.split(".")
    compressed = ".".join(sentences[:3])
    return compressed.strip()
