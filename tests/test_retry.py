from src.utils.retry import retry

def test_retry_success():
    counter = {"count": 0}

    @retry(max_attempts=3, delay=0)
    def fake_api():
        counter["count"] += 1
        if counter["count"] < 3:
            raise Exception("temporary error")
        return "success"

    result = fake_api()

    assert result == "success"
    assert counter["count"] == 3