# APP A: Introduction to Programming
## Session 03

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Python Lists](https://www.w3schools.com/python/python_lists.asp)     |

## Last Week's Challenge

## Working with Lists
Create a list
```py
list1 = ["apple", "banana", "cherry"] # Strings
list2 = [1, 5, 7, 9, 3] # Integers
list3 = [True, False, False] # Booleans
list4 = ["apple", 7, True] # Mixed Data Types
```
 
Retrieve an item from a list index
```py
inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
x = inviteList[0]
print(x)

inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
x = 2
print(inviteList[x])
```

Sort a list
```py
# Sort Ascending Order
inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
inviteList.sort()
print(inviteList)

# Sort Descending Order
inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
inviteList.sort(reverse=True)
print(inviteList)
```

Append to a list
```py
inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
print(inviteList)
inviteList.append("Amber")
print(inviteList)
```

See if a list contains something
```py
inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
inviteList.append("Amber")
if "Amber" in inviteList:
    answer = "Amber is invited!"
else:
    answer = "Amber needs to leave, now!"
print(answer)
```

See how many items in a list
```py
inviteList = ["Chris", "Lewis", "Greg", "Elijah"]
howMany = len(inviteList)
print(howMany)
```

## The FOR Loop
```py
inviteList = ["Chris", "Lewis", "Waldo", "Greg", "Elijah"]
for attendee in inviteList:
    print(attendee)

# A range
for each in range(1, 10):
    print(each)

# With IFs
inviteList = ["Chris", "Lewis", "Waldo", "Greg", "Elijah"]
for each in inviteList:
    if each == "Waldo":
        print("There's Waldo!")
    else:
        print(each)
```

## The WHILE Loop
(CTRL+C for keyboard interrupt)

A simple while loop
```py
x = 1
while x <= 10:
    print(x)
    x += 1
```

With User Input
```py
entry = ""
theList = []
while entry != "exit":
    entry = input('Please add something to the list, or use the "exit" command: ')
    if entry != "exit":
        theList.append(entry)
        print(theList)
```

## Challenge
THE CHANGE CALCULATOR
- The user enters a purchase amount
- Then the user enters the amount tendered
- Calculate how many $100's/$50's/$20's/$10's/$5's/$1's/Quarters/Dimes/Nickels/Pennies to hand back to the customer.  

> Suggested PSEUDOCODE


This is Pseudocode:
A rough draft / sketch of the program. IT IS NOT PYTHON.

See https://en.wikipedia.org/wiki/Pseudocode
```py
# Get the input
AmountOwed = User Input A
AmountTendered = User Input B
# Iterate through the currency types
AmountChange = AmountTendered - AmountOwed
AmountCalculated = AmountChange
WHILE AmountCalculated > 0:
    IF AmountCalculated > 100:
        BillOneHundreds += 1
        AmountCalculated - 100
    ELSE IF AmountCalculated > 50:
        BillFiftys += 1
        AmountCalculated - 50
    ETC...
    ETC...
    ELSE
        CoinsPennies += 1
        AmountCalculated - 0.01
# Build the response
LIST APPEND BillOneHundreds + " $100's"
LIST APPEND BillFiftys + "## $50's"
ETC
FOR EACH IN LIST:
    PRINT EACH
```