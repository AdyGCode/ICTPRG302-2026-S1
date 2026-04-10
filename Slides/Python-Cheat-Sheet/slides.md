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

# Cheat Sheet

---
level: 2
---

# Cheat Sheet


About the cheat sheet


---
layout: section
---
---
created: 2026-04-10T15:32:18 (UTC +08:00)
tags: [python cheat sheet]
source: https://realpython.com/cheatsheets/python/
author: Real Python
---

# Python Cheat Sheet – Real Python

> ## Excerpt
> Compact Python cheat sheet covering setup, syntax, data types, variables, strings, control flow, functions, classes, errors, and I/O.

---
This page contains a condensed overview of the Python programming language. It covers Python setup, syntax, data types, variables, strings, control flow, functions, classes, errors, I/O, and more! You can also download the information as a printable cheat sheet:

Get a **Python Cheat Sheet (PDF)** and learn the basics of Python 3, like working with data types, dictionaries, lists, and Python functions:

![Python Cheat Sheet](Python%20Cheat%20Sheet%20%E2%80%93%20Real%20Python/cheat_sheets_stacked.34027e654084.png)

Continue exploring [realpython.com](https://www.realpython.com/) to turbocharge your Python learning with in-depth tutorials, real-world examples, and expert guidance.

## Getting Started

-   Always add a space after the `#`
-   Use comments to explain “why” of your code

## Data Types

-   Python is dynamically typed
-   Use `None` to represent missing or optional values
-   Use `type()` to check object type
-   Check for a specific type with `isinstance()`
-   `issubclass()` checks if a class is a subclass

## Variables & Assignment

-   Variables are created when first assigned
-   Use descriptive variable names
-   Follow `snake_case` convention

## Strings

-   It’s recommended to use double-quotes for strings
-   Use `"\n"` to create a line break in a string
-   To write a backslash in a normal string, write `"\\"`

**Free Bonus:** Python Cheat Sheet (PDF) Click to preview & download

![Preview of the Python Cheat Sheet PDF](Python%20Cheat%20Sheet%20%E2%80%93%20Real%20Python/cheat_sheets_stacked.34027e654084.png)

Learn Python 3 fundamentals at a glance: data types, functions, classes, and more!

No spam. Unsubscribe any time.

## Numbers & Math

## Conditionals

-   Python uses indentation for code blocks
-   Use 4 spaces per indentation level

## Loops

-   `range(5)` generates 0 through 4
-   Use `enumerate()` to get index and value
-   `break` exits the loop, `continue` skips to next
-   Be careful with `while` to not create an infinite loop

## Functions

-   Define functions with `def`
-   Always use `()` to call a function
-   Add `return` to send values back
-   Create anonymous functions with the `lambda` keyword

## Classes

-   Classes are blueprints for objects
-   You can create multiple instances of one class
-   You commonly use classes to encapsulate data
-   Inside a class, you provide methods for interacting with the data
-   `.__init__()` is the constructor method
-   `self` refers to the instance

![Preview of the Python Cheat Sheet PDF](Python%20Cheat%20Sheet%20%E2%80%93%20Real%20Python/cheat_sheets_stacked.34027e654084.png)

**Get Your Free Python Cheat Sheet (PDF):** Learn the basics, fast.

## Exceptions

-   When Python runs and encounters an error, it creates an exception
-   Use specific exception types when possible
-   `else` runs if no exception occurred
-   `finally` always runs, even after errors

## Collections

-   A collection is any container data structure that stores multiple items
-   If an object is a collection, then you can loop through it
-   Strings are collections, too
-   Use `len()` to get the size of a collection
-   You can check if an item is in a collection with the `in` keyword
-   Some collections may look similar, but each data structure solves specific needs

## Comprehensions

-   You can think of comprehensions as condensed `for` loops
-   Comprehensions are faster than equivalent loops

**Free Bonus:** Python Cheat Sheet (PDF) Click to preview & download

![Preview of the Python Cheat Sheet PDF](Python%20Cheat%20Sheet%20%E2%80%93%20Real%20Python/cheat_sheets_stacked.34027e654084.png)

Learn Python 3 fundamentals at a glance: data types, functions, classes, and more!

No spam. Unsubscribe any time.

## File I/O

## Imports & Modules

-   Prefer explicit imports over `import *`
-   Use aliases for long module names
-   Group imports: standard library, third-party libraries, user-defined modules

## Virtual Environments

-   Virtual environments are often called “venv”
-   Use venvs to isolate project packages from the system-wide Python packages

## Packages

-   The official third-party package repository is the [Python Package Index (PyPI)](https://pypi.org/)

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

You can download this information as a printable cheat sheet:

Get a **Python Cheat Sheet (PDF)** and learn the basics of Python, like working with data types, dictionaries, lists, and Python functions:

![Python Cheat Sheet](Python%20Cheat%20Sheet%20%E2%80%93%20Real%20Python/python-logo.8eb72ea6927b.png)


---

# Acknowledgements

- Real Python. (2026). Python Cheat Sheet – Real Python. Realpython.com. https://realpython.com/cheatsheets/python/



> Slide template by Adrian Gould
> 
> Some content was generated with the assistance of Microsoft CoPilot
