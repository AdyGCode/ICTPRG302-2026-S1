# 🐍 07: Loops, Functions, and Dictionary

## Introduction:
These problems will help you practice using `if`, `elif`, and `else`, as well as `while` or `for` loops.

Keep PEP8 in mind and make your code easy to read with meaningful variable names.

> Remember: code that you haven't run or tested is not trustworthy!

> [!Loops]
> 
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

> [!Functions]
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
>     # Your implementation goes here.  This is printing as an example.
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
>  Functions can return values, using the `return` keyword.  This returned value can be 
>  A. Put into a variable
>  B. Chained into some other expression
>
> ```python
> def give_two():
>     return 2
>
> some_number = give_two()
> print(some_number * 8)
> 
> # This is similar, but I've just chained the function call straight in, rather than assigning a variable:
> print(give_two() * 2)
> ```   

> [!Dictionaries]
> ```python
> a_dict = { "description": "A collection with structured keys", "score": 123 }
>```
> Accessed by key/name:
> ```python
print(a_dict["score"])
> >>> 123
> ```
>
>  Don't forget that you can safely retrieve values from dictionaries with `get()`

---
### Warmups

> [!Instructions]
> Write functions named as following:
#### even_descending(number)
Write a function to return a list of all even numbers between 0 and number.  Use a loop to build the list.
```python
def even_descending(number):
	final_list = []
	# Your code here
	return final_list
```
#### sum_to(maximum)
Write a loop that sums all numbers from zero to the maximum.
```python
def sum_to(number):
	maximum = 0
	# Your code here
	return maximum
```



### Problems

#### Strong numbers
> A strong number is a number for which the sum of all digits factorial is equal to the original number.
> For example: `1! + 4! + 5! == 145`

A function which returns True if the given number is strong and False if the given number is not strong.

