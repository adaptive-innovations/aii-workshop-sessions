# APP A: Introduction to Programming
## Session 10

|Session Time|Facilitator|Starting URL                                                               |
|------------|-----------|---------------------------------------------------------------------------|
|1 Hour      |GR         |[File Handling](https://www.w3schools.com/python/python_file_handling.asp) |

## Last Week's Challenge

## File Handling
Open a text file, read the contents, then close it.
```py
# Open the file
f = open("demofile.txt", "r")

# Read the lines
rows = f.readlines()
print(rows)

# Close the file
f.close()
```

Open a JSON file, read the contents, then close it.
```py
# Open the file
import json 
f = open("person.json")

# Read the object
personDict = json.loads(f.read())
print(personDict)

f.close()
```

## Challenge
All of the challenges above.