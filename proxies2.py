import requests

proxies = {
    'http': 'socks6://user:password@host:port',
    'https': 'socks6://user:password@host:port'
}
requests.get("https://www.taobao.com", proxies=proxies)