"""统一登记项目有哪些 Tool"""
from src.tools.calculator import calculator

TOOL_REGISTRY = {
    "calculator": calculator
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "执行基础数学运算，包括加法、减法、乘法和除法。",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "需要执行的数学运算"
                    },
                    "a": {
                        "type": "number",
                        "description": "第一个数字"
                    },
                    "b": {
                        "type": "number",
                        "description": "第二个数字"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        }
    }
]

def get_tool(tool_name: str):
    """根据工具名称获取对应工具函数"""
    tool = TOOL_REGISTRY.get(tool_name)
    if tool is None:
        raise ValueError(f"tool not found: {tool_name}")
    return tool

def list_tools() -> list[str]:
    """返回当前所有已注册工具名称"""
    return list(TOOL_REGISTRY.keys())

def get_tool_schemas() -> list[dict]:
    """返回所有工具Schema    供LLM Tool Calling使用"""
    return TOOL_SCHEMAS