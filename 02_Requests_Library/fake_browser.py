import requests

URL = "https://httpbin.org/"
END_POINT = "headers"

# 헤더 수정없이 진행
print(f"User-Agent 수정없이 진행")
res1 = requests.get(URL+END_POINT)
print(res1.json()['headers']['User-Agent'])

# 헤더 수정
print(f"실제 나의 User-Agent로 수정하여 진행")
headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
        }
res2 = requests.get(URL+END_POINT, headers = headers)

print(res2.json()['headers']['User-Agent'])

if "Chrome" in res2.json()['headers']['User-Agent']:
    print("서버는 Chrome으로 인식함")
