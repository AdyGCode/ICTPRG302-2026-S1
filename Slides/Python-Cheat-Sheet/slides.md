---
theme: nmt
background: https://cover.sli.dev
title: Python Cheat Sheet
class: text-left
drawings:
  persist: false
transition: fade
mdc: true
duration: 35min
---

# Python Cheat Sheet

#### ICT30120 Certificate III in Information Technology<br>
#### ICT40120 Certificate IV in Information Technology<br>
#### ICT50120 Diploma of Information Technology

<div @click="$slidev.nav.next" class="mt-12 -mx-4 p-4" hover:bg="white op-10">
<p>Press <kbd>Space</kbd> or <kbd>RIGHT</kbd> for next slide/step <fa7-solid-arrow-right /></p>
</div>

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/adygcode/SaaS-FED-Notes" target="_blank" class="slidev-icon-btn">
    <fa7-brands-github class="text-zinc-300 text-3xl -mr-2"/>
  </a>
</div>


<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->


---
layout: default
level: 2
---

# Navigating Slides

Hover over the bottom-left corner to see the navigation's controls panel.

## Keyboard Shortcuts

|                                                     |                             |
|-----------------------------------------------------|-----------------------------|
| <kbd>right</kbd> / <kbd>space</kbd>                 | next animation or slide     |
| <kbd>left</kbd>  / <kbd>shift</kbd><kbd>space</kbd> | previous animation or slide |
| <kbd>up</kbd>                                       | previous slide              |
| <kbd>down</kbd>                                     | next slide                  |

---
layout: section
---

# Objectives

---
layout: two-cols
level: 2
class: text-left
---

# Objectives

::left::

TODO: Add objectives

::right::

TODO: Add further objectives


---
level: 2
---

# Contents

<Toc minDepth="1" maxDepth="1" columns="2" />


---
layout: section
---

# About the Cheat Sheet

---
level: 2
layout: two-cols
---

# About the Cheat Sheet

::left::
### Original Source
- Original Source https://realpython.com/cheatsheets/python/
- Updated and modified for educational use

<br>

### General Overview
The cheat sheet:
- Is a condensed overview of the Python programming language 

::right::
### Contents
- Python setup, 
- syntax, 
- data types, 
- variables, 
- strings, 
- control flow, 
- functions, 
- classes, 
- errors, 
- I/O, 
- and more! 


---
layout: section
---

# Getting Started

---
level: 2
layout: two-cols
---

# Getting Started

::left::

<br>

### Start the Interactive Shell
```bash [Shell]
python
```
<br>

### Quit the Interactive Shell

```python [Python]
exit()
```

::right::

<br>

### Run a Script
```bash [Shell]
python my_script.py
```

<br>

### Run a Script in Interactive Mode
```bash [Shell]
python -i my_script.py
```

---
layout: section
---

# PEP8 Rules and Conventions

---
level: 2
layout: two-cols
---

# PEP8 Rules and Conventions

::left::

### Comments
- Always add a space after the `#`
- Use comments to explain “why” of your code

::right::

### Blocks
- Use 4 spaces to indent


---
level: 2
layout: two-cols
---

# PEP8 Rules and Conventions

::left::

### Variables
- make them descriptive
- use nouns (things)
- always use snake_case
- must start with a lowercase letter (`a`-`z`) or underscore `_`
- underscore to separate words

::right::

### Constants
- make them descriptive
- use nouns (things)
- always use SHOUTY_SNAKE_CASE
- must start with a capital letter (`A`-`Z`) or underscore `_`
- underscore to separate words


---
level: 2
layout: two-cols
---

# PEP8 Rules and Conventions

::left::

### User Defined Functions
- make the name descriptive
- use verbs (actions)
- always use snake_case when naming
- must start with a lowercase letter (`a`-`z`) or underscore `_`
- Leave TWO blank lines after a user defined function

::right::


---
layout: section
---

# Data Types

---
level: 2
---

# Data Types

## General Notes
-   Python is dynamically typed
-   Use `None` to represent missing or optional values
-   Use `type()` to check object type
-   Check for a specific type with `isinstance()`
-   `issubclass()` checks if a class is a subclass


---
level: 2
---

# Data Types
## Type Investigation

