import asyncio
import time
import random

TIMEOUT_TIME = 1

async def job(random_wait_time):
    print(f"work for {random_wait_time} seconds...")
    await asyncio.sleep(random_wait_time)
    print("done!!")

async def main():
    try:
        random_wait_time = random.uniform(0.0, 3.0)
        await asyncio.wait_for(job(random_wait_time), timeout=TIMEOUT_TIME)
    except asyncio.TimeoutError:
        print("you're fire!")
if __name__ == '__main__':
    asyncio.run(main())