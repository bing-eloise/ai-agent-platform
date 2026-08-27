from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_chat_api():
    with patch("src.api.routes.ask_llm", return_value="你好！"):
        response = client.post("/chat", json={"message":"你好"})
    assert response.status_code == 200
    assert response.json() == {"answer": "你好！"}

def test_chat_empty_message():
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 422

def test_rag_api():
    mock_kb = MagicMock()
    mock_kb.ask.return_value = "Chunk Overlap可以减少上下文丢失。"
    with patch("src.api.routes.get_knowledge_base", return_value=mock_kb):
        response = client.post("/rag", json={"question": "Chunk Overlap有什么作用？"})
    assert response.status_code == 200
    assert "上下文丢失" in response.json()["answer"]
    mock_kb.ask.assert_called_once_with("Chunk Overlap有什么作用？", top_k=2)

def test_agent_api():
    mock_agent = MagicMock()
    mock_agent.run.return_value = "128乘以37等于4736."
    with patch("src.api.routes.get_agent", return_value=mock_agent):
        response = client.post("/agent", json={"message": "计算128乘以37"})
    assert response.status_code == 200
    assert "4736" in response.json()["answer"]
    mock_agent.run.assert_called_once_with("计算128乘以37")

def test_vision_api():
    mock_vision_service = MagicMock()
    mock_vision_service.analyze_image.return_value = "这是一张测试图片。"
    with patch("src.api.routes.get_vision_service", return_value=mock_vision_service):
        with open("data/images/test.png", "rb") as image_file:
            response = client.post(
                "/vision",
                data={"prompt": "请描述这张图片"},
                files={"image": ("test.png", image_file, "image/png")
                }
            )
    assert response.status_code == 200
    assert response.json() == {"answer": "这是一张测试图片。"}
    mock_vision_service.analyze_image.assert_called_once()

def test_vision_api_missing_prompt():
    with open("data/images/test.png", "rb") as image_file:
        response = client.post(
            "/vision",
            files={"image": ("test.png", image_file, "image/png")
            }
        )
    assert response.status_code == 422