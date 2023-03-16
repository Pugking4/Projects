import requests

url = "http://localhost:5000/secret"
params = {"key": "verysecretkey"}

response = requests.get(url, params=params)
print(response.text)
