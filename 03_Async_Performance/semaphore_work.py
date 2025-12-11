import asyncio
import random
import time

semahpore = asyncio.Semaphore(100)

async def work(n, t):
    async with semahpore:
        await asyncio.sleep(t)
        print(f"{n} done!")

async def main():
    start_time = time.time()
    tasks = [work(i+1, random.random()) for i in range(10000)]

    await asyncio.gather(*tasks)
    end_time = time.time()

    print("Total Work time:", end_time - start_time)

if __name__ == '__main__':
    asyncio.run(main())
