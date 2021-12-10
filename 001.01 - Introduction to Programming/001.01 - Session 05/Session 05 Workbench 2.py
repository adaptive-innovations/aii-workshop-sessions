# Import the JSON module
import json

# Create a dictionary
theFamily = {
                "dad": "Dick",
                "mom": "Jane",
                "kids": ["Timmy", "Billy", "Sally-Mae", "Sally-Anne"]
            }
print(theFamily)

# Cast dict as JSON
x = json.dumps(theFamily)
print(x)