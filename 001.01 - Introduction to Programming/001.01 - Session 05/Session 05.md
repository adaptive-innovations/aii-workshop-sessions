# APP A: Introduction to Programming
## Session 05

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)     |

## Last Week's Challenge

## Dealing with JSON
TRY, EXCEPT
```py
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

# cast dict as JSON
x = json.dumps(theFamily)
```


## Challenge
Create a JSON object which describes a cooking recipe.
Use the following structure as a general guideline:
```json
{
  "Title": "Best Chocolate Chip Cookies",
  "Time Required": "1 Hour",
  "Servings": "24",
  "Ingredients": [
    {
      "ingredient": "butter",
      "qty": "1/4 cup"
    },
    {
      "ingredient": "flour",
      "qty": "4 cups"
    }
  ],
  "Steps": [
    "Do this do that!",
    "Mix in a bowl.",
    "Bake for 5 minutes at 350F"
  ]
}
```