"""控制完整 Agent 流程"""
import json
from src.llm import ask_llm_with_tools
from src.tools.registry import get_tool_schemas
from src.agent.executor import ToolExecutor

class Agent:
    """
     基础Tool Calling Agent
    负责：
        User
          -> LLM
          -> Tool Call
          -> Tool Executor
          -> Tool Result
          -> LLM
          -> Final Answer
    """
    def __init__(self):
        self.executor = ToolExecutor()
        self.tools = get_tool_schemas()

    def run(self, user_input: str) -> str:
        if not user_input:
            raise ValueError("user_input cannot be empty")

        messages = [
            {
                "role": "user",
                "content": user_input
            }
        ]

        # 第一次调用LLM：
        assistant_message = ask_llm_with_tools(messages, self.tools)
        if not assistant_message.tool_calls:
            return assistant_message.content

        messages.append(assistant_message)
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            result = self.executor.execute(tool_name, arguments)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

        # 第二次调用LLM
        final_message = ask_llm_with_tools(messages, self.tools)
        return final_message.content