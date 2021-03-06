# Import the JSON module
import json

# Create a dictionary
theFamily = {
    "dad": {
      "name": {
        "first": "Bob",
        "middle": "Joseph",
        "last": "Dole"
      },
      "age": 98
    },
    "mom": {
      "name": {
        "first": "Jane",
        "middle": "Sally",
        "last": "Dole"
      },
      "age": 96
    },
    "kids": [
      {
        "name": {
          "first": "Bill",
          "middle": "Robert",
          "last": "Dole"
        },
        "age": 46
      },
      {
        "name": {
          "first": "Bobby",
          "middle": "Shaq",
          "last": "Dole"
        },
        "age": 44
      },
      {
        "name": {
          "first": "Jill",
          "middle": "Sally-Mae",
          "last": "Clinton"
        },
        "age": 41
      },
      {
        "name": {
          "first": "Charlie",
          "middle": "Day",
          "last": "Dole"
        },
        "age": 35
      }
    ]
  }
selection = theFamily['mom']

# Cast dict as JSON
x = json.dumps(selection)
print(x)