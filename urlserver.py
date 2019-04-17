import urllib.request

response = urllib.request.urlopen('http://www.ptyhon.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Servers'))