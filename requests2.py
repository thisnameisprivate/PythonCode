import requests

#r = requests.get('http://httpbin.org/get')
#print(r.text)
data = {
    'name':'username',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(type(r.text))
print(r.text)
print(r.json())
print(type(r.json()))