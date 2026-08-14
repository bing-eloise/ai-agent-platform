import os
from dotenv import load_dotenv
from openai import OpenAI
from src.exceptions import LLMError
from src.logger import logger
from src.utils.retry import retry

# 加载 .env
load_dotenv()

# 读取配置
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

# 创建客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

@retry(max_attempts=3, delay=1)
def ask_llm(messages: list) -> str:
    """调用大语言模型"""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"LLM request failed: {str(e)}")
        raise LLMError("LLM调用失败") from e

@retry(max_attempts=3, delay=1)
def ask_llm_stream(messages:list):
    """流式LLM调用"""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=True
        )
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield content
    except Exception as e:
        logger.error(f"LLM stream failed: {str(e)}")
        raise LLMError("LLM流式调用失败") from e

def ask_llm_with_tools(messages: list, tools: list):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        return response.choices[0].message
    except Exception as e:
        logger.error(f"LLM tool calling failed: {str(e)}")
        raise LLMError("LLM Tool Calling失败") from e