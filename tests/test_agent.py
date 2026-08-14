from unittest.mock import patch, MagicMock
from src.agent.agent import Agent
import pytest

def test_agent_with_tool_call():
    agent = Agent()
    # 第一次LLM响应：要求调用calculator
    first_message = MagicMock()
    first_message.content = None

    tool_call = MagicMock()
    tool_call.id = "call_test_001"
    tool_call.function.name = "calculator"
    tool_call.function.arguments = ('{"operation": "multiply", "a": 128, "b": 37}')

    first_message.tool_calls = [tool_call]

    # 第二次LLM响应：根据工具结果生成最终答案
    final_message = MagicMock()
    final_message.content = ("128乘以37等于4736。")
    final_message.tool_calls = None

    with patch(
        "src.agent.agent.ask_llm_with_tools",
        side_effect=[first_message, final_message]
    ) as mock_llm:
        answer = agent.run("请帮我计算128乘以37")

        assert "4736" in answer
        assert mock_llm.call_count == 2

def test_agent_without_tool_call():
    agent = Agent()
    message = MagicMock()
    message.content = "Python是一种编程语言。"
    message.tool_calls = None

    with patch(
        "src.agent.agent.ask_llm_with_tools",
        return_value=message
    ) as mock_llm:
        answer = agent.run("请用一句话介绍Python")

        assert "Python" in answer
        # 普通问题只调用一次LLM
        assert mock_llm.call_count == 1

def test_agent_empty_input():
    agent = Agent()
    with pytest.raises(ValueError):
        agent.run("")