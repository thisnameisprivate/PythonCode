import requests
result = requests.get('https://www.baidu.com')
print(result.cookies)
for key, value in result.cookies.items():
    print(key + '=' + value)
    
    
    
