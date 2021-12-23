# APP A: Introduction to Programming
## Session 06

|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Python Functions](https://www.w3schools.com/python/python_functions.asp)   |

## Last Week's Challenge

## Functions
Define a function
```py
def myTestFunction():
    x = 1
    y = 2
    z = x+y
    print(z)
```

Call a function 
```py
myTestFunction()
```

Pass Input parameters 
```py
def myTestFunction(value_a, value_b):
    z = value_a + value_b
    print(z)

myTestFunction(5, 6)
myTestFunction(8, 10)
```

Return Output
```py
def myTestFunction(value_a, value_b):
    z = value_a + value_b
    return z

x = myTestFunction(5, 6)
print(x)

print(myTestFunction(8, 10))
```

Return Multiple Outputs
```py
def myTestFunction(value_a, value_b):
    y = "Test String"
    z = value_a + value_b
    return y, z

variable1, variable2 = myTestFunction(5, 6)
print(variable1)
print(variable2)
```

Multiple Function Example
```py
def subtractTwoNumbers(value_a, value_b):
    z = value_a - value_b
    return z

def addTwoNumbers(value_a, value_b):
    z = value_a + value_b
    return z

x = addTwoNumbers(5, 6)
print(x)

y = subtractTwoNumbers(x, 2)
print(y)
```

Dictionary Creation Example
```py
def createRecipe(title, time, servings, author):
    x = {}
    x['title'] = title
    x['time'] = time
    x['servings'] = servings
    x['author'] = author
    return x
rhubarbPie = createRecipe("Rhubarb Pie", "3 Hours", "24", "Lewis")
print(rhubarbPie)
```

## Scope
Local Variables: Variables used only in the function
Example: "z"
```py
def myTestFunction(value_a, value_b):
    z = value_a + value_b
    return z
```

Global Variables: Variables used in the entire program
Example: "y"
```py
y = "Example Text"
def myTestFunction(value_a, value_b):
    print(y)
    z = value_a + value_b
    return z
```


## Challenge
Create a function which calculates square footage using 2 inputs.
Ask the user for the values for the