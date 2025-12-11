import asyncio
import time

async def zzz(t):
    await asyncio.sleep(t)
    print(f"{t}sec completed!")

async def main():
    times = map(int, input("input: ").split())
    tasks = []
    start_time = time.time()
    print("output: ")
    for t in times:
        task = asyncio.create_task(zzz(t)) 
        tasks.append(task)
    
    await asyncio.gather(*tasks)

    end_time = time.time()

    print(f"total spent time: {end_time - start_time}")

if __name__ == '__main__':
    asyncio.run(main())