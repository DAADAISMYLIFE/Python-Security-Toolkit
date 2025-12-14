from functools import wraps
import time

def retry(max_retry=1, delay=0.1, exceptions=(Exception, )):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for i in range(max_retry+1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"예상한 에러 발생")
                    last_exception = e
                    if i < max_retry:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator



