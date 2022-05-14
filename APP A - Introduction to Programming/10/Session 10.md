# APP A: Introduction to Programming
## Session 10

|Session Time|Facilitator|Starting URL                                                               |
|------------|-----------|---------------------------------------------------------------------------|
|1 Hour      |GR         |[File Handling](https://www.w3schools.com/python/python_file_handling.asp) |

## Last Week's Challenge

## File Handling
Open a text file, read the contents, then close it.
```py
# Open the text file
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

Open a CSV file, read the contents, then close it.

[See Instructions: Working with CSV](https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library)
```py
import csv

csvFile = open('People.csv')

# Read the object
fileContents = csv.reader(csvFile, delimiter=',')
for row in fileContents:
    print(row)

csvFile.close()
```

Create or open a text file, overwrite the contents, then close it.
```py
inviteList = ["Johnny Depp", "Leo Decaprio", "Andy Serkis", "Angelina Jolie"]

f = open("demowritefile.txt", "w")

for attendee in inviteList:
    f.write(attendee + "\n")

f.close()
```

Create or open a JSON file, overwrite the contents, then close it.
```py
import json
person = {"name":{"first":"Jon","middle":"Jacob","last":"Doe"},"age":55}

f = open("newPerson.json", "w")
f.write(json.dumps(person, indent=3))

f.close()
```

Create or open a CSV file, overwrite the contents, then close it.
```py
import csv

csvFile = open('newPeople.csv', mode='w', newline='')

data = []
data.append(["nameFirst","nameLast","age"]) # Headers
data.append(["Bill","Jones","55"])
data.append(["Jill","Joens","54"])

file_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for row in data:
    file_writer.writerow(row)

csvFile.close()
```

LIFE HACK: Use the location of the .py file as current working path.
```py
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
```

## Challenge
Demonstrate each of the following actions:
- Read from a text file that you made.
- Read from a JSON file that you made.
- Read from a CSV file that you made.
- Write to a text file.
- Write to a JSON file.
- Write to a CSV file.