```python [Python]
type(42)                # <class 'int'>
type(3.14)              # <class 'float'>
type("Hello")           # <class 'str'>
type(True)              # <class 'bool'>
type(None)              # <class 'NoneType'>

isinstance(3.14, float)  # True
issubclass(int, object)  # True. Everything inherits from object
```


---
level: 2
---

# Data Types
## Type Conversion

```python [Python]
int("42")                # 42
float("3.14")            # 3.14
str(42)                  # "42"
bool(1)                  # True
list("abc")              # ["a", "b", "c"]
```

---
layout: section
---

# Variables & Assignment

---
level: 2
---
# Variables & Assignment

-   Variables are created when first assigned
-   Use descriptive variable names
-   Follow `snake_case` convention

### Basic Assignment

```python [Python]
name = "Leo"           # String
age = 7                # Integer
height = 5.6           # Float
is_cat = True          # Boolean
flaws = None           # None type
```

---
level: 2
---

# Variables & Assignment
### Parallel & Chained Assignments

```python [Python]
x, y = 10, 20          # Assign multiple values
a = b = c = 0          # Give same value to multiple variables
```

### Augmented Assignments

```python [Python]
counter += 1
numbers += [4, 5]
permissions |= write
```

---
layout: section
---

# Strings

---
level: 2
layout: two-cols
---

# Strings

-   Recommended to use double-quotes `"` for strings
-   Use `"\n"` to create a line break in a string
-   To write a backslash in a normal string, write `"\\"`

::left::

### Creating Strings

```python [Python]
single = 'Hello'
double = "World"
multi = """Multiple
line string"""
```

::right::

### String Operations

```python [Python]
greeting = "me" + "ow!"  
# greeting contains "meow!"

repeat = "Meow!" * 3     
# repeat contains "Meow!Meow!Meow!"

length = len("Python")   
# length contains 6

```


---
level: 2
layout: two-cols
---

# Strings

::left::

### String Methods

```python [Python]
"a".upper()                  # "A"
"A".lower()                  # "a"
" a ".strip()                # "a"
"abc".replace("bc", "ha")    # "aha"
"a b".split()                # ["a", "b"]
"-".join(["a", "b"])         # "a-b"
```

::right::

### String Indexing & Slicing

```python [Python]
text = "Python"
text[0]      # "P" (first)
text[-1]     # "n" (last)
text[1:4]    # "yth" (slice)
text[:3]     # "Pyt" (from start)
text[3:]     # "hon" (to end)
text[::2]    # "Pto" (every 2nd)
text[::-1]   # "nohtyP" (reverse)
```


---
level: 2
layout: two-cols
---

# Strings

## String Formatting

::left::

### f-strings
```python [Python]
name = "Aubrey"
age = 2

f"Hello, {name}!"               
# generates: "Hello, Aubrey!"

f"{name} is {age} years old"    
# generates: "Aubrey is 2 years old"

f"Debug: {age=}"                
# generates: "Debug: age=2"

```

::right::


### Format method

```python
template = "Hello, {name}! You're {age}."
template.format(name="Aubrey", age=2)    
# generates: "Hello, Aubrey! You're 2."
```

---
level: 2
---

# Strings

## Raw Strings

### Normal string with an escaped tab
```python [Python]
"This is:\tCool."       # "This is:    Cool."
```

### Raw string with escape sequences

```python [Python]
r"This is:\tCool."      # "This is:\tCool."
```

---
layout: section
---

# Numbers & Math

---
level: 2
layout: two-cols
---

# Numbers & Math

::left::

### Arithmetic Operators

```python [Python]
10 + 3    # 13
10 - 3    # 7
10 * 3    # 30
10 / 3    # 3.3333333333333335
10 // 3   # 3
10 % 3    # 1
2 ** 3    # 8
```

::right::
### Useful Functions

```python [Python]
abs(-5)              # 5
round(3.7)           # 4
round(3.14159, 2)    # 3.14
min(3, 1, 2)         # 1
max(3, 1, 2)         # 3
sum([1, 2, 3])       # 6
```


---
layout: section
---

# Blocks (or Code Structures)


---
level: 2
layout: two-cols
---

# Blocks (or Code Structures)

::left::

### Groups of sequences of statements

Including:
- Conditionals (Selections)
- Loops (Selections)
    - For Loops,
    - While Loops
