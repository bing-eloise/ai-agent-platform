from src.rag.document_loader import load_text_file
from src.rag.text_splitter import split_text
from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore
from src.rag.retriever import Retriever
from src.rag.rag_service import RAGService

class KnowledgeBase:
    """
    知识库统一入口
    负责：
    Document
        -> Load
        -> Split
        -> Embedding
        -> Vector Store
        -> Retriever
        -> RAG Service
    """
    def __init__(self, file_path: str, chunk_size: int = 150, chunk_overlap: int = 30, min_relevance_score: float = 0.30):
        self.file_path = file_path
        # 加载知识库
        text = load_text_file(file_path)
        # Chunk
        self.chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        # Embedding模型
        self.embedding_model = EmbeddingModel()
        # Chunk向量化
        vectors = self.embedding_model.embed_documents(self.chunks)
        # Vector Store
        self.vector_store = VectorStore()
        self.vector_store.add(self.chunks, vectors)
        # Retriever
        self.retriever = Retriever(self.embedding_model, self.vector_store)
        # RAG Service
        self.rag_service = RAGService(self.retriever, min_relevance_score=min_relevance_score)

    def ask(self, question: str, top_k: int = 3) -> str:
        """基于知识库回答问题"""
        return self.rag_service.ask(question, top_k=top_k)