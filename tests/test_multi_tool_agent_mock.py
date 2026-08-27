from unittest.mock import MagicMock, patch
from src.agent.agent import Agent

def test_multi_tool_agent_calculator():
    agent = Agent()

    first_message = MagicMock()
    first_message.content = None

    tool_call = MagicMock()
    tool_call.id = "call_calc_001"
    tool_call.function.name = "calculator"
    tool_call.function.arguments = '{"operation": "multiply", "a": 128, "b": 37}'

    first_message.tool_calls = [tool_call]

    final_message = MagicMock()
    final_message.content = "128乘以37等于4736。"
    final_message.tool_calls = None

    with patch(
        "src.agent.agent.ask_llm_with_tools",
        side_effect=[first_message, final_message]
    ) as mock_llm:
        answer = agent.run("请计算128乘以37")

    assert "4736" in answer
    assert mock_llm.call_count == 2


def test_multi_tool_agent_rag():
    agent = Agent()

    first_message = MagicMock()
    first_message.content = None

    tool_call = MagicMock()
    tool_call.id = "call_rag_001"
    tool_call.function.name = "rag_search"
    tool_call.function.arguments = '{"question": "Chunk Overlap有什么作用？"}'

    first_message.tool_calls = [tool_call]

    final_message = MagicMock()
    final_message.content = "Chunk Overlap可以减少文本切分边界造成的上下文丢失。"
    final_message.tool_calls = None

    with patch(
        "src.agent.agent.ask_llm_with_tools",
        side_effect=[first_message, final_message]
    ) as mock_llm:
        with patch.object(
                agent.executor,
                "execute",
                return_value= "Chunk Overlap可以减少文本切分边界造成的上下文丢失。"
        ) as mock_execute:
            answer = agent.run("Chunk Overlap有什么作用？")

    assert "上下文丢失" in answer
    mock_execute.assert_called_once_with(
        "rag_search",
        {
            "question": "Chunk Overlap有什么作用？"
        }
    )
    assert mock_llm.call_count == 2


def test_multi_tool_agent_direct_answer():
    agent = Agent()

    message = MagicMock()
    message.content = "你好，我是AI助手。"
    message.tool_calls = None

    with patch(
        "src.agent.agent.ask_llm_with_tools",
        return_value=message
    ) as mock_llm:
        answer = agent.run("你好")

    assert "AI助手" in answer
    assert mock_llm.call_count == 1