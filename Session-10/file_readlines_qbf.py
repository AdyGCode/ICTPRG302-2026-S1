# File Opening & Reading 4
#
# Author: Adrian Gould
#
# Filename: file_read_qbf.py

file = open("quick_brown_fox.txt", "r")
poem_lines = file.readlines()
print(poem_lines)
