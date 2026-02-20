# 🐍 05: String Functions

---
## Instructions:

Write code to solve each of these problems.  Organise it all neatly; either in a single file called `string_functions.py`, or multiple files in a `string_functions` folder.  Eg, `string_functions/1.py`.

> [!Always!]
> Keep PEP8 in mind and make your code easy to read with meaningful variable names.
> 
> Remember: code that you haven't run or tested is not trustworthy!

---

## String Method Usage

### 1. Length of a String
Ask the user for a word and print its length using `len()`.

### 2. Capitalize a Sentence
Ask the user for a sentence and print it with the first character capitalized using `capitalize()`.

#### 2b: Usability question:
In what situations is this a bad idea? Consider the sentence "Old MacDonald had a farm".

### 3. Convert to Uppercase
Ask the user for a sentence and print it in all uppercase letters using `upper()`.

### 4. Convert to Lowercase
Ask the user for a sentence and print it in all lowercase letters using `lower()`.

### 5. Replace a Word
Write a script that starts with the phrase "JavaScript is simple to code with".
Then change out "JavaScript" with "Python" using `replace()`.

### 6. Find a Substring
Ask the user for a sentence and find the position of the word "code" using `find()`.
If you cannot find the word "code", print out the message "I guess you had other things to talk about"

> [!Hint]
> Remember that `find` returns `-1` if it didn't find the word

### 7. Strip Whitespace
Ask the user for a sentence with leading and trailing spaces and print it stripped using `strip()`.

### 8. Check if a Word is in a Sentence
Ask the user for a sentence and a word, then check if the word is in the sentence using `in`.

### 9. Combine Two Strings
Write a function which takes two strings and combines them with a space in-between.
> The point here is to write a function with a return value

### 10. Print Each Character in Uppercase
Ask the user for a word and print each character individually in uppercase using a loop.

### 11. Replace All Vowels with "*"
Ask the user for a sentence and replace all vowels with "*".
> Hint: You'll need 'an accumulator' -- an out-of-loop variable for storing the new string.

### 12. Find All Occurrences of a Letter
Ask the user for a sentence and a letter, then print all positions where the letter appears, by using a loop.

---
## Extensions
These problems are a little harder, and require you to think a bit about *how* you are going to figure something out.

### 13. Count Words in a Sentence
Ask the user for a sentence and count how many words it contains using `split()` and `len()`.

### 14. Strip and Capitalize Each Word
Ask the user for a sentence and strip and capitalize each word using a loop.
Use the `split()` method.
> [!example run]
> Here's what this might look like when you've run it
> ```
>Please enter a sentence> This sentence    is false.
>This
>Sentence
>Is
>False
>```

### 15. Reverse a Sentence
Ask the user for a sentence and print it in reverse using slicing. `[:]`
> [!Hint]
> Much like `range`, the slicing operator can take a third parameter for a "step", like this:
> ```python
> print("abcde")[::2]
>> ace
> ```

### 16. Check Palindrome
Write a function `is_palindrome(word)` that returns `True` if the word is a palindrome (and `False` if it is not).

> [!Reference]
> A "palindrome" is a word which has the same spelling backwards and forwards.  For example, the words `racecar` and `civic`, which, when reversed, still spell `racecar` and `civic`.

### 16A. Challenge: Now try it without using reverse
If you did the first part by comparing the word with the reversed word, now try doing it by comparing the word letter by letter.

### 17. Remove All Digits from a String
Ask the user for a string and remove all digits using a loop and `isdigit()`.  Once again, you'll need an accumulator to build the new string.
