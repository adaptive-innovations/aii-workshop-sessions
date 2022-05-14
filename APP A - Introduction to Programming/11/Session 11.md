# APP A: Introduction to Programming
## Session 10

|Session Time|Facilitator|Starting URL                                                               |
|------------|-----------|---------------------------------------------------------------------------|
|1 Hour      |GR         |[Formatting in Python](https://www.w3schools.com/python/python_ref_string.asp) |

## Last Week's Challenge

## String Formatting

Basic string concatenation using the "+" operator.
```py
x = "Hello"
y = "World!"
z = x + ", " + y
print(z)
```

Single line string.
```py
x = "Hello, World!"
print(x)
```

Newlines.
```py
x = "Hello, \nWorld!"
print(x)
```

Multi-line string.
```py
x = """
Hello,
World!"""
print(x)
```

String concatenation using f-strings operator.
```py
color = "brown"
sentence = f"The quick {color} fox jumps over the lazy dog"
print(sentence)
```

String and integer concatenation using f-strings operator.
```py
color = "brown"
number = 5
sentence = f"The quick {color} fox jumps over {number} lazy dog(s)"
print(sentence)
```

Refer to the variable's name and the value. Requires 3.8+.
```py
color = "brown"
number = 5
theList = ['A', 'B', 'C']
print(f'{color=}')
print(f'{number=}')
print(f'{theList=}')
```

Fetch first 2 decimal values with a number. 
```py
costOfPie = 3.141592653589793
print(f"${costOfPie:.2f}")
```

Fetch with 2 first decimal values, add the pretty commas
```py
costOfKitchen = 31532.141592653589793
print(f"${costOfKitchen:,.2f}")
```

## Working with Strings
Capitalize
```py
x = "the quick brown fox jumps over the lazy dog."
print(x)
y = x.capitalize()
print(y)
```

Upper Case
```py
x = "the quick brown fox jumps over the lazy dog."
print(x)
y = x.upper()
print(y)
```

Using Upper Case in a comparison to avoid case sensitivity.
```py
x = "lewis"
y = "LEWIS"
if x.upper() == y.upper():
    print("It's a match!")
```

Find & replace all
```py
x = "The quick brown fox jumps over the lazy dog."
print(x)
y = x.replace('brown', 'red')
print(y)
```

Strip a string
```py
x = "   The quick brown fox jumps over the lazy dog.  \n "
print(x)
y = x.strip()
print(y)
```

Find a value's starting position.
```py
x = "The quick brown fox jumps over the lazy dog."
print(x)
y = x.index('brown')
print(y)
```

Grab a section of string according to position
```py
x = "the quick brown fox jumps over the lazy dog."
print(x)
y = x[10:15]
print(y)
```

Grab value between delimiters "[" & "]"
```py
x = "Kern County [661]"
startPosition = x.index('[')+1
endPosition = x.index(']')
y = x[startPosition:endPosition]
print(y)
```

Grab value between delimiters "[" & "]" EXAMPLE B
```py
theList = ["Kern County [661]", "Fresno [559]", "Narnia [4654654]"]
for each in theList:
    startPosition = each.index('[')+1
    endPosition = each.index(']')
    print(each[startPosition:endPosition])
```

Splitting Text into a list
```py
x = "Jon|Doe|CEO"
print(x)
y = x.split('|')
print(y)
print(f"{y[0]} {y[1]}'s Title is {y[2]}!")
```

OPTIONAL: If you're crazy and want to dive into RegEx
> https://www.w3schools.com/python/python_regex.asp

Using RegEx to get text between 2 characters
```py
import re
s = "Kern County [661]"
pattern = "\[(.*?)\]"
substring = re.search(pattern, s).group(1)
print(substring)
```
## Challenge
Open/Read files ```employees.json```, ```employeeZips.txt```, ```zipcodes.csv``` and compile the data into a .csv file called ```output.csv```.
- Use only the first letter of Gender (e.g. "Male" becomes "M")
- Capitalize the first letter of the city (e.g. "BAKERSFIELD" becomes "Bakersfield")

My approach would be:
- Read ```employees.json``` and build a list of instances of class called ```employee```.
- Read ```employeeZips.txt```, and update each employee in list with ```"zipcode": "93311"```
- Read ```zipcodes.csv```, and update each employee in list with ```"city": "Chicago"``` & ```"state": "IL"```
Example instance ```pyclass.__dict__```:
```
{
    "ID": 1,
    "First Name": "Brad",
    "Last Name": "Brooks",
    "Gender": "Male",
    "Age": 20,
    "Email": "b.brooks@randatmail.com",
    "Zip": "93311",
    "City": "Bakersfield",
    "State": "CA"
}
```
- Lastly, write each employee to ```output.csv```.