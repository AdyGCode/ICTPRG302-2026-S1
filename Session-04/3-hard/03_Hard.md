
# 🌶️🌶️🌶️ Hard Puzzles — ICTPRG302 Foundations (Python)

**Legend**: 🌶️ Easy · 🌶️🌶️ Medium · 🌶️🌶️🌶️ Hard · 🌶️🌶️🌶️🌶️ Extreme  
**Language**: Python 3  
**Activity types**: True/False · Two truths & one lie · Find the bug · Predict the output · Fill-in · Write code · Guided steps


## Commenting & Documenting Code (1)

**H-COM-1 — Improve the doc (Write code)**  
*Scenario*: The function works, but documentation is unhelpful.  
**Task**: Replace the comment with a proper docstring that explains edge cases (e.g., empty list).  
```python
def average(nums):
    # returns avg
    return sum(nums) / len(nums)
```

---

## Displaying Results & Output (4)

**H-OUT-1 — Table with headers (Write code)**  
*Scenario*: Show a mini table with headers and rows aligned:  
```
Item      Qty   Price
Apples     3    $2.10
Bread      1    $3.20
```
**Task**: Print exactly the layout above using alignment (spaces or formatting).

**H-OUT-2 — Precision control (Predict the output)**  
*Scenario*: Currency rounding check.  
**Q**: What prints?  
```python
value = 1/3
print(f"{value:.2f}")
print(f"{value:.4f}")
```

**H-OUT-3 — Money format (Write code)**  
*Scenario*: Show a customer's total **with two decimals**.  
**Task**: Set `total = 12.5` and print `Total: $12.50` **using an f-string**.

**H-OUT-4 — Aligned receipt (Write code)**  
*Scenario*: Clean alignment with expressions embedded.  
**Task**: Print the lines below using **f-strings** so names are left-padded to width 8, and prices show two decimals.  
```
Tea      $2.50
Muffin   $4.00
Total    $6.50
```

---

## Variables & Naming Variables (3)

**H-VAR-1 — Unpack and ignore (Write code)**  
*Scenario*: You only need the middle value.  
**Task**: Given `t = (10, 20, 30)`, unpack into `_`, `m`, `_` and print `m`.

**H-VAR-2 — Rebinding vs mutation (True/False)**  
*Scenario*: You discuss lists.  
**Q**: Doing `x = x + [4]` mutates the original list `x`. True or False?

**H-VAR-3 — Keyword trap (Find the bug)**  
*Scenario*: A variable shadows a built-in.  
**Task**: Fix so the code prints the length of the list, not the function object.  
```python
len = [1, 2, 3]
print(len(len))
```

---

## Expressions (3)

**H-EXP-1 — Integer division vs floor (Predict the output)**  
*Scenario*: Negative values matter.  
**Q**: What do these print?  
```python
print(-3 // 2)
print(int(-3 / 2))
```

**H-EXP-2 — Combined ops (Write code)**  
*Scenario*: Compute `result = (a + b)**2 - (a*b)%3` for `a=4`, `b=5` and print it.

**H-EXP-3 — String math (Find the bug)**  
*Scenario*: User input must be added numerically.  
**Task**: Fix to sum two inputs as numbers.  
```python
x = input("x: ")
y = input("y: ")
print("sum:", x + y)
```

---

## Comparisons (1)

**H-CMP-1 — Identity vs equality (Two truths & one lie)**  
*Scenario*: Debugging a cache.  
Pick the **one lie**:  
1) `==` checks value equality.  
2) `is` checks object identity.  
3) For small integers, `a is b` is always safe and recommended.

---

## if … then (2)

**H-IF-1 — Early exit (Write code)**  
*Scenario*: Stop if `errors > 0` by printing `Fix errors` and **not** printing anything else. Otherwise print `Proceed`. Use only a single `if` and regular flow.

**H-IF-2 — Range check (Write code)**  
*Scenario*: Print `In range` if `0 <= x < 10`. Start with `x = -1` then `x = 5` and demonstrate both outcomes using only single `if` statements.

---

## if … else (1)

**H-IFE-1 — Absolute value (Write code)**  
*Scenario*: Implement absolute value logic.  
**Task**: Given `n = -7`, use `if … else` to print `7`.

---

## if … elif … else (1)

**H-IFEE-1 — Shipping tiers (Write code)**  
*Scenario*: Calculate shipping label: `Free (>= 100)`, `Standard (>= 50)`, else `Basic`.  
**Task**: With `total = 75`, print `Standard`.

---

## Nested ifs (1)

**H-NIF-1 — Deep condition (Write code · Guided steps)**  
*Scenario*: Allow lab access if `day == 'Mon'` **and** (`staff` or (`student` and `has_card`)).  
**Task**: Use nested `if`s to print `Access granted` for `day='Mon'`, `student=True`, `has_card=True`, `staff=False`.  
**Guided steps**: (1) Check day. (2) Inside, check role(s). (3) Print only when rules match.
