from src.llm import ask_llm
from src.prompt import build_rag_prompt
from src.rag.retriever import Retriever

class RAGService:
    """
    RAG知识库问答服务
    负责：
    Question
        -> Retrieval
        -> Context
        -> Prompt
        -> LLM
        -> Answer
    """
    def __init__(self, retriever: Retriever, min_relevance_score: float = 0.30):
        self.retriever = retriever
        self.min_relevance_score = min_relevance_score

    def ask(self, question: str, top_k: int = 3) -> str:
        """根据知识库回答用户问题"""
        if not question:
            raise ValueError("question cannot be empty")

        # 检索相关知识
        results = self.retriever.retriever(question, top_k=top_k)
        if not results:
            return "根据当前知识库内容，无法回答该问题。"

        best_score = results[0]["score"]
        if best_score < self.min_relevance_score:
            return "根据当前知识库内容，无法回答该问题。"

        # 构造知识库上下文
        context = self.retriever.build_context(results)

        # 构造RAG Prompt
        prompt = build_rag_prompt(context, question)

        # 调用LLM
        messages = [{"role": "user", "content": prompt}]
        answer = ask_llm(messages)
        return answer