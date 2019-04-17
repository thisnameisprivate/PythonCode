from urllib import request, parse

url = 'http://python.org/post'
headers = {
    'User-Agent': 'Monzilla/4.0 (compitable; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))