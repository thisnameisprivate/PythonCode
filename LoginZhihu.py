import requests

headers = {
    'Cookie': '_zap=4ac14348-b3e5-4b80-bbe4-7f491df07516; __DAYU_PP=rIbaMnN3mbaqv7eEuqE62e4773440a1a; __utmv=51854390.100-1|2=registration_date=20170331=1^3=entry_date=20170331=1; d_c0="AHAgi9rQiw2PTh-K1h2HtlzhKYGaEI_XJMo=|1525501181"; _ga=GA1.2.282996726.1522142700; _xsrf=Gy0LynMKsdJL4Z5THvDwPehq6yjOLVEW; __gads=ID=31399405cac724a0:T=1539734587:S=ALNI_MYLc52ttS12LksiYVv_nfuZqEO6sA; tst=r; __utmz=51854390.1549902519.15.15.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/19716589; z_c0="2|1:0|10:1552443169|4:z_c0|92:Mi4xRE5tU0JBQUFBQUFBY0NDTDJ0Q0xEU1lBQUFCZ0FsVk5JYlYxWFFCcjBDWE5KVWQ4aTRUS1Vfdm55VEs2b2RSX3pR|d703e867ead91b76ab2f6896955d82876f0090048bc01866704f877100cecd6c"; __utma=51854390.282996726.1522142700.1549902519.1554017614.16; q_c1=f2ff0330f7424a98b84bc6e0b5701ec7|1554855839000|1520999275000; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
result = requests.get('https://www.zhihu.com', headers=headers)
print(result.text)