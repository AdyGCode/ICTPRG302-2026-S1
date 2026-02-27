---
theme: nmt
background: https://cover.sli.dev
title: ICTPRG302 - Puzzles 1
class: text-left
drawings:
  persist: false
transition: fade
mdc: true
duration: 35min
---

# ICTPRG302 Introduction to Programming (Python)

## Puzzles to Practice With #1

---
layout: two-cols
---

# Python Puzzles to Practice With #1

::left::

## Level: 🌶️ Just starting out!

<br> 

## Language: Python 3  

::right::

## Activity types

- True/False
- Two truths & one lie
- Find the bug
- Predict the output
- Fill-in
- Write code
- Guided steps

---
layout: section
---

# Commenting & Documenting Code

---

# B-COM-1 — Why comment?

## Scenario: 

You're handing a tiny script to a classmate. 

They ask if comments affect how the program runs.  

## Question:

<Announcement type="brainstorm">
Comments are lines starting with `#`. 
<br>
Do they change the program's output. 

Yes or No?
</Announcement>

---

# B-COM-2 — Add a helpful comment

## Scenario: 

A junior keeps confusing addition with concatenation.  

### Task: 

Add **one** comment that explains the difference for the two lines below.  

### Guided steps:


1) Read and understand the purpose of each `print`.
2) Write one comment **above** the pair explaining the difference.

```python
print(3 + 4)
print("3" + "4")
```

---

# B-COM-4 — Find the bug: missing `#` 
 
## Scenario: 

Someone meant to leave themselves a note, but the program crashes.  

### Task:

Fix the error by making the note a real comment.

```python
This line is just a reminder to fix the math later
print(2 + 2)
```

---
layout: section
---

# Displaying Results & Output

---

# B-OUT-1 — Hello shop!

## Scenario: 

A kiosk should greet users.  

## Task:

Write **one** line that prints `Welcome to Byte-Sized Shop!`.

---

# B-OUT-2 — Numbers vs. strings

## Scenario: 

You audit two lines from last year's code.  

## Predict the Output:

What do these print?  

```python
print(7 + 8)
print("7" + "8")
```

---

# B-OUT-3 — Print needs brackets (Find the bug)
 
## Scenario: 

A Python snippet was pasted into a file, but there is an error.

## Task:

What is the error?

How do you fix it?

```python
print "System online"
```
---

# B-OUT-4 — Show a total
 
## Scenario: 

Show a customer's total.  

## Task:

- Create a variable called `total` that has a value of `12.5`, and then
- Print `Total: $` followed by the value of total.  

## Guided steps:

1) Create `total = 12.5`.
2) Print using either `print('Total: $', total)` or concatenation.

---
layout: section
---

# Variables & Naming Variables

---

# B-VAR-1 — Valid name?
 
## Scenario: 

You're naming variables for a library app.  

<Announcement type="brainstorm">
<code>book_count</code> is a valid variable name in Python. 

<p>True or False?</p>
</Announcement>

---

# B-VAR-2 — Don't fight keywords
 
## Scenario: 

Someone used a reserved word as a name.  

## Task:

Rename the variable to something legal and meaningful. 

```python
class = "Physics"
print(class)
```

---

# B-VAR-3 — Short and clear
 
## Scenario: 

Team style guide discussion.  

## Pick the **lie**

1) Names should be descriptive but concise.  
2) Variable names can start with a number.  
3) `snake_case` is common in Python.

---

# B-VAR-4 — Reassign then print 
 
## Scenario: 

A counter gets updated.  

## Predict the output:

 What prints?

```python
count = 1
count = count + 2
print(count)
```
---

# B-VAR-5 — Set and show
 
## Scenario: 

Track a user's nickname.  

## Task:

- Create a variable `nickname` with your name
- Print `Hello, <name>!` using concatenation.  

## Guided steps:

1) Make the variable. 
2) Print the message.

---
layout: section
---

# Expressions

---

# B-EXP-1 — Order of operations
 
## Scenario: 

You review a formula.  

## Predict the output:

 What does this print?  

```python
print(2 + 3 * 4)
```

---

# B-EXP-2 — Force the order
 
## Scenario: 

You need the result `20` using the same numbers as above.  

## Task:

Add parentheses (round brackets) to `2 + 3 * 4` so it evaluates to `20`.

---

# B-EXP-3 — Division facts
 
## Scenario: 

A teammate mixes up `/` and `//`.  
<br>

<Announcement type="brainstorm">
In Python, <code>5 / 2</code> gives a <code>float</code> and <code>5 // 2</code> gives an <code>int</code>.

Is this **True** or **False**?
</Announcement>

---

# B-EXP-4 — Mix types
 
## Scenario: 

A quick sum fails.  

## Task:

Fix the error so it prints `12`.  

```python
print("7" + 5)
```
---

# B-EXP-5 — Tiny calculator
 
## Scenario: 

A kiosk adds two numbers for users.  

## Task:

Create the two variables `first_number` and `second_number`, `first_number 
= 6`, `second_number = 9`, then print the label and result on one line (e.g.,
`a + b = 15`) .  

## Guided steps:

1) Create variables. 
2) Use `print('first_number + second_number =', first_number + second_number)` or concatenation.

---
layout: section
---

# Comparisons

---

# B-CMP-1 — Same value?
 
## Scenario: 

You compare user input with a number.  

<br>

<Announcement type="brainstorm">
Does the comparison expression <code>5 == "5"</code> evaluate to True? 

Yes or No?
</Announcement>

