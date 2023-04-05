import requests
import json
import random

# specify endpoint
url = 'https://cat-fact.herokuapp.com/facts'

# specify parameters
params = {'animal_type': 'cat', 'amount': 500}

# make GET request
response = requests.get(url, params=params)

# load response content into a Python dictionary
data = json.loads(response.content)

# dump data into a JSON file
with open('cat_facts.json', 'w') as f:
    json.dump(data, f, indent=4)

#print(data)
facts = []
# iterate over facts and print text values
for fact in data:
    #print(fact['text'])
    facts.append(fact['text'])

#choose random fact from facts
randfact = random.choice(facts)

print(randfact)