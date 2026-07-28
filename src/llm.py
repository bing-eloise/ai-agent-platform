import os

from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env
load_dotenv()

# 读取配置
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

# 创建客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def ask_llm(messages: list) -> str:
    """调用大语言模型"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content