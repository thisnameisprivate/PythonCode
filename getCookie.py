import http.cookiejar, urllib.request
#保存https://baidu.com cookie 到当前文件夹cookie.txt file
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)
cookie.save(ignore_discard=True, ignore_expires=True)