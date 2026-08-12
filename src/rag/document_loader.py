"""把 TXT/PDF 等文件读取成文本"""
from pathlib import Path

def load_text_file(file_path: str) -> str:
    """读取txt文本文件并返回字符串内容"""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Currently only .txt files are supported")

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

        return text