"""项目配置文件，所有全局配置统一放在这里。"""
import os
from dotenv import load_dotenv
from src.exceptions import ConfigError

load_dotenv()

APP_NAME = "AI Agent Platform"
VERSION = "1.0.0"
AUTHOR = "bing_eloise"
MAX_HISTORY = 10
MAX_TOKENS = 500

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

if not API_KEY:
    raise ConfigError("API_KEY is not configured")
if not BASE_URL:
    raise ConfigError("BASE_URL is not configured")
if not MODEL:
    raise ConfigError("MODEL is not configured")