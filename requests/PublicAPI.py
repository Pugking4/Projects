import requests
import json

r = requests.get('https://api.publicapis.org/entries')

r.json()

with open('data.json', 'w') as f:
    json.dump(r.json(), f, indent=4)