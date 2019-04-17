from urllib.parse import urlunparse

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=c', 'coment']
result = urlunparse(data)
print(result)