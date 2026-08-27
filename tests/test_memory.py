import src.database as database_module
from src.memory import ChatMemory

def test_memory_add_messages(tmp_path, monkeypatch):
    test_db = tmp_path / "memory_test.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))
    memory = ChatMemory(max_history=10, max_tokens=500)

    memory.add_user_message("你好")
    memory.add_assistant_message("你好！")
    messages = memory.get_messages()

    assert len(messages) == 2
    assert messages[0] == {"role": "user", "content": "你好"}
    assert messages[1] == {"role": "assistant", "content": "你好！"}
    memory.db.conn.close()

def test_memory_history_limit(tmp_path, monkeypatch):
    test_db = tmp_path / "history.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))
    memory = ChatMemory(max_history=3, max_tokens=1000)

    memory.add_user_message("1")
    memory.add_user_message("2")
    memory.add_user_message("3")
    memory.add_user_message("4")

    assert len(memory.messages) == 3
    assert memory.messages[0]["content"] == "2"
    memory.db.conn.close()

def test_memory_info(tmp_path, monkeypatch):
    test_db = tmp_path / "info.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))
    memory = ChatMemory(max_history=10, max_tokens=100)

    memory.add_user_message("hello")
    info = memory.get_memory_info()

    assert "conversation_id" in info
    assert info["message_count"] == 1
    assert info["estimated_tokens"] == 5
    assert info["max_tokens"] == 100
    assert info["usage_rate"] == 5.0
    memory.db.conn.close()

def test_memory_auto_summary(tmp_path, monkeypatch):
    test_db = tmp_path / "summary_memory.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))
    memory = ChatMemory(max_history=20, max_tokens=20)

    memory.summary_memory.generate_summary = (lambda messages: "历史摘要")
    memory.summary_memory.update_summary = (lambda summary: setattr(memory.summary_memory, "summary", summary))

    for i in range(6):
        memory.add_user_message(f"这是一条比较长的消息{i}")

    assert memory.summary_memory.get_summary() == "历史摘要"
    assert len(memory.messages) <= 5
    memory.db.conn.close()