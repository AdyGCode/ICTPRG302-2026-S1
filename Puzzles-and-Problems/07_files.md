# 🐍 File Handling
  ---

> [!Important]
> Keep PEP8 in mind and make your code easy to read with meaningful variable names.
> Remember: code that you haven't run or tested is not trustworthy!

> [!Reference]
> 
> Traditional file handling:
> ```python
> file_handler = open("some_text_file.txt", "r", encoding="utf-8")
> for line in file_handler:
> 	print(line)
> file_handler.close() # Never forget to close!
> ``` 
>
> Modern (good) file handling, with "contexts":
> ```python
> with open("some_text_file.txt", "r", encoding="utf-8") as file_handler:
> 	for line in file_handler:
> 		print(line)
> ```
> 
> Modes:
> 
> | Letter | Meaning |
> | ------ | ---------- |
> | r | Read file |
> | w | Write to file (truncates) |
> | a | Append to file (adds on the end) |

---

Name your file `files_exercises.py` in order to use the associated unit tests.

The following use the provided file `example.txt` for reading.
### 1. Reading
Try reading the contents of `example.txt`.  Print each line, *without* trailing newlines.

### 2. Writing
Write "Hello, world!" to a file called `my_file.txt`.  Visually inspect the contents.

### 3. Truncation?
Now write "Good evening" in the same `my_file.txt`.  What do you notice has happened to the file?

### 4. Appending
Write a program that asks for a user input, and appends it to `my_file.txt`.

### 5. But now, with loops
Make a loop of the above, so that the user can keep inputting text until they type "quit".

### 6.  Reading, pt 2
Make a function that returns a list of all words in a file

---

## Putting things together

These are general exercises to try and put things together from previous weeks.
These may rapidly become quite advanced, do not be too intimidated if you find them challenging to approach.
### Word counter

> If you did problem 20 during 'lists and dictionaries', then this should be a not-too-intimidating extension, using file handling and tuples. (If you didn't, don't worry, I'll break it into steps.)
>
> I have provided the entire text of the public domain novel "Carmilla" as test text for this question.  See `carmilla_le_fanu.txt`.

The problem: I have a large book, and I want to know what the most common 100 words in the book are.  

#### Step 1: Write a function called `word_count(string)`
First, I should be able to take any string, split it into words, and count occurrences of those words.  I am not too worried about miscounts.  It's okay if `rose` and `rose.` are counted as different words, so I could probably just split on spaces for this step.

#### Step 2: 
Figure out how to merge dictionaries together, so that you can count multiple strings...

> [!Hint]
> You could try iterating through a new dictionary, getting and adding values into the original.
> ```python
> original_dictionary = { 'word': 2 }
> new_dictionary = { 'word': 5, 'new': 1 }
> for key,value in new_dictionary.items():
> 	original_dictionary[key] = original_dictionary.get(key, 0) + value
> ```

#### Step 3:
Read, line by line, the lines of the novel, and build out a dictionary of word counts.

#### Step 4:
Create a list of tuples of `(word_count, word)`, so that you can sort from most used to least-used word in the novel.  Print this out.

--- 
### Budget tracker

Make an application for keeping track of your fortnightly budget.
The user can enter lines starting with `+` to enter their income, and `-` to enter their expenses.

The application keeps running until the user quits.
The application will save everything to a "CSV": a comma-separated values file, called `budget.csv`.

```example
Add a line item (+/-,Name) or quit: 
+500,Wages
[Your net income is $500 per week]

Add a line item (+/-,Name) or quit: 
-100,Food
[Your net income is $400 per week]

Add a line item (+/-,Name) or quit: 
-350,Board
[Your net income is $50 per week]

Add a line item (+/-,Name) or quit: 
-100,Games
[You're over-budget by $50]

Add a line item (+/-,Name) or quit: 
quit
```

This will write a file that looks like this. (Note that the over-budget item was not written):
```csv
Item,Credit,Debit
Wages,500,0
Food,0,100
Board,0,350
```

