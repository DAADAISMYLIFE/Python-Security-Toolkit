import requests

# 세션 유지 X
print("세션을 유지하지 않고 requests 연결")
requests.get("https://httpbin.org/cookies/set/login/success")
res = requests.get("https://httpbin.org/cookies")
print(f"보유 쿠키: {res.json()}")

# 세션 유지하며 연결
print("세션을 유지하고 requests 연결")
session = requests.Session()
session.get("https://httpbin.org/cookies/set/login/success")
res = session.get("https://httpbin.org/cookies")
print(f"보유 쿠키: {res.json()}")
