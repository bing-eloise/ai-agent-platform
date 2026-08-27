"""创建 FastAPI Application"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.api.routes import router
from src.exceptions import AIChatError, LLMError
from src.logger import logger
from config.settings import APP_NAME, VERSION

app = FastAPI(
    title=f"{APP_NAME} API",
    version=VERSION,
    description="AI Chat / RAG / Multi-Tool Agent / Multimodal API Service"
)

@app.get("/health")
def health_check():
    """API健康检查"""
    return {"status": "OK"}

app.include_router(router)

@app.exception_handler(LLMError)
async def llm_error_handler(request: Request, exc: LLMError):
    """LLM相关异常处理"""
    logger.error(f"LLM API error: {str(exc)}")
    return JSONResponse(
        status_code=503,
        content={
            "error": "LLM_SERVICE_ERROR",
            "message": "AI服务暂时不可用，请稍后重试。"
        }
    )

@app.exception_handler(AIChatError)
async def ai_chat_error_handler(request: Request, exc: AIChatError):
    """项目自定义异常统一处理"""
    logger.error(f"Application error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "AI_CHAT_ERROR",
            "message": str(exc)
        }
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """未预期异常统一处理"""
    logger.exception(f"Unexpected API error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "服务器内部错误。"
        }
    )