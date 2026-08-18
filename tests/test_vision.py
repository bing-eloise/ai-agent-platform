import pytest
from src.multimodal.vision import VisionService, MockVisionProvider

def test_mock_vision():
    provider = MockVisionProvider()
    service = VisionService(provider)
    result = service.analyze_image("data/images/test.png", "请描述这张图片")
    assert "Mock Vision Result" in result

def test_empty_prompt():
    provider = MockVisionProvider()
    service = VisionService(provider)
    with pytest.raises(ValueError):
        service.analyze_image("data/images/test.png", "")