import json
from src.llm import ask_llm_with_tools
from src.tools.registry import get_tool_schemas

messages = [
    {
        "role": "user",
        "content": "计算128乘以37"
    }
]

tools = get_tool_schemas()
message = ask_llm_with_tools(messages, tools)

print("Content:")
print(message.content)

print("\nTool Calls:")
print(message.tool_calls)

if message.tool_calls:
    for tool_call in message.tool_calls:
        print("\nTool Name:")
        print(tool_call.function.name)

        print("\nArguments:")
        print(tool_call.function.arguments)

        arguments = json.loads(tool_call.function.arguments)
        print("\nParsed Arguments:")
        print(arguments)