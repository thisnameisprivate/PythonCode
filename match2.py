import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(type(result.group()))
print(result.group().split(' '))
print(result.group().split(' ')[1])
print(result.span())
print(type(result.group().split(' ')))


#result = re.math("^Hello.*Demo$", content)
#print(result.group())
#print(result.span())
#print(result.group(1))
#print(result.group(2))
#print(result.group(0))
#print(result.group().split(' '))
#print(type(result.group().split(' ')))


#result = re.match('^Hello.*?(\d+).*Deom$')
#print(result.group())
#print(result.span())
#print(result.group(1))
#print(result.group(2))
#print(result.group(3))
#pirnt(result.group().split(' '))
#print(type(result.group().split(' ')))