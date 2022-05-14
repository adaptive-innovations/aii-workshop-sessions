
import json 

class person():
    def __init__(self, ID):
        self.ID = 1
        self.FirstName = None
        self.LastName = None
        self.Gender = None
        self.Age = None
        self.Email = None

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
newDict = {}

for each in array1:
    thisPersonId = each['ID']
    # Generate Class instance for this person ID
    newDict[thisPersonId] = person(thisPersonId)
    # Update the Class instances with this dataset's values
    newDict[thisPersonId].FirstName = each['First Name']
    newDict[thisPersonId].LastName = each['Last Name']

for each in array2:
    thisPersonId = each['ID']
    # Update the Class instances with this dataset's values
    newDict[thisPersonId].Gender = each['Gender']
    newDict[thisPersonId].Age = each['Age']
    newDict[thisPersonId].Email = each['Email']

array3 = []
for each in newDict:
    array3.append(newDict[each].__dict__)

print(json.dumps(array3, indent=4))