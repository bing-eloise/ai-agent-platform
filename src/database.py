"""负责创建数据库、保存消息、查询历史"""
import sqlite3
import os
from datetime import datetime

DB_PATH = "memory.db"

class DatabaseManager:
    """SQLite数据库管理"""

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        # 会话表
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations
            (
                id TEXT PRIMARY KEY,
                created_time TEXT
            )
            """
        )
        # 消息表
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT,
                role TEXT,
                content TEXT,
                timestamp TEXT
            )
            """
        )
        # 摘要表
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS summaries
            (
                conversation_id TEXT PRIMARY KEY,
                summary TEXT,
                updated_time TEXT
            )
            """
        )
        self.conn.commit()

    def save_conversation(self, conversation_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO conversations
            VALUES (?,?)
            """,
            (
                conversation_id,
                datetime.now().isoformat()
            )
        )
        self.conn.commit()

    def save_summary(self, conversation_id, summary):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO summaries
            (
                conversation_id,
                summary,
                updated_time
            )
            VALUES (?,?,?)
            ON CONFLICT(conversation_id)
            DO UPDATE SET
                summary=excluded.summary,
                updated_time=excluded.updated_time
            """,
            (
                conversation_id,
                summary,
                datetime.now().isoformat()
            )
        )
        self.conn.commit()

    def load_summary(self, conversation_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT summary
            FROM summaries
            WHERE conversation_id=?
            """,
            (conversation_id,)
        )
        result = cursor.fetchone()
        if result:
            return result[0]
        return ""

    def save_message(self, conversation_id, role, content):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO messages
            (
                conversation_id,
                role,
                content,
                timestamp
            )
            VALUES (?,?,?,?)
            """,
            (
                conversation_id,
                role,
                content,
                datetime.now().isoformat()
            )
        )
        self.conn.commit()

    def load_messages(self, conversation_id):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT role,content
            FROM messages
            WHERE conversation_id=?
            ORDER BY id
            """,
            (conversation_id,)
        )
        rows = cursor.fetchall()
        return [
            {"role": row[0], "content": row[1]}
            for row in rows
        ]

    def get_latest_conversation(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT id
            FROM conversations
            ORDER BY created_time DESC
            LIMIT 1
            """
        )
        result = cursor.fetchone()
        if result:
            return result[0]
        return None