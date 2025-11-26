import socket
import asyncio

clients = []

# 사용자 메시지 수신 및 처리
async def handle_client(reader, writer):
    clients.append(writer)
    addr = writer.get_extra_info('peername')
    print(f"새로운 접속이 확인되었습니다. {addr}")

    try:
        while True:
            data = await reader.read(1024)

            if not data: break
            
            message = data.decode('utf-8')
            print(f"[{addr}] {message}")
            
            for client_writer in clients:
                if client_writer == writer: continue
                try:
                    client_writer.write(data)
                    await client_writer.drain()
                except:
                    pass
    except asyncio.CancelledError:
        print(f"클라이언트 해제 오류")
    finally:
        print("유저가 한 명 떠났습니다.")
        if writer in clients:
            clients.remove(writer)
        writer.close()
        await writer.wait_closed()
    

# 서버 열고 기다리기
async def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8888

    server = await asyncio.start_server(handle_client, SERVER_HOST, SERVER_PORT)

    print(f"비동기 서버를 구동합니다. ({SERVER_HOST}:{SERVER_PORT})")
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
