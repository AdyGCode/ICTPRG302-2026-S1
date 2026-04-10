# File Opening & Reading 2
#
# Author: Adrian Gould
#
# Filename: file_read_temperatures.py

file = open("temperatures.txt", "r")
temperatures = file.read()
print(temperatures)
