import pytest
from pydantic import ValidationError
from src.api.schemas import ChatRequest, ChatResponse

def test_chat_request():
    request = ChatRequest(message="你好")
    assert request.message == "你好"

def test_chat_request_empty_message():
    with pytest.raises(ValidationError):
        ChatRequest(message="")

def test_chat_response():
    response = ChatResponse(answer="你好!")
    assert response.answer == "你好!"