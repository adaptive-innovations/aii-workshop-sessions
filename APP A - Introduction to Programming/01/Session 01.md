# APP A: Introduction to Programming
## Session 01

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Python Intro](https://www.w3schools.com/python/python_intro.asp)     |

## Code Highlights
The Print Statement
```py
print('Hello, World!')
```

```py
# Variables
x = 1
print(x)
```

```py
# Operators
x = 1
y = 23
print(x+y)
```

```py
# Variables Can Reference Each Other
x = 1
y = 23
z = x+y
print(z)
```

```py
# Variables Can Change
x = 1
print(x)
x = 100
print(x)
```

Comments
```py
# This does nothing
```

```py
# User Input
x = input('Enter username: ')
print(x)
```

```py
# String Concatonate
x = input('Enter username: ')
print("Your username is " + x + "!")
```

```py
# Assign Multiple Values
x = "Orange"
y = "Banana"
z = "Cherry"

print(x)
print(y)
print(z)

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
```

```py
# Casting Variables Example A
x = "3" # STR
y = 5 # INT

print(int(x) + y)
```


```py
# Casting Variables Example B
x = input('Tell me a number: ')
y = input('Tell me another number: ')

z = int(x)+int(y)

print("Added up: " + str(z))
```

## Challenge
Create a program that...
- Asks for user input
- Performs a math operation with it
- Returns the result
- Uses Comments
- Demonstrates variable casting