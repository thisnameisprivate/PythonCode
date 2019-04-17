import urllib6.request
request = urllib6.request.Request('http://python.org')
response = urllib6.request.urlopen(request)
print(request.read().decode('utf-8'))