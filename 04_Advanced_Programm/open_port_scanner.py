import socket
import asyncio

IP = input("스캔할 IP 주소를 입력해주세요: ")
FIRST_PORT = 1
END_PORT = 65535

semaphore = asyncio.Semaphore(500)

open_ports = []

async def scan(ip, port):
    async with semaphore:
        try:
            future = asyncio.open_connection(ip, port)
            reader, writer = await asyncio.wait_for(future, timeout=0.5)
            
            print(f"[OPEN] 포트 {port}번 열려있음")
            
            banner = await reader.read(1024)
            print(f"{banner.decode().strip()}")

            await writer.close()
            await writer.wait_closed()
        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            pass

async def main():
    print(f"{IP}의 포트 {FIRST_PORT} ~ {END_PORT} 스캔 시작")

    tasks = []

    for port in range(FIRST_PORT, END_PORT+1):
        task = scan(IP, port)
        tasks.append(task)

    await asyncio.gather(*tasks)
    print("스캔 종료")

if __name__ == '__main__':
    asyncio.run(main())
