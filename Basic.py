import requests
from requests.auth import HTTPBasicAuth

result = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'), timeout=1)
print(result.status_code)

