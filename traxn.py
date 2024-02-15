import json
import requests

url = "https://tracxn.com/api/2.2/sandbox/companies"
headers = {
    'accesstoken': 'c638e63a-48fc-47cb-8c5b-9bf13fe28a1b',
    'cache-control': 'no-cache',
    'Content-Type': 'application/json'
}

data = '{"fliter":{"isFunded": true} }'

response = requests.post(url, headers=headers, data=data)
print(response.text)
# Save the response as a JSON file
# with open('response.json', 'w') as f:
#     json.dump(response.json(), f)
