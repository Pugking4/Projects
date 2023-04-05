import requests
import json
import random

# specify endpoint
url = 'https://dog.ceo/api/breeds/image/random'

# specify parameters
params = {}

# make GET request
response = requests.get(url, params=params)

# load response content into a Python dictionary
data = json.loads(response.content)

# dump data into a JSON file
with open('dog_img.json', 'w') as f:
    json.dump(data, f, indent=4)
