import re

content = '54aK54yr5oiR54ix5L2g'
#第一个参数为正则表达式
#第二个参数为替换后的字符串
#第三个参数为要替换的目标字符串
content = re.sub('\d+', ' ', content)
print(content.split(' '))