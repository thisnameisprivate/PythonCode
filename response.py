import requests

result = requests.get('http://www.jianshu.com')
exit() if not result.status_code == requests.codes.ok else print('Request Successfully')



# print(type(result.status_code), result.status_code)
# print(type(result.headers), result.headers)
# print(type(result.cookies), result.cookies)
# print(type(result.url), result.url)
# print(type(result.history), result.history)