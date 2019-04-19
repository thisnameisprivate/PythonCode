import requests

result = requests.Session()
result.get('http://httpbin.org/cookies/set/number/123456789')
r = result.get('http://httpbin.org/cookies')
print(r.text)
print(type(r.json()))
print(r.json())
print(r.json()['cookies']['number'])