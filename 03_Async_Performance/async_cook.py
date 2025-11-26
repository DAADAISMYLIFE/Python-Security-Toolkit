import time
import asyncio

async def cook_ramen(index):
    print(f"{index}번 라면: 물을 끓이기 시작합니다.. (다음 라면을 준비)")
    await asyncio.sleep(3)
    print(f"{index}번 라면: 완성되었습니다.")

async def main():
    start_time = time.time()

    print("---- 비동기식 방법----")
    
    await asyncio.gather(
        cook_ramen(1),
        cook_ramen(2),
        cook_ramen(3)
    )

    end_time = time.time()
    print(f"총 걸린 시간: {end_time - start_time}")

if __name__ == "__main__":
    asyncio.run(main())
