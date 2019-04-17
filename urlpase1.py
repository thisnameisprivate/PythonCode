from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#commit')
print(type(result), result)