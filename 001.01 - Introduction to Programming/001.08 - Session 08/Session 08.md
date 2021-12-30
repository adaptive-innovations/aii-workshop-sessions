# APP A: Introduction to Programming
## Session 07

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Python Classes](https://www.w3schools.com/python/python_classes.asp) |

## Last Week's Challenge

## Classes
Define a class
```py
class Employee:
    nameFirst = 'Greg'
    nameLast = 'Kapler'

Minion1 = Employee()

print(Minion1.nameFirst)
print(Minion1.nameLast)
```

Initialize a class
```py
class Employee:
    def __init__(self, first, last):
        self.nameFirst = first
        self.nameLast = last
        self.nameFull = self.nameFirst + " " + self.nameLast

Minion1 = Employee('Greg', 'Kapler')
Minion2 = Employee('Amber', 'Kapler')

print(Minion1.nameFirst + " " + Minion1.nameLast)
print(Minion2.nameFirst + " " + Minion2.nameLast)
```


Add more functions to the class
```py
class Employee:
    def __init__(self, first, last, pay):
        self.nameFirst = first
        self.nameLast = last
        self.nameFull = self.nameFirst + " " + self.nameLast
        self.paySalary = pay
    def giveRaise(self, thePercentage):
        newSalary = self.paySalary * thePercentage
        self.paySalary = newSalary

Minion1 = Employee('Greg', 'Kapler', 500000)

print(Minion1.nameFull + " makes $" + str(Minion1.paySalary) + " per year!")

Minion1.giveRaise(1.1)

print(Minion1.nameFull + " makes $" + str(Minion1.paySalary) + " per year!")
```

Present the class as a dict or JSON object
```py
import json

class Employee:
    def __init__(self, first, last, pay):
        self.nameFirst = first
        self.nameLast = last
        self.nameFull = self.nameFirst + " " + self.nameLast
        self.paySalary = pay
    def giveRaise(self, thePercentage):
        newSalary = self.paySalary * thePercentage
        self.paySalary = newSalary

Minion1 = Employee('Greg', 'Kapler', 500000)
Minion1.giveRaise(1.1)

# Print the class as a dict
print(Minion1.__dict__)

# Print the class as JSON
print(json.dumps(Minion1.__dict__, indent=4))
```

List of Class Objects
```py
listOfEmployees = []

class Employee:
    def __init__(self, first, last, pay):
        self.nameFirst = first
        self.nameLast = last
        self.nameFull = self.nameFirst + " " + self.nameLast
        self.paySalary = pay

listOfEmployees.append(Employee('Greg', 'Kapler', 500000))
listOfEmployees.append(Employee('Lewis', 'Wilcox', 500000))
listOfEmployees.append(Employee('Chris', 'Barnett', 500000))
listOfEmployees.append(Employee('Jeff', 'Buehler', 500000))

employeeCount = len(listOfEmployees)
print("There are " + str(employeeCount) + " employees on file!")

for each in listOfEmployees:
    print(each.nameFull)
    print(json.dumps(each.__dict__, indent=4))
```

## Challenge
Create a Villan class.
Include a variable for the number of minions he has in his army.
Every new villain always starts out with 101 minions.
Create a function that adds to the current number of minions at his disposal.
Update the Villains' callsign variable after his/her class instance has already been initialized.