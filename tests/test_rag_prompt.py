from src.prompt import build_rag_prompt

def test_build_rag_prompt():
    context = """
    [知识1]
    Embedding可以把文本转换成向量。
    """
    question = "Embedding有什么作用？"
    prompt = build_rag_prompt(context, question)

    assert context in prompt
    assert question in prompt
    assert "知识库" in prompt