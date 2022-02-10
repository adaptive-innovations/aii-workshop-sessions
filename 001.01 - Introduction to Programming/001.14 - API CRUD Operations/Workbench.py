from email import header
from urllib import response
import requests
import json

# Go to https://crudcrud.com and get your URL
myCrudCrudURL = 'https://crudcrud.com/api/4efc5cf883b7402496de9c9dff8d4799'
thisProjectName = 'WorkshopSession14'
url = f"{myCrudCrudURL}/{thisProjectName}"
headers = {'Content-Type': 'application/json'}
print(url)

def createRecord(inputDict):
    payload = json.dumps(inputDict)
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code < 400:
        print('Success')
    else:
        print('Error!')

def readAllRecords():
    payload = ""
    response = requests.request("GET", url, headers=headers, data=payload)
    responseJSON = response.json()
    print(json.dumps(responseJSON, indent=4))

def readOneRecord(recordID):
    appendedUrl = f'{url}/{recordID}'
    payload = ""
    response = requests.request("GET", appendedUrl, headers=headers, data=payload)
    responseJSON = response.json()
    print(json.dumps(responseJSON, indent=4))

def updateRecord(recordID, inputDict):
    appendedUrl = f'{url}/{recordID}'
    payload = json.dumps(inputDict)
    response = requests.request("PUT", appendedUrl, headers=headers, data=payload)
    if response.status_code < 400:
        print(f'Success.')
    else:
        print('Error!')

def deleteRecord(recordID):
    appendedUrl = f'{url}/{recordID}'
    payload = ""
    response = requests.request("DELETE", appendedUrl, headers=headers, data=payload)
    if response.status_code < 400:
        print(f'Success.')
    else:
        print('Error!')


#newEmployee = {"name": "Bob Dole", "smell": "Glrious Freedom", "Age": 97}
#createRecord(newEmployee)
readAllRecords()
#readOneRecord('620487f038fd8d03e897344a')
#updateRecord('620487f038fd8d03e897344a', {"name": "Bob Dole", "smell": "Freedom", "Age": 55})
#deleteRecord('620487f038fd8d03e897344a')