- and more

::right::

### Remember...

-   Python uses indentation for code blocks
-   Use 4 spaces per indentation level

---
layout: section
---

# Conditionals

---
level: 2
layout: two-cols
---

# Conditionals



::left::

### If-Elif-Else

```python [Python]
if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
else:
    category = "adult"
```

::right::

### Comparison Operators

```python [Python]
x == y    # Equal to
x != y    # Not equal to
x < y     # Less than
x <= y    # Less than or equal
x > y     # Greater than
x >= y    # Greater than or equal
```

---
level: 2
layout: two-cols
---

# Conditionals

::left::

### Logical Operators

```python [Python]
if age >= 18 and has_car:
    print("Roadtrip!")

if is_weekend or is_holiday:
    print("No work today.")

if not is_raining:
    print("You can go outside.")
```


---
layout: section
---

# Loops

---
level: 2
---

# Loops

- `range(5)` generates 0 through 4
- Use `enumerate()` to get index and value
- `break` exits the loop, `continue` skips to next
- Be careful with `while` to not create an infinite loop


---
level: 2
layout: two-cols
---

# Loops
## For Loops

::left::

### Loop through range

for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

### Loop through collection

fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)

::right::

### With enumerate for index

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")


---
level: 2
layout: two-cols
---

# Loops
## While Loops

### While condition


### While True
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

### Loop Control

for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit loop
    print(i)

---
layout: section
---

# Functions (User Defined)

---
level: 2
layout: two-cols
---

# Functions (User Defined)

-   Define functions with `def`
-   Always use `()` to call a function
-   Add `return` to send values back
-   Create anonymous functions with the `lambda` keyword

Defining Functions
def greet():
    return "Hello!"

def greet_person(name):
    return f"Hello, {name}!"

def add(x, y=10):    # Default parameter
    return x + y
Calling Functions
greet()                   # "Hello!"
greet_person("Bartosz")   # "Hello, Bartosz"
add(5, 3)                 # 8
add(7)                    # 17
Return Values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3])
Useful Built-in Functions
callable()  # Checks if an object can be called as a function
dir()       # Lists attributes and methods
globals()   # Get a dictionary of the current global symbol table
hash()      # Get the hash value
id()        # Get the unique identifier
locals()    # Get a dictionary of the current local symbol table
repr()      # Get a string representation for debugging
Lambda Functions
square = lambda x: x**2
result = square(5)  # 25

# With map and filter
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

## Classes

-   Classes are blueprints for objects
-   You can create multiple instances of one class
-   You commonly use classes to encapsulate data
-   Inside a class, you provide methods for interacting with the data
-   `.__init__()` is the constructor method
-   `self` refers to the instance

Defining Classes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Create instance
my_dog = Dog("Frieda", 3)
print(my_dog.bark())  # Frieda says Woof!
Class Attributes & Methods
class Cat:
    species = "Felis catus"   # Class attribute

    def __init__(self, name):
        self.name = name      # Instance attribute

    def meow(self):
        return f"{self.name} says Meow!"

    @classmethod
    def create_kitten(cls, name):
        return cls(f"Baby {name}")
Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

## Exceptions

-   When Python runs and encounters an error, it creates an exception
-   Use specific exception types when possible
-   `else` runs if no exception occurred
-   `finally` always runs, even after errors

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Calculation attempted")
Common Exceptions
ValueError         # Invalid value
TypeError          # Wrong type
IndexError         # List index out of range
KeyError           # Dict key not found
FileNotFoundError  # File doesn't exist
Raising Exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age



## Collections

-   A collection is any container data structure that stores multiple items
-   If an object is a collection, then you can loop through it
-   Strings are collections, too
-   Use `len()` to get the size of a collection
-   You can check if an item is in a collection with the `in` keyword
-   Some collections may look similar, but each data structure solves specific needs

Lists
# Creating lists
empty = []
nums = [5]
mixed = [1, "two", 3.0, True]

# List methods
nums.append("x")         # Add to end
nums.insert(0, "y")      # Insert at index 0
nums.extend(["z", 5])    # Extend with iterable
nums.remove("x")         # Remove first "x"
last = nums.pop()        # Pop returns last element

