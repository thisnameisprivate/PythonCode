from urllib.parse import parse_qs

query = 'name=germay&age=22'
print(parse_qs(query))