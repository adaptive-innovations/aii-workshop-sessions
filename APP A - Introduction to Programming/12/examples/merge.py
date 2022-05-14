import json

array1 = [
            {"ID":1,"First Name":"Brad","Last Name":"Brooks"},
            {"ID":2,"First Name":"Ada","Last Name":"Owens"},
            {"ID":3,"First Name":"Hailey","Last Name":"Hill"},
            {"ID":4,"First Name":"Alan","Last Name":"Chapman"}
         ]
array2 = [
            {"ID":1,"Gender":"Male","Age":20,"Email":"b.brooks@randatmail.com"},
            {"ID":2,"Gender":"Female","Age":21,"Email":"a.owens@randatmail.com"},
            {"ID":3,"Gender":"Female","Age":24,"Email":"h.hill@randatmail.com"},
            {"ID":4,"Gender":"Male","Age":19,"Email":"a.chapman@randatmail.com"}
         ]
array3 = []

# Iterate thrugh 1st dataset
for each in array1:
    rowDict = {}
    # Add from 1st array
    rowDict['ID'] = each['ID']
    rowDict['First Name'] = each['First Name']
    rowDict['Last Name'] = each['Last Name']
    array3.append(rowDict)

# Iterate through 2nd dataset 
for each2 in array2:
    # Find matching row in the new dataset
    for each3 in array3:
        if each2['ID'] == each3['ID']:
            # Update from 2nd array
            each3['Gender'] = each2['Gender']
            each3['Age'] = each2['Age']
            each3['Email'] = each2['Email']

print(json.dumps(array3, indent=4))