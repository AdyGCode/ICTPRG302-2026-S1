# 🐍 03: Functions

---

## Instructions:
Each problem below asks you to write one or more functions to solve a task.
Try to keep your functions small, focused, and reusable.
Think about what your functions will return, if anything.

Many of these exercises may be packaging up your previous code into standalone functions, so this may not take very long at all!

There is little "new material".  This is all to get you used to writing and invoking functions.  The muscle memory of typing these functions will also help you to remember the `syntax`.

Keep PEP8 in mind and make your code easy to read with meaningful variable names.

> Remember: code that you haven't run or tested is not trustworthy!

> [!Reference]
> User-defined functions are written with the `def` keyword, eg:
>
> ```python
> def your_function():
>     pass # Your code
> ```
> You can give your functions "parameters", which are like local variables for that function:
>
> ```python
> def your_function_but_with_parameters(parameter_a, parameter_b):
>     print(parameter_a, parameter_b)
> ```
> Functions without parameters are invoked by name and brackets:
> ```python
> your_function()
>```
> Functions with parameters need arguments:
> ```python
> your_function_but_with_parameters("Hello", "World")
> ```
> 
> Importantly, functions can return values, which can be assigned back to variables and/or used.
> 
> ```python
> def your_function():
> 	return "Some value"
> 
> print(your_function())	# Outputs: Some value
> ```

---

### 1. Greeting Function 
🌶️
Write a function `greet(name)` that prints a personalized greeting.
Use it to greet three different people.
(These can be fixed names, such as "Martha", "Knuth", "Allie")

### 2. Add Two Numbers 
🌶️
Write a function `add(a, b)` that returns the sum of two numbers.
Use it to add several pairs of numbers arbitrarily (eg: `add(2,5)`, `add(6,10)`)
> Extension 🌶️🌶️🌶️: Add all numbers between 1 and 10 using nested loops. 
> (eg, 1+1, 1+2, 1+3 ... 10+10)

### 3. Check Even or Odd 
🌶️🌶️
Write a function `is_even(n)` that returns `True` if a number is even, otherwise `False`.
Use it to check a series of numbers from 1 - 10

### 4. Find the Largest of Three 
🌶️🌶️
Write a function `largest(a, b, c)` that returns the largest of three numbers.

### 5. Convert Celsius to Fahrenheit 
🌶️🌶️
Write a function `c_to_f(celsius)` that converts Celsius to Fahrenheit.
Use it to convert a series of temperatures, from 20 to 40.

### 6. Count Vowels in a Word 
🌶️🌶️
Write a function `count_vowels(word)` that returns the number of vowels in a word.

### 7. Multiplication Table 
🌶️
Write a function `print_table(n)` that prints the multiplication table for a number up to 10.

### 8. FizzBuzz Function 
🌶️🌶️🌶️
Write a function `fizzbuzz(number)` that returns "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, or the number.  Then use this function to print out the fizzbuzz result for the first 100 numbers.  

### 9. Prime Checker 
🌶️🌶️🌶️
Write a function `is_prime(n)` that returns `True` if a number is prime, otherwise `False`.
Use it to print all prime numbers from 1 to 50.

### 10. Factorial Calculator 
🌶️
Write a function `factorial(n)` that returns the factorial of a number.

#### 10A: **Optional** Extension 
🌶️🌶️🌶️
Don't use a loop: write a ⚠️ recursive function ⚠️ (which calls itself!).

> [! Important]
> Recursive functions are a somewhat advanced topic, because they can be difficult to write well.  A badly written recursive function will quickly exceed the ability of your computer to deal with it. (Python will hold your hand, however.)
>
> They are not *generally* considered good practice, but are fun in this training setting.
> ```python
> def sum_until_hundred(number):
> 	if(number >= 100):
> 		return 100
> 	return number + sum_until_hundred(number + 1)	
> ```
### 11. Fibonacci Sequence
Write a function `fibonacci(n)` which gives the "Nth" fibonacci number in a sequence.
A. Use a loop 🌶️
B. (Optional) Write this as a ⚠️ recursive function ⚠️ 🌶️🌶️🌶️

> [!Note] 
> The fibonacci sequence is a series of numbers that start with 1, 1, and add the two previous numbers together to make the next number.
> For example, the first 8 fibonacci numbers are:
> 1, 1, 2, 3, 5, 8, 13, 21



