from src.rag.document_loader import load_text_file

def test_load_text_file():
    text = load_text_file("data/test.txt")
    assert isinstance(text, str)
    assert len(text) > 0
    assert "RAG" in text