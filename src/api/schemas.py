"""定义请求和响应的数据结构"""
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    """AI聊天请求"""
    message: str = Field(
        ...,
        min_length=1,
        description="用户输入的消息"
    )

class ChatResponse(BaseModel):
    """AI聊天响应"""
    answer: str


class RAGRequest(BaseModel):
    """RAG知识库问答请求"""
    question: str = Field(
        ...,
        min_length=1,
        description="用户知识库问题"
    )

class RAGResponse(BaseModel):
    """RAG知识库问答响应"""
    answer: str


class AgentRequest(BaseModel):
    """Agent请求"""
    message: str = Field(
        ...,
        min_length=1,
        description="用户发送给Agent的消息"
    )

class AgentResponse(BaseModel):
    """Agent响应"""
    answer: str

class VisionResponse(BaseModel):
    """Vision响应"""
    answer: str