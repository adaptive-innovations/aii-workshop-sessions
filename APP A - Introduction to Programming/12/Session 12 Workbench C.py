import json

person = {'ID': 1, 'First Name': 'Brad', 'Last Name': 'Brooks', 'Gender': 'Male', 'Age': 20, 'Email': 'b.brooks@randatmail.com'}
print('object:')
print(json.dumps(person, indent=4))

# Give me the keys
print("==================")
print('keys:')
for each in person.keys():
    print(each)
print("==================")

# Give me the values
print("==================")
print('values:')
for each in person.values():
    print(each)
print("==================")

# Give me the items as a tuple with 2 items
print("==================")
print('items:')
for each in person.items():
    key = each[0]
    value = each[1]
    print(each)
    print(f'{key=}') # key
    print(f'{value=}') # value
print("==================")