"""
Summary Memory负责长对话摘要管理：
    1、接收历史消息。
    2、生成摘要。
    3、保存摘要。
    4、提供摘要内容。
"""
from src.llm import ask_llm

class SummaryMemory:
    def __init__(self, db, conversation_id):
        self.db = db
        self.conversation_id = conversation_id
        self.summary = self.db.load_summary(conversation_id)

    def generate_summary(self, messages):
        prompt = [
            {
                "role": "system",
                "content": "根据已有摘要和新的聊天内容，重新生成一个新的摘要。保留重要信息，简洁输出。"
            },
            {
                "role": "user",
                "content":
                    f"""
                    当前摘要：{self.summary}
                    新聊天记录：{messages}
                    """
            }
        ]
        summary = ask_llm(prompt)
        summary = summary[:500]
        return summary

    def update_summary(self, new_summary: str):
        self.summary = new_summary
        self.db.save_summary(self.conversation_id, new_summary)

    def get_summary(self):
        return self.summary