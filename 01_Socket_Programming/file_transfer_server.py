import socket
import os

HOST = '0.0.0.0'
PORT = 9999
BASE_STORAGE = './received_files/'

def main():
    
    os.makedirs(BASE_STORAGE, exist_ok=True)
    
    try:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))

            sock.listen()
            print("클라이언트를 기다리는 중...")

            while True:
                conn, addr = sock.accept()
                print("클라이언트 연결됨.")
        
                # 파일 전체 크기 받기
                data = conn.recv(1024)
                delimiter = b"<END>"
                
                if delimiter in data:
                    header, body_chunk = data.split(delimiter, 1)

                    file_info = header.decode('utf-8')
                    filename, filext = file_info.split()
                    if filext == '<NONE>': filext=''
                    print(f"file_info: {filename}{filext}")
                                
                    with open(BASE_STORAGE+"copied_"+filename+filext, "wb") as file:
                        file.write(body_chunk)

                        while True:
                            file_byte = conn.recv(1024)
                            if not file_byte: break
                            file.write(file_byte) 

    except Exception as e:
        print(f"Unexpected Exception: {e}")

if __name__ == '__main__':
    main()

