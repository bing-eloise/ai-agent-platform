"""统一登记项目有哪些 Tool"""
from src.tools.calculator import calculator
from src.tools.rag_tool import RAGTool
from src.rag.knowledge_base import KnowledgeBase

_rag_tool = None

def get_rag_tool() -> RAGTool:
    """延迟初始化 RAG Tool"""
    global _rag_tool
    if _rag_tool is None:
        knowledge_base = KnowledgeBase("data/test.txt")
        _rag_tool = RAGTool(knowledge_base)
    return _rag_tool

def rag_search(question: str) -> str:
    """查询本地知识库"""
    rag_tool = get_rag_tool()
    return rag_tool.query(question)

TOOL_REGISTRY = {
    "calculator": calculator,
    "rag_search": rag_search
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
    },
    {
        "type": "function",
        "function": {
            "name": "rag_search",
            "description": "查询项目本地知识库。当用户的问题需要根据项目知识库中的内容回答时使用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "需要查询知识库的问题"
                    }
                },
                "required": ["question"]
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