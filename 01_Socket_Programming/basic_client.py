import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

# TODO: 클라이언트 소켓 사용 순서
# 1. 소켓 생성
# 2. 서버 주소로 연결
# 3. 서버 접속 성공
# 4. 데이터 주고 받기
# 6. 소켓 종료

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as client_sock:
    client_sock.connect((SERVER_HOST, SERVER_PORT))
    
    client_sock.sendall("클라이언트 입니다!".encode('utf-8'))
    data = client_sock.recv(1024)
    print("서버 :", data.decode('utf-8'))
