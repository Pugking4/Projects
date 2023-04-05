import json

# Convert a Python dictionary to a JSON string
data = {"name": "John Doe", "age": 30, "isStudent": False}
json_string = json.dumps(data)
print(json_string)

# Convert a JSON string to a Python dictionary
json_string = '{"name": "John Doe", "age": 30, "isStudent": false}'
data = json.loads(json_string)
print(data)