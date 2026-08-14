import pytest
from src.tools.registry import (get_tool, list_tools)
from src.tools.registry import get_tool_schemas

def test_get_calculator():
    tool = get_tool("calculator")
    result = tool("multiply", 6, 7)
    assert result == 42

def test_list_tools():
    tools = list_tools()
    assert "calculator" in tools

def test_unknown_tool():
    with pytest.raises(ValueError):
        get_tool("unknown_tool")

def test_tool_schema():
    schemas = get_tool_schemas()
    assert len(schemas) > 0

    calculator_schema = schemas[0]
    assert calculator_schema["function"]["name"] == "calculator"

    parameters = calculator_schema["function"]["parameters"]["properties"]
    assert "operation" in parameters
    assert "a" in parameters
    assert "b" in parameters