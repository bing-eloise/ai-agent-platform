from src.rag.knowledge_base import KnowledgeBase

class RAGTool:
    """知识库查询工具"""
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def query(self, question: str) -> str:
        """查询本地知识库"""
        if not question:
            raise ValueError("question cannot be empty")
        return self.knowledge_base.ask(question, top_k=2)