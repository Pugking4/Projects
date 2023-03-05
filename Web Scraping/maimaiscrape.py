import requests

cookies = {
    'clal': '0zty47vrrd28kjktfov70av49o3510idhukgkzwmb4zi5mo03m566n31n7gg4kmw',
    'JSESSIONID': 'D8A4BFEFEDC6D4ED95604F281BD81094.pay_lng01',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://lng-tgk-aime-gw.am-all.net',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/&back_url=https://maimai.sega.com/',
    # 'Cookie': 'clal=0zty47vrrd28kjktfov70av49o3510idhukgkzwmb4zi5mo03m566n31n7gg4kmw; JSESSIONID=D8A4BFEFEDC6D4ED95604F281BD81094.pay_lng01',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

data = {
    'retention': '1',
    'sid': 'pugking4',
    'password': 'Cocothe4th00',
}

response = requests.post('https://lng-tgk-aime-gw.am-all.net/common_auth/login/sid/', cookies=cookies, headers=headers, data=data)