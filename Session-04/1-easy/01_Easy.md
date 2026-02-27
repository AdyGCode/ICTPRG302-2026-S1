
# 🌶️ Easy Puzzles — ICTPRG302 Foundations (Python)

**Legend**: 🌶️ Easy · 🌶️🌶️ Medium · 🌶️🌶️🌶️ Hard · 🌶️🌶️🌶️🌶️ Extreme  
**Language**: Python 3  
**Activity types**: True/False · Two truths & one lie · Find the bug · Predict the output · Fill-in · Write code · Guided steps


## Commenting & Documenting Code (4)

**E-COM-1 — Why comment? (True/False)**  
*Scenario*: You're handing a tiny script to a classmate. They ask if comments affect how the program runs.  
**Q**: Comments (lines starting with `#`) change the program's output. True or False?

**E-COM-2 — Docstring vs. comment (Two truths & one lie)**  
*Scenario*: Your team wants to capture function purpose.  
**Task**: Pick the **one lie**:  
1) A docstring sits inside triple quotes right after a `def`.  
2) `#` comments are for inline notes that are **not** executed.  
3) A docstring must always be on the last line of the file.

**E-COM-3 — Add a helpful comment (Write code · Guided steps)**  
*Scenario*: A junior keeps confusing addition with concatenation.  
**Task**: Add **one** comment that explains the difference for the two lines below.  
**Guided steps**: (1) Read each `print`. (2) Write one comment **above** the pair explaining the difference.  
```python
print(3 + 4)
print("3" + "4")
```

**E-COM-4 — Find the bug: missing `#` (Find the bug)**  
*Scenario*: Someone meant to leave themselves a note, but the program crashes.  
**Task**: Fix the error by making the note a real comment.  
```python
This line is just a reminder to fix the math later
print(2 + 2)
```

---

## Displaying Results & Output (4)

**E-OUT-1 — Hello shop! (Write code)**  
*Scenario*: A kiosk should greet users.  
**Task**: Write **one** line that prints `Welcome to Byte-Sized Shop!`.

**E-OUT-2 — Numbers vs. strings (Predict the output)**  
*Scenario*: You audit two lines from last year's code.  
**Q**: What do these print?  
```python
print(7 + 8)
print("7" + "8")
```

**E-OUT-3 — Print needs brackets (Find the bug)**  
*Scenario*: A Python 2 snippet was pasted into your Python 3 file.  
**Task**: Fix it.  
```python
print "System online"
```

**E-OUT-4 — Show a total (Guided steps)**  
*Scenario*: Show a customer's total.  
**Task**: Create `total = 12.5` and print `Total: $` followed by the total (no need for two decimals).  
**Guided steps**: (1) Create `total = 12.5`. (2) Print using either `print('Total: $', total)` or concatenation.

---

## Variables & Naming Variables (5)

**E-VAR-1 — Valid name? (True/False)**  
*Scenario*: You're naming variables for a library app.  
**Q**: `book_count` is a valid variable name in Python. True or False?

**E-VAR-2 — Don't fight keywords (Find the bug)**  
*Scenario*: Someone used a reserved word as a name.  
**Task**: Rename the variable to something legal.  
```python
class = "Physics"
print(class)
```

**E-VAR-3 — Short and clear (Two truths & one lie)**  
*Scenario*: Team style guide discussion.  
Pick the **one lie**:  
1) Names should be descriptive but concise.  
2) Variable names can start with a number.  
3) `snake_case` is common in Python.

**E-VAR-4 — Reassign then print (Predict the output)**  
*Scenario*: A counter gets updated.  
**Q**: What prints?  
```python
count = 1
count = count + 2
print(count)
```

**E-VAR-5 — Set and show (Guided steps)**  
*Scenario*: Track a user's nickname.  
**Task**: Create a variable `nickname` with your name and print `Hello, <name>!` using concatenation or `print('Hello,', nickname, '!')`.  
**Guided steps**: (1) Make the variable. (2) Print the message.

---

## Expressions (5)

**E-EXP-1 — Order of operations (Predict the output)**  
*Scenario*: You review a formula.  
**Q**: What does this print?  
```python
print(2 + 3 * 4)
```

**E-EXP-2 — Force the order (Fill-in)**  
*Scenario*: You need the result `20` using the same numbers as above.  
**Task**: Add parentheses to `2 + 3 * 4` so it evaluates to `20`.

**E-EXP-3 — Division facts (True/False)**  
*Scenario*: A teammate mixes `/` and `//`.  
**Q**: In Python, `5 / 2` gives a float and `5 // 2` gives an int. True or False?

