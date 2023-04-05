import requests
import json
import random

# specify endpoint
url = 'https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/&back_url=https://maimai.sega.com/'
# specify parameters
params = {}

# make GET request
response = requests.get(url, params=params)

print(response.text)
'''
# load response content into a Python dictionary
data = json.loads(response.content)

# dump data into a JSON file
with open('maimai.json', 'w') as f:
    json.dump(data, f, indent=4)
'''