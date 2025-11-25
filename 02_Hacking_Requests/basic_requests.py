import requests

URL = "https://naver.com"

response = requests.get(URL)
print(response)
print(response.status_code)
print(response.text)