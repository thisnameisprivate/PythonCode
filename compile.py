import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result4 = re.sub(pattern, '', content1)
result5 = re.sub(pattern, '', content2)
result6 = re.sub(pattern, '', content3)
print(result4)
print(result5)
print(result6)
#print(result4, result5, result6)