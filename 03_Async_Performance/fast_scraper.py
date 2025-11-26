import aiohttp
import asyncio
import time


async def fetch(session, url, index):
    print(f"{index}번 요청 보냄")

    async with session.get(url) as response:
        text = await response.text()
        print(f"{index}번 요청 도착: 상태({response.status})")
        return text

async def main():
    url = 'https://httpbin.org/delay/1'
    count = 10

    print(f"{count}개의 사이트 동시 접속")
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(count):
            task = fetch(session, url, i+1)
            tasks.append(task)

        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"\n총 소요 시간 : {end_time - start_time}초")

if __name__ == "__main__":
    asyncio.run(main())
