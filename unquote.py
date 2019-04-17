from urllib.parse import unquote, quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print(unquote(url))