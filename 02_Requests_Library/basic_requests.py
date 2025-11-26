import requests

URL = "https://httpbin.org/"
END_POINT = "get"

response = requests.get(URL+END_POINT)

print(f"서버 응답 코드 : {response.status_code}")

if response.status_code == 200:
    print("접속 성공!")
    data = response.json()
    print(f"받은 데이터 : {data}")
    print(f"내 IP 주소 : {data['origin']}")
else:
    print("접속 실패!")

