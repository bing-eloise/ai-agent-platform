import src.database as database_module
from src.database import DatabaseManager

def test_database_message_storage(tmp_path, monkeypatch):
    test_db = tmp_path / "test_memory.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))

    db = DatabaseManager()
    conversation_id = "test-conversation"
    db.save_conversation(conversation_id)
    db.save_message(conversation_id, "user", "你好")
    db.save_message(conversation_id, "assistant", "你好！")
    messages = db.load_messages(conversation_id)

    assert messages == [
        {
            "role": "user",
            "content": "你好"
        },
        {
            "role": "assistant",
            "content": "你好！"
        }
    ]
    db.conn.close()

def test_database_summary(tmp_path, monkeypatch):
    test_db = tmp_path / "test_summary.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))

    db = DatabaseManager()
    conversation_id = "summary-test"
    db.save_conversation(conversation_id)

    db.save_summary(conversation_id, "第一次摘要")
    assert db.load_summary(conversation_id) == "第一次摘要"
    # 验证ON CONFLICT更新
    db.save_summary(conversation_id, "更新后的摘要")
    assert db.load_summary(conversation_id) == "更新后的摘要"
    db.conn.close()

def test_latest_conversation(tmp_path, monkeypatch):
    test_db = tmp_path / "latest.db"
    monkeypatch.setattr(database_module, "DB_PATH", str(test_db))

    db = DatabaseManager()
    assert db.get_latest_conversation() is None
    db.save_conversation("conversation-001")
    assert db.get_latest_conversation() == "conversation-001"
    db.conn.close()