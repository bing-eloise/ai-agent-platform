from src.exceptions import (AIChatError, LLMError)

def test_llm_error():
    error = LLMError("LLM failed")
    assert isinstance(error, AIChatError)