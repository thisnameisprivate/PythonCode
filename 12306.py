import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


#import logging
#import requests
#logging.captureWarnings(True)
#response = requests.get('https://www.12306.cn', verify=False)
#print(response.status_code)


#import requests
#response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
#print(response.status_code)

###



























