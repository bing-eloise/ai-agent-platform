from src.rag.knowledge_base import KnowledgeBase

kb = KnowledgeBase("data/test.txt")

question = "Chunk Overlap有什么作用？"
# question = "法国的首都是哪里？"

answer = kb.ask(question, top_k=2)

print("Question:")
print(question)
print("\nAnswer:")
print(answer)