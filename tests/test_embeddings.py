from src.rag.embeddings import EmbeddingModel

def test_embed_text():
    model = EmbeddingModel()
    vector = model.embed_text("RAG是一种检索增强生成技术")
    assert isinstance(vector, list)
    assert len(vector) > 0
    assert isinstance(vector[0], float)

def test_embed_documents():
    model = EmbeddingModel()
    texts = ["RAG是一种检索增强生成技术", "Embedding可以将文本转换为向量"]
    vectors = model.embed_documents(texts)
    assert len(vectors) == 2
    assert len(vectors[0]) > 0