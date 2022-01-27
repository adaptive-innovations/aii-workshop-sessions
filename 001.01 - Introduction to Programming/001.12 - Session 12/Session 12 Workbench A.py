myList = [
            {
                "Name": "Lewis",
                "Age": "Old",
                "Height": "Garganutan",
                "Smell": "Like elderly mule.",
                "type": "Milkdrinker"
            },
            {
                "Name": "Chris",
                "Age": "Spring Chicken",
                "Height": "Glorious",
                "Smell": "Like elderberries.",
                "type": "Whiskey"
            }
        ]

myDict = {
            "Lewis": {
                "Name": "Lewis",
                "Age": "Old",
                "Height": "Garganutan",
                "Smell": "Like elderly mule.",
                "type": "Milkdrinker"
            },
            "Chris": {
                "Name": "Chris",
                "Age": "Spring Chicken",
                "Height": "Glorious",
                "Smell": "Like elderberries.",
                "type": "Whiskey"
            }
        }

# Searching in a Dict
print(myDict['Lewis'])

# Searching in a List
for each in myList:
    if each['Name'] == 'Lewis':
        print(each)
