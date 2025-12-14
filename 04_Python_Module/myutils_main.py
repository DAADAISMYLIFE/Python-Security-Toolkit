from myutils import timer, retry
import time

@timer.measure
def work():
    print("일을 수행합니다.")
    time.sleep(0.5)
    print("일을 마칩니다.")

@retry.retry(max_retry=3, delay=0.3, exceptions=(ValueError,))
def unstable():
    print("asdf")
    raise ValueError

if __name__ == '__main__':
    work()

    unstable()





