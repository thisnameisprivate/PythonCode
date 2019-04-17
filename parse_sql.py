from urllib.parse import parse_sql

query = 'name=gream&age=22'
print(parse_sql(query))