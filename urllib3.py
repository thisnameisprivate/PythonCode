import urllib.request
request = urllib.request.Request('http://python.org')
response = urllib.request.urlopen(request)
print(request.read().decode('utf-8'))