<Announcement type="info">
Note: <code>=</code> is a <code>=</code> followed by an <code>=</code>.
</Announcement>
---

# B-CMP-2 — Boundary check
 
## Scenario: 

Validate ticket age.  

## Predict the Output:

What does the following Python code print?

```python
print(3 < 3)
print(3 <= 3)
```

---

# B-CMP-3 — Not equal (Write code)
 
## Scenario: 

A quick sanity check.  

## Task:

Write a single line that prints whether `x` is **not**
equal to `y` using `!=` with `x = 10` and `y = 7`.

<br>

<Announcement type="info">
Note: <code>!=</code> is an <code>!</code> followed by an <code>=</code>.
</Announcement>

---
layout: section
---

# Decisions: if … then 

---

# B-IF-1 — Correct Age for a Movie 
 
## Scenario: 

Let adults in.  

## Task:

If `age >= 18`, print `Access granted`.  


## Guided steps:
1) Set `age = 18`. 
2) Write an `if` to print the message.

<br>

<Announcement type="info">
Note: <code>>=</code> is a <code>&gt;</code> followed by an <code>=</code>.
</Announcement>
---

# B-IF-2 — Nothing happens
 
## Scenario: 

A student expects output.  

<br>

<Announcement type="brainstorm">
If a condition is False in a single `if`, nothing in its block runs. 
<pre><code>
age = 20
if age > 21:
    print('You are allowed to enter')
</code></pre>
<br>

True or False?
</Announcement>

---

# B-IF-3 — Missing colon (Find the bug)
 
## Scenario: 

Your code won't run.  

## Task:

Fix the `if`.

```python
if 2 > 1
    print("yep")
```
---

# B-IF-4 — Indenting matters
 
## Scenario: 

A block of the code is misaligned (incorrectly indented).  

## Task:

Make the print only happen when `score > 50`.

```python
score = 51
if score > 50:
print("Passed")
```
---

# B-IF-5 — Truthy check (Write code)
 
## Scenario: 

A string indicates if a user typed anything.  

## Task:

If `name` is non-empty, print `Hi, <name>!` with `name = "Ada"`.

<Announcement type="info">
The <code><</code> and <code>></code> in <code>&lt;name></code> are
<br>placeholders to help you create the correct code.
</Announcement>

---
layout: section
---

# Decisions: if … then … else

---

# B-IFE-1 — Pass/Fail
 
## Scenario: 

Print `pass` if `mark >= 50`, else print `fail`.  

## Task:

Create a variable called `mark` and a value of `49` ( `mark = 49`).

Then use an `if … else` decision structure to print out `pass` or `fail`.

<br>
<Announcement type="info">
The <code>>=</code> is a <code>></code> followed by a <code>=</code>.
</Announcement>

---

# B-IFE-2 — Which branch?
 
## Scenario: 

Reading a friend’s code.  

## Predict the output:

What prints when we run this code?

```python
n = 0
if n:
    print("non-zero")
else:
    print("zero")
```
---

# B-IFE-3 — Misaligned else
 
## Scenario: 

The `else` is not working as it 'binds' to nothing.  

## Task:

Fix indentation, and missing colon (`:`) in the following code:  

```python
if 3 == 3
    print("eq")
    else:
        print("neq")
```

---
layout: section
---

# if … elif … else

---

# B-IFEE-1 — Light status (Write code)
 
## Scenario: 

Turn a light red/yellow/green.  

## Task:

Create a variable called `state` and set its value to `yellow` (`state = "yellow"`)

Depending on the `state` the `if..elif..elif..else` will print `Stop`,`Caution`, or `Go`.

- <span class="text-center text-black bg-red-500 w-24 p-1 px-2 mb-1 
  inline-block"> red 
</span> Stop 
- <span class="text-center text-black bg-yellow-500 w-24 p-1 px-2 mb-1 
inline-block"> yellow </span> 
Caution 
- <span class="text-center text-black bg-green-500 w-24 p-1 px-2 mb-1 
inline-block"> green </span> Go

---

# B-IFEE-2 — First match wins 
 
## Scenario: 

Overlapping conditions.  

## Predict the Output:

 What prints?  

```python
x = 10
if x > 5:
    print("big")
elif x > 8:
    print("bigger")
else:
    print("small")
```

---

# B-IFEE-3 — Missing elif colon
 
## Scenario: 

`SyntaxError` strikes again.  

## Task:

Find the bug and fix it.

```python
num = 2
if num == 1:
    print("one")
elif num == 2
    print("two")
else:
    print("other")
```

---
layout: section
---

# Nested ifs (3)

---

# B-NIF-1 — Student discount
 
## Scenario: 

Discount applies only to students with a valid card.  

## Task:

Write the code so that:
- If `is_student` is True, then if `has_card` is True, print `Discount 
applied`. 
- Otherwise, print nothing.  

## Guided steps:
1) Set `is_student = True`, `has_card = True`. 
2) Write nested `if`s.

---

# B-NIF-2 — Predict nested output
 
## Scenario: 

Checking login.  

##  Predict the output:

 What prints?

```python
logged_in = True
is_admin = False
if logged_in:
    if is_admin:
        print("Admin")
    print("Welcome")
```

---

# B-NIF-3 — Indent the nest 
 
## Scenario: 

A body fell out of its nest.  

## Task:

Find the bug and correct it.

Make this run without error and only print `Access` when both conditions are True.

```python
paid = True
has_ticket = True
if paid:
if has_ticket:
    print("Access")
```

---
layout: end
---

# That's All Folks!

## More puzzles to come
