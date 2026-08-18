"""构造多模态Message"""
def build_multimodal_message(prompt: str, image_data_url: str) -> list[dict]:
    """
    构造多模态用户消息。
    包含：文本输入、图片输入
    """
    if not prompt:
        raise ValueError("prompt cannot be empty")

    if not image_data_url:
        raise ValueError("image_data_url cannot be empty")

    message = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {"url": image_data_url}
                }
            ]
        }
    ]
    return message