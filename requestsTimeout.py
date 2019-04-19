import requests

result = requests.get("https://www.taobao.com", timeout=1)
print(result.status_code)