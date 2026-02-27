---
title: Medium Puzzles — ICTPRG302
---
---

# 🌶️🌶️ Medium Puzzles — ICTPRG302 Foundations (Python)

---
**Legend**: 🌶️ Easy · 🌶️🌶️ Medium · 🌶️🌶️🌶️ Hard · 🌶️🌶️🌶️🌶️ Extreme  
---
**Language**: Python 3  
---
**Activity types**: True/False · Two truths & one lie · Find the bug · Predict the output · Fill-in · Write code · Guided steps


---
# Commenting & Documenting Code (2)
---

---
**M-COM-1 — Good docstring (Write code · Guided steps)**  
*Scenario*: Your function will be shared with new hires.  
---
**Task**: Add a docstring that states **purpose**, **parameters**, and **return**.  
```python
def area(width, height):
    return width * height
```

---
**M-COM-2 — Two truths & one lie (Documentation)**  
*Scenario*: Code review standards.  
Pick the **one lie**:  
1) Docstrings can be accessed at runtime via `help()` or `__doc__`.  
2) Inline comments should describe *why* more than *what*.  
3) A file-level docstring must list every import statement.

---

---
# Displaying Results & Output (3)
---

---
**M-OUT-1 — Neat lines (Write code)**  
*Scenario*: Print a tiny receipt with neat lines.  
---
**Task**: Print the three lines below using one `print` each so prices appear neatly underneath each other using simple spaces.  
```
Tea      $2.50
Muffin   $4.00
Total    $6.50
```

---
**M-OUT-2 — Concatenate math (Predict the output)**  
*Scenario*: A teammate wrote an inline calc without f-strings.  
---
**Q**: What prints?  
```python
x = 3
y = 4
print(str(x) + " + " + str(y) + " = " + str(x + y))
```

---
**M-OUT-3 — Escape hatch (Find the bug)**  
*Scenario*: Quotes in strings.  
---
**Task**: Make this print **exactly**: `She said, "Hi"`.  
```python
print("She said, "Hi"")
```

---

---
# Variables & Naming Variables (4)
---

---
**M-VAR-1 — Swap values (Write code)**  
*Scenario*: Two counters are mixed up.  
---
**Task**: Swap `a` and `b` using **one** line.  
```python
a, b = 1, 2
# your code here
print(a, b)  # expect 2 1
```

---
**M-VAR-2 — Shadow boxing (True/False)**  
*Scenario*: You debate reusing names.  
---
**Q**: Reassigning `x` inside the same scope creates a new variable, leaving the old `x` unchanged. True or False?

---
**M-VAR-3 — Clear names (Two truths & one lie)**  
*Scenario*: Naming review.  
Pick the **one lie**:  
1) Avoid single-letter names for non-trivial values.  
2) Prefer names that communicate units (e.g., `duration_ms`).  
3) Using `l` and `O` is fine; they never look like `1` and `0`.

---
**M-VAR-4 — Constant-ish (Write code)**  
*Scenario*: Team uses uppercase for constants.  
---
**Task**: Create `PI = 3.14159` and print the area of a circle of radius `2`. (Optionally use `round(..., 2)`.)

---

---
# Expressions (4)
---

---
**M-EXP-1 — Rounding differences (Predict the output)**  
*Scenario*: A price needs rounding.  
---
**Q**: What prints?  
```python
price = 2.675
print(round(price, 2))
```

---
**M-EXP-2 — Cast it right (Find the bug)**  
*Scenario*: Input comes as text.  
---
**Task**: Fix so it prints `Sum: 12`.  
```python
a = "5"
b = "7"
print("Sum:", a + b)
```

---
**M-EXP-3 — Mod and power (Write code)**  
*Scenario*: Check if `n` is a multiple of 3 and print `n^2`.  
---
**Task**: With `n = 9`, print `True 81` in one line separated by a space (use `%` and `**`).

---
**M-EXP-4 — Precedence puzzle (Two truths & one lie)**  
*Scenario*: Quick quiz.  
Pick the **one lie**:  
1) `**` has higher precedence than `*` and `+`.  
2) `()` can change evaluation order.  
3) `a + b * c` adds first, then multiplies.

---

---
# Comparisons (2)
---

---
**M-CMP-1 — Chain it (Write code)**  
*Scenario*: Validate a rating 1–5 inclusive.  
---
**Task**: Using **one** comparison, print whether `rating = 5` is in range.

---
**M-CMP-2 — Floating point gotcha (True/False)**  
*Scenario*: Comparing calculations.  
---
**Q**: `0.1 + 0.2 == 0.3` evaluates to True. True or False?

---

---
# if … then (3)
---

---
**M-IF-1 — Minimum spend (Write code)**  
*Scenario*: Offer free shipping for `total >= 50`.  
---
**Task**: With `total = 49.99`, print nothing; with `total = 50`, print `Free shipping!`.

---
**M-IF-2 — Guard clause (Write code)**  
*Scenario*: Only proceed if `token` is not empty.  
---
**Task**: If `token` is falsy, print `Missing token`.

---
**M-IF-3 — Count conditionally (Guided steps)**  
*Scenario*: Tally only positives.  
---
**Task**: If `x > 0`, add `x` to `total` and print `total`. Start with `total = 0` and `x = 3`.

---

---
# if … else (2)
---

---
**M-IFE-1 — Even or odd (Write code)**  
*Scenario*: Label numbers.  
---
**Task**: With `n = 12`, print `even`; otherwise `odd`.

---
**M-IFE-2 — Truthiness (Predict the output)**  
*Scenario*: Review container checks.  
---
**Q**: What prints?  
```python
items = []
if items:
    print("has items")
else:
    print("empty")
```

---

---
# if … elif … else (2)
---

---
**M-IFEE-1 — Grade bands (Write code)**  
*Scenario*: Translate `score` to bands: `HD >= 85`, `D >= 75`, `C >= 65`, `P >= 50`, else `N`.  
---
**Task**: With `score = 76`, print `D`.

---
**M-IFEE-2 — Order matters (True/False)**  
*Scenario*: You discuss condition ordering.  
---
**Q**: In `if/elif/else`, the **first** True condition runs and the rest are skipped. True or False?

---

---
# Nested ifs (2)
---

---
**M-NIF-1 — Double-check (Write code)**  
*Scenario*: Allow download only if `logged_in` and `paid`.  
---
**Task**: Use nested `if`s to print `Download ready` for `logged_in=True`, `paid=True`.

---
**M-NIF-2 — Predict nested (Predict the output)**  
*Scenario*: Feature flag.  
---
**Q**: What prints?  
```python
flag = False
beta = True
if flag:
    if beta:
        print("A")
    else:
        print("B")
print("C")
```
