# APP A: Introduction to Programming
## Session 02

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Python Conditions](https://www.w3schools.com/python/python_conditions.asp)     |

## Last Week's Challenge

## Code Highlights
Identify a data type
```py
x = 1
y = type(x)
print("The data type is: "+str(y))
```

### The IF statement

IF greater than
```py
a = 33
b = 200
if b > a:
    print("b is greater than a")
```
IF less than
```py
a = 200
b = 33
if b < a:
    print("b is less than a")
```
IF equal to
```py
a = 33
b = 33
if b == a:
    print("b is equal to a")
```
IF NOT equal to
```py
a = 33
b = 34
if b != a:
    print("b is not equal to a")
```
### The ELSE statement

IF ELSE
```py
x = int(input('Tell me a number: '))

if x > 100 :
    print (str(x)+' is greater than 100!')
else:
    print ('Dream bigger!')
```

ELIF (Else If)
```py
x = int(input('Tell me a number: '))

if x > 100:
    print(str(x)+' is greater than 100!')
elif x > 50:
    print(str(x)+' is greater than 50!')
else:
    print('Dream bigger!')
```

Multiple ELIFs
```py
x = int(input('Tell me a number: '))

if x > 100:
    print(str(x)+' is greater than 100!')
elif x > 50:
    print(str(x)+' is greater than 50!')
elif x > 0:
    print(str(x)+' is greater than 0!')
else:
    print('Dream bigger!')
```

Indentation Matters
```py
a = 33
b = 200
if b > a:
    print("b is greater than a")
    print("Here's the second line of text!")
```
```py
a = 33
b = 200
if b > a:
    print("b is greater than a")
print("Here's the second line of text!")
```

Check if it's a number
```py
x = input('Tell me a number: ')
if x.isdigit():
    print("Nice, that's a number!")
else:
    print("Go away you clown!")
```

## Challenge
Create a program that...
- Asks for user input
- Performs an conditional operation with it (IF, ELIF, ELSE)
- Returns the result
- Uses Comments
- Demonstrates variable casting