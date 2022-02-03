import json
import requests



method = "GET"
# Example: https://api.funtranslations.com/translate/pirate.json?text=This is the best day of my life!
url = "https://api.funtranslations.com/translate/pirate.json?text=" 
textToTranslate = input("Please enter some text to translate into Pirate speak: ")
url = url + textToTranslate

headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)

responseJSON = response.json()

print(responseJSON['contents']['translated'])
