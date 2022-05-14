import requests

method = "GET"
url = "https://api.kanye.rest"
headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)

# Get the response as text
responseStr = response.text
responseJSON = response.json()

print(responseStr)