import pytest
from src.agent.executor import ToolExecutor

def test_execute_calculator():
    executor = ToolExecutor()
    result = executor.execute(
        "calculator",
        {
            "operation": "multiply",
            "a": 128,
            "b": 37
        }
    )
    assert result == 4736

def test_execute_unknown_tool():
    executor = ToolExecutor()
    with pytest.raises(ValueError):
        executor.execute("unknown_tool", {})

def test_invalid_arguments():
    executor = ToolExecutor()
    with pytest.raises(ValueError):
        executor.execute("calculator", "invalid arguments")