from config.settings import APP_NAME,VERSION

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

        print(f"AI > 你刚刚输入的是：{user_input}")

def main():
    print_banner()
    chat()

if __name__ == "__main__":
    main()