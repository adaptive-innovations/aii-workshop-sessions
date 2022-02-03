import json
import requests

method = "GET"
url = "https://www.boredapi.com/api/activity" 

headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)

print(response.text)