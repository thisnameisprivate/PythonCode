import requests

result = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(result.content)