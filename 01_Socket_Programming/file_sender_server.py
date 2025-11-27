import socket

HOST = '0.0.0.0'
PORT = 9999


def main():
    try:
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        sock.bind((HOST, PORT))

        sock.listen()
        print("클라이언트를 기다리는 중...")

        conn, addr = sock.accept()
        print("클라이언트 연결됨.")
    
        # 파일 전체 크기 받기
        data = conn.recv(1024)
        delimiter = b"<END>"
        
        if delimiter in data:
            header, body_chunk = data.split(delimiter, 1)


            file_info = header.decode('utf-8')
            filename, filesize = file_info.split()
            print(f"file_info: {filename} {filesize}")
        
            file = open("copied"+filename, "wb")
            file.write(body_chunk)

            while True:
                file_byte = conn.recv(1024)
                if not file_byte: break
                file.write(file_byte) 
            file.close()
        sock.close()

    except Exception as e:
        print(f"Unexpected Exception: {e}")
        file.close()
        sock.close()

if __name__ == '__main__':
    main()

