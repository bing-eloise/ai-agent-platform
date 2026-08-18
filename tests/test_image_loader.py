import pytest
from src.multimodal.image_loader import validate_image, load_image, encode_image_base64, image_to_data_url

def test_validate_image():
    path = validate_image("data/images/test.png")
    assert path.exists()
    assert path.suffix == ".png"

def test_load_image():
    image = load_image("data/images/test.png")
    assert isinstance(image, bytes)
    assert len(image) > 0

def test_image_not_found():
    with pytest.raises(FileNotFoundError):
        validate_image("data/images/not_found.png")

def test_unsupported_image_type(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("not an image")
    with pytest.raises(ValueError):
        validate_image(str(file_path))

def test_encode_image_base64():
    image = load_image("data/images/test.png")
    encoded = encode_image_base64(image)
    assert isinstance(encoded, str)
    assert len(encoded) > 0

def test_image_to_data_url():
    data_url = image_to_data_url("data/images/test.png")
    assert data_url.startswith("data:image/png;base64,")

def test_encode_empty_image():
    with pytest.raises(ValueError):
        encode_image_base64(b"")