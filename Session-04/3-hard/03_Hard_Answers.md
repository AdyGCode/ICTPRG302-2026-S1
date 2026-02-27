
# 🌶️🌶️🌶️ Hard — Answers

## Commenting & Documenting Code
- **H-COM-1**: Example:
  ```python
  def average(nums):
      """Return the arithmetic mean of nums.

      Returns 0.0 for an empty list to avoid ZeroDivisionError.
      """
      return sum(nums) / len(nums) if nums else 0.0
  ```

## Displaying Results & Output
- **H-OUT-1**:
  ```python
  print(f"{'Item':8} {'Qty':>3}   Price")
  print(f"{'Apples':8} {3:>3}   $2.10")
  print(f"{'Bread':8} {1:>3}   $3.20")
  ```
- **H-OUT-2**: Prints `0.33` then `0.3333`.
- **H-OUT-3**:
  ```python
  total = 12.5
  print(f"Total: ${total:.2f}")
  ```
- **H-OUT-4**:
  ```python
  print(f"{'Tea':8} ${2.5:.2f}")
  print(f"{'Muffin':8} ${4.0:.2f}")
  print(f"{'Total':8} ${6.5:.2f}")
  ```

## Variables & Naming Variables
- **H-VAR-1**:
  ```python
  t = (10, 20, 30)
  _, m, _ = t
  print(m)
  ```
- **H-VAR-2**: **False** — that rebinding creates a new list; it does not mutate the original.
- **H-VAR-3**:
  ```python
  data = [1, 2, 3]
  print(len(data))
  ```

## Expressions
- **H-EXP-1**: Prints `-2` then `-1`.
- **H-EXP-2**:
  ```python
  a, b = 4, 5
  result = (a + b) ** 2 - (a * b) % 3
  print(result)
  ```
- **H-EXP-3**:
  ```python
  x = int(input("x: "))
  y = int(input("y: "))
  print("sum:", x + y)
  ```

## Comparisons
- **H-CMP-1**: **Lie: (3)** — relying on `is` for value comparison is not recommended.

## if … then
- **H-IF-1**:
  ```python
  errors = 1
  if errors > 0:
      print("Fix errors")
  else:
      print("Proceed")
  ```
- **H-IF-2**:
  ```python
  x = -1
  if 0 <= x < 10:
      print("In range")
  x = 5
  if 0 <= x < 10:
      print("In range")
  ```

## if … else
- **H-IFE-1**:
  ```python
  n = -7
  if n < 0:
      print(-n)
  else:
      print(n)
  ```

## if … elif … else
- **H-IFEE-1**:
  ```python
  total = 75
  if total >= 100:
      print("Free")
  elif total >= 50:
      print("Standard")
  else:
      print("Basic")
  ```

## Nested ifs
- **H-NIF-1**:
  ```python
  day = 'Mon'
  student = True
  has_card = True
  staff = False

  if day == 'Mon':
      if staff:
          print('Access granted')
      else:
          if student and has_card:
              print('Access granted')
  ```
