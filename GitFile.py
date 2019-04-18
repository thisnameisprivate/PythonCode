import requests
files = {'file': open('favicon.ico', 'rb')}
result = requests.post('http://httpbin.org/post', files=files)
print(result.text)