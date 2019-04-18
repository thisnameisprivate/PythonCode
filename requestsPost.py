import requests

data = {'name': 'germey', 'age': 22}
result = requests.post('http://httpbin.org/post', data=data)
print(result.text)
print(type(result.text))
print(result.json())
print(result.json()['form'])
print(result.json()['headers'])