import uuid
from datetime import datetime
from src.database import DatabaseManager
from src.tokenizer import estimate_tokens
from config.settings import MAX_HISTORY, MAX_TOKENS
from src.logger import logger

class ChatMemory:
    """Conversation Memory 管理用户聊天上下文"""
    def __init__(self, max_history=MAX_HISTORY, max_tokens=MAX_TOKENS):
        # 创建ChatMemory时会自动创建会话
        self.db = DatabaseManager()
        # 会话ID
        latest_id = self.db.get_latest_conversation()
        if latest_id:
            self.conversation_id = latest_id
        else:
            self.conversation_id = str(uuid.uuid4())
        self.db.save_conversation(self.conversation_id)
        # 创建时间
        self.created_time = datetime.now()
        # 最大保存消息数量
        self.max_history = max_history
        # 最大保存token大小
        self.max_tokens = max_tokens
        # 消息列表
        self.messages = self.db.load_messages(self.conversation_id)

    def add_user_message(self, content: str):
        self.messages.append(
            {
                "role": "user",
                "content": content,
                "time": datetime.now().isoformat()
            }
        )
        self.db.save_message(self.conversation_id, "user", content)
        self._limit_history()

    def add_assistant_message(self, content: str):
        self.messages.append(
            {
                "role": "assistant",
                "content": content,
                "time": datetime.now().isoformat()
            }
        )
        self.db.save_message(self.conversation_id, "assistant", content)
        self._limit_history()

    def get_messages(self):
        return [
            {
                "role": message["role"],
                "content": message["content"]
            }
            for message in self.messages
        ]

    def get_token_count(self):
        return estimate_tokens(self.messages)

    def _limit_history(self):
        """第一层限制：消息数量"""
        if len(self.messages) > self.max_history:
            removed = len(self.messages) - self.max_history
            self.messages = self.messages[-self.max_history:]
            logger.warning(f"History limit reached, removed {removed} messages")

        """第二层限制：token数量"""
        while self.get_token_count() > self.max_tokens:
            self.messages.pop(0)
            logger.warning(
                f"Token limit reached, removed old message. "
                f"Current tokens: {self.get_token_count()}"
            )

    def get_memory_info(self):
        current_tokens = self.get_token_count()
        return {
            "conversation_id": self.conversation_id,
            "message_count": len(self.messages),
            "estimated_tokens": current_tokens,
            "max_tokens": self.max_tokens,
            "usage_rate": round(current_tokens / self.max_tokens * 100, 2)
        }