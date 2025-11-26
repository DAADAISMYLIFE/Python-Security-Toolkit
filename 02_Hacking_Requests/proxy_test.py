import requests

# 127.0.0.1:8080으로 동작하는 프록시 프로그램이 작동중이어야 합니다.

proxies = {
    "http" : "http://127.0.0.1:8080",        
    "https" : "http://127.0.0.1:8080",        
}

print("프록시를 통해 접속 중...")

try:
    res = requests.get("https://httpbin.org/ip", proxies=proxies, verify=False)

    print(f"상태 코드 : {res.status_code}")
    print(f"응답 내용 : {res.text}")
except Exception as e:
    print("접속 실패")
    print(f"에러 내용 : {e}")
