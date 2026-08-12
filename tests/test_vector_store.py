from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore

def test_vector_search():
    model = EmbeddingModel()
    documents = [
        "RAG是一种检索增强生成技术",
        "Python是一种编程语言",
        "Embedding可以将文本转换为向量"
    ]
    vectors = model.embed_documents(documents)

    store = VectorStore()
    store.add(documents, vectors)
    query = "什么技术可以把文本转换成向量？"
    query_vector = model.embed_text(query)
    results = store.search(query_vector, top_k=1)

    assert len(results) == 1
    assert "Embedding" in results[0]["text"]
    assert isinstance(results[0]["score"], float)