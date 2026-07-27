from config.settings import APP_NAME,VERSION
from src.llm import ask_llm

def print_banner():
    """打印程序欢迎信息"""
    print("=" * 40)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 40)

def chat():
    """简单聊天循环"""
    while True:
        user_input = input("You > ")

        if user_input.lower() in ["exit", "quit"]:
            print("AI > Bye!")
            break

        answer = ask_llm(user_input)

        print(f"AI > {answer}")

def main():
    print_banner()
    chat()

if __name__ == "__main__":
    main()