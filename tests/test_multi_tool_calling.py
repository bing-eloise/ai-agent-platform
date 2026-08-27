from src.llm import ask_llm_with_tools
from src.tools.registry import get_tool_schemas

def check_tool_selection(question: str):
    messages = [
        {
            "role": "user",
            "content": question
        }
    ]
    tools = get_tool_schemas()
    message = ask_llm_with_tools(messages, tools)

    print("\nQuestion:")
    print(question)

    print("\nContent:")
    print(message.content)

    print("\nTool Calls:")
    print(message.tool_calls)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            print("Selected Tool:", tool_call.function.name)

def test_calculator_selection():
    check_tool_selection("请计算128乘以37")

def test_rag_selection():
    check_tool_selection("Chunk Overlap有什么作用？请查询项目知识库。")


def test_no_tool_selection():
    check_tool_selection("你好，请简单介绍一下你自己。")