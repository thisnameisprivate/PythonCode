import urlsocket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, urlsocket.timeout):
        print('TIME OUT')
