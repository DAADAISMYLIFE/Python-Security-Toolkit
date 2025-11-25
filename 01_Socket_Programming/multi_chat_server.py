import socket
import threading

HOST = '127.0.0.1'
PORT = 8888

# 클라이언트 리스트
clients = []

# 사용자의 메시지를 처리
def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg: break
            broadcast(msg, client_socket)
        except Exception as e:
            break
    
    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)
    print("클라이언트가 한 명 떠났습니다.")


# 메시지를 전송한 클라이언트를 제외한 다른 사용자들에게 전달
def broadcast(msg, sender):
    for client in clients:
        if client == sender: continue
        try:
            client.send(msg)
        except:
            client.close()
            if client in clients:
                clients.remove(client)


if __name__ == '__main__':
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"채팅 서버를 시작합니다. ({HOST}:{PORT})")

    while True:
        conn, addr = server_socket.accept()
        clients.append(conn)
        print(f"새 클라이언트가 입장했습니다: {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, ))
        thread.start()