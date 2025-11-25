import socket

HOST = "127.0.0.1"
PORT = 8080

# TODO: 서버 소켓 사용 순서
# 1. 소켓 생성
# 2. 소켓 바인딩
# 3. 클라이언트 소켓 리스닝
# 4. 클라이언트 연결 시도 시 Accept
# 5. 데이터 주고 받기
# 6. 클라이언트 종료 시 소켓 종료

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen()
    print(f"서버 {HOST}:{PORT}에서 클라이언트 대기 중...")

    while True:
        conn, addr = server_sock.accept()
        print(f"{addr}에서 접속했습니다.")

        data = conn.recv(1024)
        if not data: break

        print(f"{addr} : {data.decode('utf-8')}")
        conn.sendall(data)

    conn.close()
