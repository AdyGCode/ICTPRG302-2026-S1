# 🐍 02: Loops & Conditionals

## Introduction:
These problems will help you practice using `if`, `elif`, and `else`, as well as `while` or `for` loops.

Keep PEP8 in mind and make your code easy to read with meaningful variable names.

> Remember: code that you haven't run or tested is not trustworthy!

> [!Reference]
> 
> If, else, elif:
> ```python
> if some_condition:
>     pass # Do something
> elif some_other_condition:
>     pass # Do something else
> else:
>     pass # This is the default
> ```
> Definite, or `for` loops:
> ```python
> for loop_variable in some_sequence:
>   pass # Do something
> ```
> 
> Indefinite, or `while` loops:
> ```python
> loop_condition = True
> while loop_condtion:
>   pass # Do something
> ```

---

## Conditionals

### 1. Odd or Even
Ask the user for a number and print whether it is odd or even. Hint: Don't forget your `%` operator.

### 2. Largest of Three Numbers
Ask the user for three numbers and print the largest one.

### 3. Grade Calculator
Ask for a score (0–100) and print the grade:
- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: below 60

### 4. Password Checker
Ask the user to enter a password. If it matches a preset password, print "Access granted", otherwise print "Access denied".
(You decide what the password is.)

---

## Loops

### 5. Count from 1 to 10
Use a loop to print numbers from 1 to 10.

### 6. Countdown from 10
Use a loop to print numbers from 10 down to 1.

### 7. Print Even Numbers from 1 to 20
Use a loop to print all even numbers between 1 and 20.

### 8. Sum of First 10 Numbers
Use a loop to calculate and print the sum of numbers from 1 to 10.
Hint: You may like to use some kind of "accumulator" variable that sits outside the loop.

### 9. Multiplication Table
Ask the user for a number and print its multiplication table up to 12.

### 10. Factorial Calculator
Ask the user for a number and calculate its factorial using a loop.

### 11. Print All Characters in a Word
Ask the user for a word and print each character on a new line using a loop.

### 12. Draw a triangle
Ask the user for a "height", and then draw a triangle of that height:

```
How tall is your triangle? 4

*
**
***
****
```

---

## Putting it together: Loops and Conditionals

### 13. Number Guessing Game
Set a secret number. Ask the user to guess until they get it right. Give hints if the guess is too high or too low.

### 14. Count Vowels in a Word
Ask the user for a word and count how many vowels it contains.

### 15. Print All Prime Numbers from 1 to 50
Use a loop and conditionals to print all prime numbers between 1 and 50.
> Hint: You may need to nest loops.

### 16. FizzBuzz
Print numbers from 1 to 50. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz".
> Fun fact: this used to be a common entry-level interview problem.

### 17. Sum of Digits
Ask the user for a number and calculate the sum of its digits.
> Hint: You may want to take advantage of the string datatype, so that you are able to iterate over a number.

#### Sample:

Input:
```
Enter a number:
```
Assuming that the user input "123", we do "1 + 2 + 3"

Output:
```
The sum of digits is: 6
```

### 18. Count How Many Times a Specific Letter Appears
Ask the user for a word and a letter, then count how many times that letter appears in the word.
