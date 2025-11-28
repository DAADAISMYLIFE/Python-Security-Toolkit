import socket
import os
import time

SERVER_HOST = '127.0.0.1'
PORT = 9999


def main():
    file_path = input()
    
    try:
        with open(file_path, 'rb') as file:
            file_root, file_ext = os.path.splitext(file_path)
            file_name = os.path.basename(file_root)            

            if not file_ext: file_ext = '<NONE>'

            with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
                sock.connect((SERVER_HOST, PORT))

                send_data = f"{file_name} {file_ext}<END>"
                sock.send(send_data.encode('utf-8'))

                while True:
                    file_byte = file.read(1024)
                    if not file_byte: break
                    sock.send(file_byte)
                 
    except FileNotFoundError:
        print(f"File {file_path} does not exits")
 
    except Exception as e:
        print(f"Unexpected Exception: {e}")

if __name__ == '__main__':
    main()
