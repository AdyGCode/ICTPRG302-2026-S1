
# 🌶️🌶️ Medium — Answers

## Commenting & Documenting Code
- **M-COM-1**: Example:
  ```python
  def area(width, height):
      """Return the rectangle area.

      Parameters:
          width (float): The width of the rectangle.
          height (float): The height of the rectangle.
      Returns:
          float: Area as width * height.
      """
      return width * height
  ```
- **M-COM-2**: **Lie: (3)** — file-level docstrings don't need to list every import.

## Displaying Results & Output
- **M-OUT-1**:
  ```python
  print('Tea'   + ' ' * 6 + '$2.50')
  print('Muffin' + ' ' * 3 + '$4.00')
  print('Total'  + ' ' * 4 + '$6.50')
  ```
- **M-OUT-2**: `3 + 4 = 7`
- **M-OUT-3**:
  ```python
  print("She said, "Hi"")
  ```

## Variables & Naming Variables
- **M-VAR-1**:
  ```python
  a, b = b, a
  ```
- **M-VAR-2**: **False** — reassignment in the same scope updates the same variable.
- **M-VAR-3**: **Lie: (3)** — `l` and `O` can be confusing; avoid them.
- **M-VAR-4**:
  ```python
  PI = 3.14159
  r = 2
  print(round(PI * r * r, 2))  # or: print(PI * r * r)
  ```

## Expressions
- **M-EXP-1**: Typically prints `2.67` due to binary rounding of 2.675.
- **M-EXP-2**:
  ```python
  a = "5"; b = "7"
  print("Sum:", int(a) + int(b))
  ```
- **M-EXP-3**:
  ```python
  n = 9
  print(n % 3 == 0, n ** 2)
  ```
- **M-EXP-4**: **Lie: (3)** — multiplication happens before addition.

## Comparisons
- **M-CMP-1**:
  ```python
  rating = 5
  print(1 <= rating <= 5)
  ```
- **M-CMP-2**: **False** — due to floating-point representation.

## if … then
- **M-IF-1**: Example:
  ```python
  total = 49.99
  if total >= 50:
      print("Free shipping!")
  total = 50
  if total >= 50:
      print("Free shipping!")
  ```
- **M-IF-2**:
  ```python
  if not token:
      print("Missing token")
  ```
- **M-IF-3**:
  ```python
  total = 0
  x = 3
  if x > 0:
      total += x
  print(total)
  ```

## if … else
- **M-IFE-1**:
  ```python
  n = 12
  if n % 2 == 0:
      print("even")
  else:
      print("odd")
  ```
- **M-IFE-2**: Prints `empty`.

## if … elif … else
- **M-IFEE-1**:
  ```python
  score = 76
  if score >= 85:
      print("HD")
  elif score >= 75:
      print("D")
  elif score >= 65:
      print("C")
  elif score >= 50:
      print("P")
  else:
      print("N")
  ```
- **M-IFEE-2**: **True**

## Nested ifs
- **M-NIF-1**:
  ```python
  logged_in = True
  paid = True
  if logged_in:
      if paid:
          print("Download ready")
  ```
- **M-NIF-2**: Prints `C` only.
