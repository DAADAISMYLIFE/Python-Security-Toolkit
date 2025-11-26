import asyncio
import socket

target_ip = '127.0.0.1'
start_port = 1
end_port = 65535

semaphore = asyncio.Semaphore(500)

async def scan_port(ip, port):
    async with semaphore:
        try:
            future = asyncio.open_connection(ip, port)

            reader, writer = await asyncio.wait_for(future, timeout=0.5)

            print(f"[OPEN] 포트 {port}번 열려있음")
            writer.close()
            await writer.wait_closed()

        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            pass

async def main():
    print(f"{target_ip}의 포트 {start_port} ~ {end_port} 스캔 시작")

    tasks = []

    for port in range(start_port, end_port + 1):
        task = scan_port(target_ip, port)
        tasks.append(task)

    await asyncio.gather(*tasks)
    print("스캔 완료")

if __name__ == '__main__':
    asyncio.run(main())
