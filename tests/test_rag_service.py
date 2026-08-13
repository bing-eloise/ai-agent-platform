from unittest.mock import patch
from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore
from src.rag.retriever import Retriever
from src.rag.rag_service import RAGService

def test_rag_service_with_mock_llm():
    documents = [
        "Chunk Overlap可以减少文本切分边界造成的上下文丢失。",
        "Embedding可以将文本转换成向量。",
        "Python是一种编程语言。"
    ]
    embedding_model = EmbeddingModel()
    vectors = embedding_model.embed_documents(documents)

    vector_store = VectorStore()
    vector_store.add(documents, vectors)

    retriever = Retriever(embedding_model, vector_store)
    rag_service = RAGService(retriever, min_relevance_score=0.30)

    with patch("src.rag.rag_service.ask_llm") as mock_llm:
        mock_llm.return_value = ("Chunk Overlap 可以减少文本切分边界造成的上下文丢失。")
        answer = rag_service.ask("Chunk Overlap有什么作用？", top_k=1)

        assert "上下文丢失" in answer
        mock_llm.assert_called_once()

def test_rag_service_rejects_irrelevant_query():
    documents = [
        "RAG是一种检索增强生成技术。",
        "Embedding可以将文本转换成向量。"
    ]
    embedding_model = EmbeddingModel()
    vectors = embedding_model.embed_documents(documents)

    vector_store = VectorStore()
    vector_store.add(documents, vectors)

    retriever = Retriever(embedding_model, vector_store)
    rag_service = RAGService(retriever, min_relevance_score=0.99)

    with patch("src.rag.rag_service.ask_llm") as mock_llm:
        answer = rag_service.ask("法国的首都是哪里？", top_k=1)

        assert "无法回答" in answer
        mock_llm.assert_not_called()