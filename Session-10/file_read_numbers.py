# File Opening & Reading 1
#
# Author: Adrian Gould
#
# Filename: file_read_numbers.py

numbers_file = open("numbers.txt","r")
numbers = numbers_file.read()
numbers_file.close()

print(numbers)
