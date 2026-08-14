"""根据工具名称找到并执行对应 Tool"""
from src.tools.registry import get_tool

class ToolExecutor:
    """
    工具执行器
    负责：
    tool_name + arguments
        -> 查找工具
        -> 执行工具
        -> 返回结果
    """
    def execute(self, tool_name: str, arguments: dict):
        """执行指定工具"""
        if not tool_name:
            raise ValueError("tool_name cannot be empty")

        if not isinstance(arguments, dict):
            raise ValueError("arguments must be a dictionary")

        tool = get_tool(tool_name)
        result = tool(**arguments)
        return result