# Create a dictionary
thisdict =  {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964,
                "price": "$5,000"
            }

# Read a key's value
print(thisdict['model'])

# Modify a key's value
thisdict['model'] = "F-150"
print(thisdict)

# Add a key value pair
thisdict['title'] = "Clean"
print(thisdict)

# Delete an item
del thisdict['price']
print(thisdict)

# Add a list
theFamily = {
                "dad": "Dick",
                "mom": "Jane",
                "kids": ["Timmy", "Billy", "Sally-Mae", "Sally-Anne"]
            }
print(theFamily)

# Select a list item
print(theFamily['kids'][2])

# Iterate through a nested list
for kid in theFamily['kids']:
    print(kid)