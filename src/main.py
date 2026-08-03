from config.settings import APP_NAME,VERSION
from src.llm import ask_llm_stream
from src.memory import ChatMemory
from src.logger import logger
from src.prompt import get_prompt

def print_banner():
    """打印程序欢迎信息"""
    print("=" * 40)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 40)

def chat():

    memory = ChatMemory()

    print("""
    请选择助手类型：
    
    1. 普通助手
    2. 编程助手
    3. 科研助手
    """)
    choice = input("请输入：")
    role_map = {
        "1": "default",
        "2": "coding",
        "3": "research"
    }
    role = role_map.get(choice, "default")
    print(f"当前模式： {role}")

    """聊天循环"""
    while True:
        user_input = input("You > ")

        if user_input.lower() in ["exit", "quit"]:
            print("AI > Bye!")
            break

        memory.add_user_message(user_input)
        messages = [{"role":"system", "content":get_prompt(role)}]
        messages.extend(memory.get_messages())

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