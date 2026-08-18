"""读取、校验、编码图片"""
from pathlib import Path
import base64
import mimetypes

SUPPORTED_IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
MAX_IMAGE_SIZE = 5*1024*1024

def validate_image(file_path: str) -> Path:
    """
    校验图片文件。
    检查：文件是否存在、文件类型是否合法、文件大小是否超过限制
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {file_path}")
    if not path.is_file():
        raise ValueError("image path must point to a file")
    if path.suffix.lower() not in SUPPORTED_IMAGE_TYPES:
        raise ValueError(f"unsupported image type: {path.suffix}")
    if path.stat().st_size > MAX_IMAGE_SIZE:
        raise ValueError("image size exceeds 5MB limit")
    return path

def load_image(file_path: str) -> bytes:
    """读取图片并返回二进制数据"""
    path = validate_image(file_path)
    return path.read_bytes()

def encode_image_base64(image_bytes: bytes) -> str:
    """将图片二进制编码为Base64字符串"""
    if not image_bytes:
        raise ValueError("image bytes cannot be empty")
    encoded = base64.b64encode(image_bytes)
    return encoded.decode("utf-8")

def image_to_data_url(file_path: str) -> str:
    """将图片转换成Data URL"""
    path = validate_image(file_path)
    image_bytes = load_image(file_path)
    mime_type, _ = mimetypes.guess_type(path.name)
    if mime_type is None:
        raise ValueError("unable to determine image MIME type")
    encoded = encode_image_base64(image_bytes)
    return (
        f"data:{mime_type};base64,{encoded}"
    )