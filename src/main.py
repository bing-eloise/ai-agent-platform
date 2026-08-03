from config.settings import APP_NAME,VERSION
from src.llm import ask_llm_stream
from src.memory import ChatMemory
from src.logger import logger

def print_banner():
    """打印程序欢迎信息"""
    print("=" * 40)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 40)

def chat():

    memory = ChatMemory()
    """聊天循环"""
    while True:
        user_input = input("You > ")

        if user_input.lower() in ["exit", "quit"]:
            print("AI > Bye!")
            break

        memory.add_user_message(user_input)
        messages = memory.get_messages()

        logger.info(f"User request: {user_input}")

        answer = ""

        print("AI >", end="")

        for token in ask_llm_stream(messages):
            print(token, end="", flush=True)
            answer += token

        memory.add_assistant_message(answer)

        logger.info("LLM response success")
        print()

def main():
    print_banner()
    chat()

if __name__ == "__main__":
    main()