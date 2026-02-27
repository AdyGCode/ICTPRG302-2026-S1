---
title: Extreme Puzzles — ICTPRG302
---
---

# 🌶️🌶️🌶️🌶️ Extreme Puzzles — ICTPRG302 Foundations (Python)

---
**Legend**: 🌶️ Easy · 🌶️🌶️ Medium · 🌶️🌶️🌶️ Hard · 🌶️🌶️🌶️🌶️ Extreme  
---
**Language**: Python 3  
---
**Activity types**: True/False · Two truths & one lie · Find the bug · Predict the output · Fill-in · Write code · Guided steps


---
# Displaying Results & Output (1)
---

---
**X-OUT-1 — Mini report (Write code)**  
*Scenario*: Generate a one-line summary with embedded calculations and formatting.  
---
**Task**: With `items=3`, `avg=12.3456`, print: `3 items · avg $12.35` **exactly** (use an f-string and formatting).

---

---
# Variables & Naming Variables (1)
---

---
**X-VAR-1 — Legal or not? (Two truths & one lie)**  
*Scenario*: Security review of names.  
Pick the **one lie**:  
1) `__hidden_value` is a valid identifier.  
2) `total$` is valid in Python.  
3) `_cache2` is valid.

---

---
# Expressions (1)
---

---
**X-EXP-1 — Expression only (Write code)**  
*Scenario*: One-liner requirement.  
---
**Task**: In **one** expression (no variables), compute the average of `4, 10, 6` and floor it to an integer.

---

---
# Comparisons (1)
---

---
**X-CMP-1 — Safe equality (Write code)**  
*Scenario*: Avoid float equality pitfalls.  
---
**Task**: Using `abs`, print whether `0.1 + 0.2` is within `1e-9` of `0.3`.

---

---
# if … then (1)
---

---
**X-IF-1 — Single-if guard (Write code)**  
*Scenario*: Only greet when name is non-empty **and** not just spaces.  
---
**Task**: With `name = "  "`, write a single `if` that prints `Hello!` only when name has non-space characters.

---

---
# if … else (1)
---

---
**X-IFE-1 — Sign label (Write code)**  
*Scenario*: Label numbers as `pos`, `neg`, or `zero` using **only** `if … else` (no `elif`).  
---
**Task**: For `n = 0`, print `zero`.

---

---
# if … elif … else (1)
---

---
**X-IFEE-1 — Tax bands (Write code)**  
*Scenario*: Compute a simple tax band label: `High (>= 90)`, `Mid (>= 60)`, else `Low`.  
---
**Task**: With `score = 59.999`, print `Low`.

---

---
# Nested ifs (1)
---

---
**X-NIF-1 — Triple gate (Write code · Guided steps)**  
*Scenario*: Access allowed only when (`logged_in`) and ( `verified` and not `suspended`).  
---
**Task**: Use nested `if`s to print `OK` for `logged_in=True`, `verified=True`, `suspended=False`.  
---
**Guided steps**: (1) Check `logged_in`. (2) Inside, check `verified`. (3) Inside, check `not suspended`.
