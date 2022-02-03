import json
import requests

method = "GET"
url = "https://pokeapi.co/api/v2/gender/1"
headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)

# Get the response as text
responseJSON = response.json()

print(json.dumps(responseJSON, indent=4))