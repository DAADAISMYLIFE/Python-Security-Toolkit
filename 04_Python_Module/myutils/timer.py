from functools import wraps
import time

def measure(func):
    @wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"함수{func.__name__} 실행 시간: {end_time - start_time}")
    return wrapper

