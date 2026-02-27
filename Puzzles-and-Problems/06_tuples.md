
# 🐍 Tuples

---

> [!Important]
> Keep PEP8 in mind and make your code easy to read with meaningful variable names.
> Remember: code that you haven't run or tested is not trustworthy!

> [!Reference]
> Tuples are similar to lists, but are written with `()` round brackets.
> ```python
> a_tuple = (1,2,3)
> ``` 


---
## Tuples

Name your working file `tuple_exercises.py` if you want to use the associated unit tests.

### 1.  Write a function called `push(tuple, element)` that takes a tuple and returns it with one extra element. 

> [!Hint]
> Tuples are immutable! Think of how would you do this with a string, which is similar.
> You can turn a list into a tuple using the `tuple()` function.

### 2. Write a function `is_equal(tuple1, tuple2)`, which compares the equality of two tuples
    
### 3. Write a function `greater(tuple1, tuple2)`, which returns the greater of two tuples

### 4. Try making the tuple `(1, 'a', True)`.  What do you notice?
#### Now compare it (> or < or \==) against:
A: `(1, 'b', False)`
B: `(1, 1, 1)`

### 5. Using the following list of tuples, sort them.  How does Python compare tuples? `[(2, 3), (1, 2), (3, 4), (3, 1)]`.

### 6. Try making the following dictionary: `{(1,2): "a"}`. Why does this work?

---
## Destructuring

> [!Note]
> Apart from being 'immutable lists', tuples allow us to do something else:
>
>  We are able to use tuples to 'destructure' values
>  ```python
>  (first_element, second_element) = ("Hello", "World")
>  ```
> In this case, `first_element` will be "Hello" and `second_element` will be "World"
>
>  This counts for function return values as well:
>  ```python
>  def function_which_returns_multiple_values():
> 	 count_a = 1
> 	 count_b = 2
> 	 return (count_a, count_b)
>	
>  (variable_a, variable_b) = function_which_returns_multiple_values()	
>  ```
>  In this example, `variable_a` will have a value of 1, and `variable_b` will have a value of 2.

### 7. Write a function that takes a string, and returns both a list of all words in the string, and the count of all words in the string.

For example:
```
>>> word_count("Hello world")
>>> (["Hello", "world"], 2)
```

Then assign the return value of `word_count` to two separate variables, "string_as_list" and "string_length"

---
