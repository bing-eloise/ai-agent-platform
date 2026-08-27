from unittest.mock import MagicMock, patch
from src.summary import SummaryMemory

def test_summary_memory_load():
    mock_db = MagicMock()
    mock_db.load_summary.return_value = ("已有摘要")
    memory = SummaryMemory(mock_db, "test-conversation")
    assert memory.get_summary() == "已有摘要"

def test_summary_memory_update():
    mock_db = MagicMock()
    mock_db.load_summary.return_value = ""
    memory = SummaryMemory(mock_db, "test-conversation")
    memory.update_summary("新的摘要")
    assert memory.get_summary() == "新的摘要"
    mock_db.save_summary.assert_called_once_with("test-conversation", "新的摘要")


def test_generate_summary():
    mock_db = MagicMock()
    mock_db.load_summary.return_value = ("旧摘要")
    memory = SummaryMemory(mock_db, "test-conversation")
    with patch("src.summary.ask_llm", return_value="这是模型生成的新摘要") as mock_llm:
        summary = memory.generate_summary([{"role": "user", "content": "新的聊天内容"}])
    assert summary == "这是模型生成的新摘要"
    mock_llm.assert_called_once()

def test_summary_length_limit():
    mock_db = MagicMock()
    mock_db.load_summary.return_value = ""
    memory = SummaryMemory(mock_db, "test-conversation")
    long_summary = "A" * 1000
    with patch("src.summary.ask_llm", return_value=long_summary):
        summary = memory.generate_summary([{"role": "user", "content": "test"}])
    assert len(summary) == 500