import json

peopleNames = [
            {
                "ID": 1,
                "First Name": "Brad",
                "Last Name": "Brooks"
            },
            {
                "ID": 2,
                "First Name": "Ada",
                "Last Name": "Owens"
            }
        ]

peopleOther = [
            {
                "ID": 1,
                "Gender": "Male",
                "Age": 20,
                "Email": "b.brooks@randatmail.com"
            },
            {
                "ID": 2,
                "Gender": "Female",
                "Age": 21,
                "Email": "a.owens@randatmail.com"
            }
        ]

newPeopleNames = {}
for each in peopleNames:
    newPeopleNames[each['ID']] = each
newPeopleOther = {}
for each in peopleOther:
    newPeopleOther[each['ID']] = each

# Explained
'''
newPeopleMerged = {}
for each in peopleNames:
    newPeopleMerged[each['ID']] = {
                                    "ID": each['ID'],
                                    "First Name": each['First Name'],
                                    "Last Name": each['Last Name']
                                  }
'''

newPeopleMerged = {}
for each in peopleNames:
    newPeopleMerged[each['ID']] = each
    newPeopleMerged[each['ID']]['Gender'] = newPeopleOther[each['ID']]['Gender']
    newPeopleMerged[each['ID']]['Email'] = newPeopleOther[each['ID']]['Email']

print(json.dumps(newPeopleMerged, indent=3))
