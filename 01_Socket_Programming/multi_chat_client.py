import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8888

# 서버의 메시지를 처리
def receive_message(sock):
    while True:
        try:
            msg = sock.recv(1024)
            print(f"\n상대방: {msg.decode('utf-8')}")
        except Exception as e:
            print("연결이 종료되었습니다.")
            break
    sock.close()

if __name__ == '__main__':
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((SERVER_HOST, SERVER_PORT))

    print(f"채팅 서버에 접속했습니다. ({SERVER_HOST}:{SERVER_PORT})")

    thread = threading.Thread(target=receive_message, args=(sock, ), daemon=True)
    thread.start()

    while True:
        try:
            msg = input()
            if msg == "quit":
                break
            sock.send(msg.encode('utf-8'))
        except:
            break
        
    sock.close()