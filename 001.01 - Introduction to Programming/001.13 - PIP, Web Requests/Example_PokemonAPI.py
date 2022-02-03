import json
import requests



method = "GET"
#url = "https://pokeapi.co/api/v2/gender/1" # Female
url = "https://pokeapi.co/api/v2/gender/2" # Male 
#url = "https://pokeapi.co/api/v2/gender/3" # Genderless
headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)

# Get the response as text
responseJSON = response.json()

for each in responseJSON['pokemon_species_details']:
    print(each)
