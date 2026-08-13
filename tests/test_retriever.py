from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore
from src.rag.retriever import Retriever

def test_retriever():
    documents = [
        "RAG是一种检索增强生成技术",
        "Embedding可以把文本转换成向量",
        "Python是一种编程语言"
    ]
    embedding_model = EmbeddingModel()
    vectors = embedding_model.embed_documents(documents)

    vector_store = VectorStore()
    vector_store.add(documents, vectors)

    retriever = Retriever(embedding_model, vector_store)
    results = retriever.retriever("如何把文本转换成向量？", top_k=1)

    assert len(results) == 1
    assert "Embedding" in results[0]["text"]

def test_build_context():
    embedding_model = EmbeddingModel()
    vector_store = VectorStore()
    retriever = Retriever(embedding_model, vector_store)

    results = [
        {
            "text": "RAG是一种检索增强生成技术",
            "score": 0.9
        },
        {
            "text": "Embedding可以将文本转换为向量",
            "score": 0.8
        }
    ]
    context = retriever.build_context(results)

    assert "[知识1]" in context
    assert "[知识2]" in context
    assert "RAG" in context
    assert "Embedding" in context