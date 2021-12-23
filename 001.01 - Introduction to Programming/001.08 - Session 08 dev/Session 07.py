'''
We're getting address data from www.geoapify.com
Copy the url and paste into your browser...
(Note the "text=" value in the URL):
https://api.geoapify.com/v1/geocode/autocomplete?apiKey=6e1658c097204e148523a63d73061c3b&text=93314

'''
import json
import requests

def autocompleteAddress(searchText):
    apiKey = "6e1658c097204e148523a63d73061c3b"
    url = "https://api.geoapify.com/v1/geocode/autocomplete?apiKey="+apiKey+"&text="+searchText
    response = requests.request("GET", url, headers={}, data={}, allow_redirects=False)
    responseDict = response.json()
    resultAddress = responseDict['features'][0]['properties']['formatted']
    return json.dumps(resultAddress, indent=4)

entry = ""
while True == True:
    try: 
        entry = input("Address Search: ")
        if entry == 'exit':
            break
        searchResult = autocompleteAddress(entry)
        print(searchResult)
    except: 
        print("Error!")