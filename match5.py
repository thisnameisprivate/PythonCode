import re

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result.group().split(')'))
print(result.group().split(')')[1])