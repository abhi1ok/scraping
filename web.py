import json
import requests

# Make a request
response = requests.get('https://github.com')

# Convert the response to JSON format
data = response.json()

# Now 'data' is a Python dictionary.
print(data)