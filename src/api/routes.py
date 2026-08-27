"""定义 /chat、/rag、/agent 等 API"""
import os
import tempfile
from functools import lru_cache
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from src.api.schemas import ChatRequest, ChatResponse, RAGRequest, RAGResponse, AgentRequest, AgentResponse, VisionResponse
from src.llm import ask_llm
from src.rag.knowledge_base import KnowledgeBase
from src.agent.agent import Agent
from src.multimodal.vision import VisionService, MockVisionProvider

router = APIRouter()

@lru_cache
def get_knowledge_base() -> KnowledgeBase:
    """
    延迟初始化知识库。
    第一次调用 /rag 时创建，后续复用。
    """
    return KnowledgeBase("data/test.txt")

@lru_cache
def get_agent() -> Agent:
    """创建并复用Agent"""
    return Agent()

@lru_cache
def get_vision_service() -> VisionService:
    """创建并复用 Vision Service"""
    return VisionService(MockVisionProvider())

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """普通AI聊天接口"""
    messages = [
        {
            "role": "user",
            "content": request.message
        }
    ]
    answer = ask_llm(messages)
    return ChatResponse(answer=answer)

@router.post("/rag", response_model=RAGResponse)
def rag_chat(request: RAGRequest):
    """RAG知识库问答接口"""
    knowledge_base = get_knowledge_base()
    answer = knowledge_base.ask(request.question, top_k=2)
    return RAGResponse(answer=answer)

@router.post("/agent", response_model=AgentResponse)
def agent_chat(request: AgentRequest):
    """Agent接口"""
    agent = get_agent()
    answer = agent.run(request.message)
    return AgentResponse(answer=answer)

@router.post("/vision", response_model=VisionResponse)
async def vision_chat(prompt: str = Form(...), image: UploadFile = File(...)):
    """图片理解接口"""
    suffix = os.path.splitext(image.filename or "")[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        content = await image.read()
        temp_file.write(content)
        temp_path = temp_file.name
    try:
        vision_service = get_vision_service()
        answer = vision_service.analyze_image(temp_path, prompt)
        return VisionResponse(answer=answer)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)