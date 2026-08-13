from src.rag.knowledge_base import KnowledgeBase

def test_knowledge_base_init():
    kb = KnowledgeBase("data/test.txt")
    assert len(kb.chunks) > 0
    assert kb.embedding_model is not None
    assert kb.vector_store is not None
    assert kb.retriever is not None
    assert kb.rag_service is not None