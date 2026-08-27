from src.tokenizer import estimate_tokens

def test_estimate_tokens():
    messages = [
        {
            "role": "user",
            "content": "你好"
        },
        {
            "role": "assistant",
            "content": "Hello"
        }
    ]
    tokens = estimate_tokens(messages)
    assert tokens == 7


def test_estimate_tokens_empty():
    assert estimate_tokens([]) == 0


def test_estimate_tokens_missing_content():
    messages = [
        {
            "role": "user"
        }
    ]
    assert estimate_tokens(messages) == 0