import json

array1 = [
            {"ID":1,"First Name":"Brad","Last Name":"Brooks","Gender":"Male","Age":20,"Email":"b.brooks@randatmail.com"},
            {"ID":2,"First Name":"Ada","Last Name":"Owens","Gender":"Female","Age":21,"Email":"a.owens@randatmail.com"}
         ]
array2 = [
            {"ID":3,"First Name":"Hailey","Last Name":"Hill","Gender":"Female","Age":24,"Email":"h.hill@randatmail.com"},
            {"ID":4,"First Name":"Alan","Last Name":"Chapman","Gender":"Male","Age":19,"Email":"a.chapman@randatmail.com"}
         ]

# Append array1 & array2 together as array3
array3 = []
for each in array1:
    array3.append(each)
for each in array2:
    array3.append(each)

print(json.dumps(array3, indent=4))