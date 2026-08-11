import time
from functools import wraps
from src.logger import logger

def retry(max_attempts=3, delay=1):
    """
    Retry装饰器
    :param max_attempts: 最大尝试次数
    :param delay: 初始等待时间
    """
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:

                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(
                        f"{func.__name__} failed "
                        f"attempt={attempt}: {str(e)}"
                    )
                    if attempt == max_attempts:
                        raise e

                    sleep_time = delay*(2**(attempt-1))
                    logger.info(f"Retry after {sleep_time}s")
                    time.sleep(sleep_time)

                    attempt += 1

        return wrapper

    return decorator