**E-EXP-4 — Mix types (Find the bug)**  
*Scenario*: A quick sum fails.  
**Task**: Fix the error so it prints `12`.  
```python
print("7" + 5)
```

**E-EXP-5 — Tiny calculator (Guided steps)**  
*Scenario*: A kiosk adds two numbers for users.  
**Task**: Set `a = 6`, `b = 9`, then print the label and result on one line (e.g., `a + b = 15`) **without** f-strings.  
**Guided steps**: (1) Create variables. (2) Use `print('a + b =', a + b)` or concatenation.

---

## Comparisons (3)

**E-CMP-1 — Same value? (True/False)**  
*Scenario*: You compare user input with a number.  
**Q**: `5 == "5"` evaluates to True. True or False?

**E-CMP-2 — Boundary check (Predict the output)**  
*Scenario*: Validate ticket age.  
**Q**: What prints?  
```python
print(3 < 3)
print(3 <= 3)
```

**E-CMP-3 — Not equal (Write code)**  
*Scenario*: A quick sanity check.  
**Task**: Write a single line that prints whether `x` is **not** equal to `y` using `!=` with `x = 10` and `y = 7`.

---

## if … then (single `if`) (5)

**E-IF-1 — Movie age gate (Guided steps)**  
*Scenario*: Let adults in.  
**Task**: If `age >= 18`, print `Access granted`.  
**Guided steps**: (1) Set `age = 18`. (2) Write an `if` to print the message.

**E-IF-2 — Nothing happens (True/False)**  
*Scenario*: A student expects output.  
**Q**: If a condition is False in a single `if`, nothing in its block runs. True or False?

**E-IF-3 — Missing colon (Find the bug)**  
*Scenario*: Your code won't run.  
**Task**: Fix the `if`.  
```python
if 2 > 1
    print("yep")
```

**E-IF-4 — Indentation matters (Find the bug)**  
*Scenario*: A block is misaligned.  
**Task**: Make the print only happen when `score > 50`.  
```python
score = 51
if score > 50:
print("Passed")
```

**E-IF-5 — Truthy check (Write code)**  
*Scenario*: A string indicates if a user typed anything.  
**Task**: If `name` is non-empty, print `Hi, <name>!` with `name = "Ada"` (no f-strings).

---

## if … then … else (3)

**E-IFE-1 — Pass/Fail (Write code)**  
*Scenario*: Print pass if `mark >= 50`, else print fail.  
**Task**: Use `if … else` with `mark = 49`.

**E-IFE-2 — Which branch? (Predict the output)**  
*Scenario*: Reading a friend’s code.  
**Q**: What prints?  
```python
n = 0
if n:
    print("non-zero")
else:
    print("zero")
```

**E-IFE-3 — Misaligned else (Find the bug)**  
*Scenario*: The `else` binds to nothing.  
**Task**: Fix indentation/colon.  
```python
if 3 == 3
    print("eq")
    else:
        print("neq")
```

---

## if … elif … else (3)

**E-IFEE-1 — Light status (Write code)**  
*Scenario*: Turn a light red/yellow/green.  
**Task**: With `state = "yellow"`, print `Stop`, `Caution`, or `Go` using `if/elif/else`.

**E-IFEE-2 — First match wins (Predict the output)**  
*Scenario*: Overlapping conditions.  
**Q**: What prints?  
```python
x = 10
if x > 5:
    print("big")
elif x > 8:
    print("bigger")
else:
    print("small")
```

**E-IFEE-3 — Missing elif colon (Find the bug)**  
*Scenario*: SyntaxError strikes again.  
**Task**: Fix it.  
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

## Nested ifs (3)

**E-NIF-1 — Student discount (Write code · Guided steps)**  
*Scenario*: Discount applies only to students with a valid card.  
**Task**: If `is_student` is True, then if `has_card` is True, print `Discount applied`. Otherwise print nothing.  
**Guided steps**: (1) Set `is_student = True`, `has_card = True`. (2) Write nested `if`s.

**E-NIF-2 — Predict nested output (Predict the output)**  
*Scenario*: Checking login.  
**Q**: What prints?  
```python
logged_in = True
is_admin = False
if logged_in:
    if is_admin:
        print("Admin")
    print("Welcome")
```

**E-NIF-3 — Indent the nest (Find the bug)**  
*Scenario*: A body fell out of its nest.  
**Task**: Make this run without error and only print `Access` when both conditions are True.  
```python
paid = True
has_ticket = True
if paid:
if has_ticket:
    print("Access")
```
