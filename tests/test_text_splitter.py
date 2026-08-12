from src.rag.text_splitter import split_text

def test_split_text():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chunks = split_text(text, chunk_size=10, chunk_overlap=2)
    assert len(chunks) > 1
    assert chunks[0] == "ABCDEFGHIJ"
    assert chunks[1].startswith("IJ")

def test_empty_text():
    chunks = split_text("")
    assert chunks == []