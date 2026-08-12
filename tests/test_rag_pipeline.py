from src.rag.document_loader import load_text_file
from src.rag.text_splitter import split_text
from src.rag.embeddings import EmbeddingModel
from src.rag.vector_store import VectorStore

def test_rag_retrieval_pipeline():
    # 1. 读取文档
    text = load_text_file("data/test.txt")

    # 2. 文本切分
    chunks = split_text(text, chunk_size=150, chunk_overlap=30)
    assert len(chunks) > 1

    # 3. Chunk生成Embedding
    model = EmbeddingModel()
    vectors = model.embed_documents(chunks)
    assert len(vectors) == len(chunks)

    # 4. 存入Vector Store
    store = VectorStore()
    store.add(chunks, vectors)
    query = "为什么文档需要进行Chunk切分？"
    query_vector = model.embed_text(query)
    results = store.search(query_vector, top_k=2)
    assert len(results) == 2

    # 5. 检查是否检索到了相关内容
    retrieved_text = " ".join(
        result["text"]
        for result in results
    )
    assert ("Chunk" in retrieved_text or "切分" in retrieved_text)