import socket
import os

SERVER_HOST = '127.0.0.1'
PORT = 9999


def main():
    file_path = input()
    
    try:
        file_size = os.path.getsize(file_path)
        file = open(file_path, 'br')
        print(f"{file_path} size : {file_size}")
        
        try:
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.connect((SERVER_HOST, PORT))

            send_data = f"{file_path} {str(file_size)}"
    
            sock.send(send_data.encode('utf-8'))
            
            while True:
                file_byte = file.read(1024)
                sock.send(file_byte)

        except Exception as e:
            print(f"Unexpected Exception: {e}")
            file.close()
            sock.close()
    
    except FileNotFoundError:
        print(f"File {file_path} does not exits")
    
    finally:
        file.close()
        sock.close()

if __name__ == '__main__':
    main()
