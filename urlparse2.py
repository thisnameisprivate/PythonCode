from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html#commit', scheme='https', allow_fragments=False)
print(result.scheme, '\n', result[0], '\n', result.netloc, '\n', result[1])