"""定义 /chat、/rag、/agent 等 API"""
from fastapi import APIRouter
from src.api.schemas import ChatRequest, ChatResponse
from src.llm import ask_llm
from src.rag.knowledge_base import KnowledgeBase
from src.api.schemas import RAGRequest, RAGResponse
from src.agent.agent import Agent
from src.api.schemas import AgentRequest, AgentResponse

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