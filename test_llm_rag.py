from src.llm import ask_llm

messages = [
    {
        "role": "user",
        "content": """
请只根据下面提供的资料回答问题。

资料：
Chunk Overlap 可以减少文本切分边界造成的上下文丢失。

问题：
Chunk Overlap 有什么作用？

如果资料中存在答案，请直接根据资料回答。
如果资料中确实不存在答案，再回答“无法回答”。
"""
    }
]

answer = ask_llm(messages)
print(answer)