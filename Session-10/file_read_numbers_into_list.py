# File Opening & Reading 8
#
# Author: Adrian Gould
#
# Filename: file_read_numbers_into_list.py

numbers_file = open("numbers.txt","r")
numbers =[]

for number in numbers_file:
    numbers.append( int( number.strip() ) )

numbers_file.close()

print(numbers)
