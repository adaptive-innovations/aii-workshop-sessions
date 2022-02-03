import requests

method = "GET"
url = "https://api.kanye.rest"
headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)