# File Opening & Reading 7
#
# Author: Adrian Gould
#
# Filename: file_readline_for_loop.py

file = open("quick_brown_fox.txt", "r")

for poem_line in file:
    print(poem_line)
    
file.close()

