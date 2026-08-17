from unittest.mock import patch
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
    with patch.object(
        __import__("src.api.routes", fromlist=["knowledge_base"]).knowledge_base,
        "ask",
        return_value="Chunk Overlap可以减少上下文丢失。"
    ):
        response = client.post("/rag", json={"question": "Chunk Overlap有什么作用？"})
    assert response.status_code == 200
    assert "上下文丢失" in response.json()["answer"]

def test_agent_api():
    with patch.object(
        __import__("src.api.routes", fromlist=["agent"]).agent,
        "run",
        return_value="128乘以37等于4736."
    ):
        response = client.post("/agent", json={"message": "计算128乘以37"})
        assert response.status_code == 200
        assert "4736" in response.json()["answer"]