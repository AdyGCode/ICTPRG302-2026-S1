
# 🌶️🌶️🌶️🌶️ Extreme — Answers

## Displaying Results & Output
- **X-OUT-1**:
  ```python
  items = 3
  avg = 12.3456
  print(f"{items} items · avg ${avg:.2f}")
  ```

## Variables & Naming Variables
- **X-VAR-1**: **Lie: (2)** — `total$` is **not** a valid identifier in Python.

## Expressions
- **X-EXP-1**:
  ```python
  print((4 + 10 + 6) // 3)
  ```

## Comparisons
- **X-CMP-1**:
  ```python
  print(abs(0.1 + 0.2 - 0.3) < 1e-9)
  ```

## if … then
- **X-IF-1**:
  ```python
  name = "  "
  if name.strip():
      print("Hello!")
  ```

## if … else
- **X-IFE-1**:
  ```python
  n = 0
  if n == 0:
      print("zero")
  else:
      if n > 0:
          print("pos")
      else:
          print("neg")
  ```

## if … elif … else
- **X-IFEE-1**:
  ```python
  score = 59.999
  if score >= 90:
      print("High")
  elif score >= 60:
      print("Mid")
  else:
      print("Low")
  ```

## Nested ifs
- **X-NIF-1**:
  ```python
  logged_in=True
  verified=True
  suspended=False
  if logged_in:
      if verified:
          if not suspended:
              print("OK")
  ```
