"""定义 /chat、/rag、/agent 等 API"""
from fastapi import APIRouter, UploadFile, File, Form
from src.api.schemas import ChatRequest, ChatResponse
from src.llm import ask_llm
from src.rag.knowledge_base import KnowledgeBase
from src.api.schemas import RAGRequest, RAGResponse
from src.agent.agent import Agent
from src.api.schemas import AgentRequest, AgentResponse
import os
import tempfile
from src.multimodal.vision import VisionService, MockVisionProvider

router = APIRouter()
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

knowledge_base = KnowledgeBase("data/test.txt")
@router.post("/rag", response_model=RAGResponse)
def rag_chat(request: RAGRequest):
    """RAG知识库问答接口"""
    answer = knowledge_base.ask(request.question, top_k=2)
    return RAGResponse(answer=answer)

agent = Agent()
@router.post("/agent", response_model=AgentResponse)
def agent_chat(request: AgentRequest):
    """Agent接口"""
    answer = agent.run(request.message)
    return AgentResponse(answer=answer)

vision_service = VisionService(MockVisionProvider())
@router.post("/vision")
async def vision_chat(prompt: str = Form(...), image: UploadFile = File(...)):
    """图片理解接口"""
    suffix = os.path.splitext(image.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        content = await image.read()
        temp_file.write(content)
        temp_path = temp_file.name
    try:
        answer = vision_service.analyze_image(temp_path, prompt)
        return {"answer": answer}
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)