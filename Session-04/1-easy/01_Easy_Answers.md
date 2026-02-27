
# 🌶️ Easy — Answers

## Commenting & Documenting Code
- **E-COM-1**: **False** — comments do not affect program execution/output.
- **E-COM-2**: **Lie: (3)** — a docstring is not required to be the last line of the file.
- **E-COM-3**: Example: `# First adds numbers; second concatenates strings` (any equivalent).
- **E-COM-4**: Add `#` before the first line, e.g., `# This line is just a reminder to fix the math later`.

## Displaying Results & Output
- **E-OUT-1**: `print("Welcome to Byte-Sized Shop!")`
- **E-OUT-2**: Prints `15` then `78`.
- **E-OUT-3**: `print("System online")`
- **E-OUT-4**:
  ```python
  total = 12.5
  print('Total: $', total)
  # or
  print('Total: $' + str(total))
  ```

## Variables & Naming Variables
- **E-VAR-1**: **True**
- **E-VAR-2**: e.g., `course = "Physics"`; then `print(course)`
- **E-VAR-3**: **Lie: (2)** — names cannot start with a number.
- **E-VAR-4**: Prints `3`.
- **E-VAR-5**:
  ```python
  nickname = "Ada"
  print('Hello, ' + nickname + '!')  # or: print('Hello,', nickname, '!')
  ```

## Expressions
- **E-EXP-1**: `14`
- **E-EXP-2**: `(2 + 3) * 4`
- **E-EXP-3**: **True**
- **E-EXP-4**: `print(int("7") + 5)` or `print("7" + str(5))`
- **E-EXP-5**:
  ```python
  a = 6
  b = 9
  print('a + b =', a + b)  # or: print('a + b = ' + str(a + b))
  ```

## Comparisons
- **E-CMP-1**: **False**
- **E-CMP-2**: Prints `False` then `True`.
- **E-CMP-3**:
  ```python
  x = 10
  y = 7
  print(x != y)
  ```

## if … then
- **E-IF-1**:
  ```python
  age = 18
  if age >= 18:
      print("Access granted")
  ```
- **E-IF-2**: **True**
- **E-IF-3**:
  ```python
  if 2 > 1:
      print("yep")
  ```
- **E-IF-4**:
  ```python
  score = 51
  if score > 50:
      print("Passed")
  ```
- **E-IF-5**:
  ```python
  name = "Ada"
  if name:
      print('Hi, ' + name + '!')
  ```

## if … else
- **E-IFE-1**:
  ```python
  mark = 49
  if mark >= 50:
      print("Pass")
  else:
      print("Fail")
  ```
- **E-IFE-2**: Prints `zero`.
- **E-IFE-3**:
  ```python
  if 3 == 3:
      print("eq")
  else:
      print("neq")
  ```

## if … elif … else
- **E-IFEE-1**:
  ```python
  state = "yellow"
  if state == "red":
      print("Stop")
  elif state == "yellow":
      print("Caution")
  else:
      print("Go")
  ```
- **E-IFEE-2**: Prints `big`.
- **E-IFEE-3**:
  ```python
  num = 2
  if num == 1:
      print("one")
  elif num == 2:
      print("two")
  else:
      print("other")
  ```

## Nested ifs
- **E-NIF-1**:
  ```python
  is_student = True
  has_card = True
  if is_student:
      if has_card:
          print("Discount applied")
  ```
- **E-NIF-2**: Prints `Welcome` only.
- **E-NIF-3**:
  ```python
  paid = True
  has_ticket = True
  if paid:
      if has_ticket:
          print("Access")
  ```
