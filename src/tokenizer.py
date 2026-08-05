""" Token统计工具 """
def estimate_tokens(messages):
    """
    粗略估算token数量
    中文：一个字约等于 1-2 token
    英文：一个单词约等于 1 token
    """
    total = 0
    for message in messages:
        content = message.get("content", "")
        total += len(content)
    return total