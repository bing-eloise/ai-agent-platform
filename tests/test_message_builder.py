import pytest
from src.multimodal.message_builder import build_multimodal_message

def test_build_multimodal_message():
    data_url = ("data:image/png;base64,abc123")
    messages = build_multimodal_message("请描述这张图片", data_url)
    assert len(messages) == 1
    message = messages[0]
    assert message["role"] == "user"
    assert len(message["content"]) == 2
    assert message["content"][0]["type"] == "text"
    assert message["content"][1]["type"] == "image_url"

def test_empty_prompt():
    with pytest.raises(ValueError):
        build_multimodal_message("", "data:image/png;base64,abc")

def test_empty_image():
    with pytest.raises(ValueError):
        build_multimodal_message("描述图片", "")