# List indexing and checks
fruits = ["banana", "apple", "orange"]
fruits[0]                # "banana"
fruits[-1]               # "orange"
"apple" in fruits        # True
len(fruits)              # 3
Tuples
# Creating tuples
point = (3, 4)
single = (1,)    # Note the comma!
empty = ()

# Basic tuple unpacking
point = (3, 4)
x, y = point 
x                # 3
y                # 4

# Extended unpacking
first, *rest = (1, 2, 3, 4) 
first            # 1
rest             # [2, 3, 4]
Sets
# Creating Sets
a = {1, 2, 3}
b = set([3, 4, 4, 5])

# Set Operations
a | b            # {1, 2, 3, 4, 5}
a & b            # {3}
a - b            # {1, 2}
a ^ b            # {1, 2, 4, 5}
Dictionaries
# Creating Dictionaries
empty = {}
pet = {"name": "Leo", "age": 42}

# Dictionary Operations
pet["sound"] = "Purr!"   # Add key and value
pet["age"] = 7           # Update value
age = pet.get("age", 0)  # Get with default
del pet["sound"]         # Delete key
pet.pop("age")           # Remove and return

# Dictionary Methods
pet = {"name": "Frieda", "sound": "Bark!"}
pet.keys()         # dict_keys(['name', 'sound'])
pet.values()       # dict_values(['Frieda', 'Bark!'])
pet.items()        # dict_items([('name', 'Frieda'), ('sound', 'Bark!')])


## Comprehensions

-   You can think of comprehensions as condensed `for` loops
-   Comprehensions are faster than equivalent loops

List Comprehensions
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
Other Comprehensions
# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}

# Set comprehension
unique_lengths = {len(word) for word in ["who", "what", "why"]}

# Generator expression
sum_squares = sum(x**2 for x in range(1000))

## File I/O

File Operations
# Read an entire file
with open("file.txt", mode="r", encoding="utf-8") as file:
    content = file.read()

# Read a file line by line
with open("file.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Write a file
with open("output.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World!\n")

# Append to a File
with open("log.txt", mode="a", encoding="utf-8") as file:
    file.write("New log entry\n")




## Imports & Modules

-   Prefer explicit imports over `import *`
-   Use aliases for long module names
-   Group imports: standard library, third-party libraries, user-defined modules

Import Styles
# Import entire module
import math
result = math.sqrt(16)

# Import specific function
from math import sqrt
result = sqrt(16)

# Import with alias
import numpy as np
array = np.array([1, 2, 3])

# Import all (not recommended)
from math import *
Package Imports
# Import from package
import package.module
from package import module
from package.subpackage import module

# Import specific items
from package.module import function, Class
from package.module import name as alias


## Virtual Environments

-   Virtual environments are often called “venv”
-   Use venvs to isolate project packages from the system-wide Python packages

Create Virtual Environment
$ python -m venv .venv
Activate Virtual Environment (Windows)
PS> .venv\Scripts\activate
Activate Virtual Environment (Linux & macOS)
$ source .venv/bin/activate
Deactivate Virtual Environment
(.venv) $ deactivate

## Packages

-   The official third-party package repository is the [Python Package Index (PyPI)](https://pypi.org/)

Install Packages
$ python -m pip install requests
Save Requirements & Install from File
$ python -m pip freeze > requirements.txt
$ python -m pip install -r requirements.txt

## Miscellaneous

| Truthy | Falsy |
| --- | --- |
| `-42` | `0` |
| `3.14` | `0.0` |
| `"John"` | `""` |
| `[1, 2, 3]` | `[]` |
| `("apple", "banana")` | `()` |
| `{"key": None}` | `{}` |
|  | `None` |

Pythonic Constructs
# Swap variables
a, b = b, a

# Flatten a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for sublist in matrix for item in sublist]

# Remove duplicates
unique_unordered = list(set(my_list))

# Remove duplicates, preserve order
unique = list(dict.fromkeys(my_list))

# Count occurrences
from collections import Counter

counts = Counter(my_list)


---

# Acknowledgements

- Real Python. (2026). Python Cheat Sheet – Real Python. Realpython.com. https://realpython.com/cheatsheets/python/



> Slide template by Adrian Gould
> 
> Some content was generated with the assistance of Microsoft CoPilot
