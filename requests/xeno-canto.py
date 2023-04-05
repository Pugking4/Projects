import requests
import json
import random

# specify endpoint
url = 'https://xeno-canto.org/api/2/recordings'

# specify parameters
params = {'query': 'cnt:australia'}

# make GET request
response = requests.get(url, params=params)

#print(response.content)

# load response content into a Python dictionary
data = json.loads(response.content)

# dump data into a JSON file
#with open('xenocanto.json', 'w') as f:
#    json.dump(data, f, indent=4)

bird = random.choice(data['recordings'])

output = f"Common Name: {bird['en']}\nScientific Name: {bird['gen'].title()} {bird['sp'].lower()}\nLocation: {bird['loc']}\nDate Recorded: {bird['date']}\nRemark: {bird['rmk']}\n{bird['type'].title()}: {bird['file']}\nUrl: {bird['url']}"

print(output)