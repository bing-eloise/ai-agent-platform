"""把长文本切成多个 Chunk"""

def split_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list[str]:
    """
    将长文本切分成多个有重叠的文本块。
    :param chunk_size: 每个文本块最大字符数
    :param chunk_overlap: 相邻文本块之间的重叠字符数
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap

    return chunks