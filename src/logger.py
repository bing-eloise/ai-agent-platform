import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("AI_Agent_Platform")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)