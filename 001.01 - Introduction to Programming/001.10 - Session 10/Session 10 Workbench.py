import json 

f = open("person.json")

personDict = json.loads(f.read())
print(personDict)

f.close()