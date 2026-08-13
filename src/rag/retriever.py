"""Retriever：接收用户问题，自动完成 Query Embedding + Vector Search"""
"""Retriever负责“找知识”，Context Builder负责“整理知识”"""
from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore

class Retriever:
    """
    RAG 检索器
    负责： Query -> Embedding -> Vector Search
    """
    def __init__(self, embedding_model: EmbeddingModel, vector_store: VectorStore):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retriever(self, query: str, top_k: int = 3) -> list[dict]:
        """根据用户问题检索最相关的文档 Chunk"""
        if not query:
            raise ValueError("query cannot be empty")
        query_vector = self.embedding_model.embed_text(query)
        results = self.vector_store.search(query_vector, top_k=top_k)
        return results

    def build_context(self, results: list[dict]) -> str:
        """将检索结果整理为可供LLM使用的上下文"""
        if not results:
            return ""
        context_parts = []
        for index, result in enumerate(results, start=1):
            text = result["text"]
            context_parts.append(f"[知识{index}]\n{text}")
        return "\n\n".join(context_parts)