# Getting User Input
#
# Filename: input-01.py
#
# Author: Adrian Gould <adrian.gould@nmtafe.wa.edu.au>


number = input("How old are you?")
number = int(number) # change value of number to an integer
name = input("What is your name?")

print("Hello, ", name)
print("You have made ", number," journeys around the sun")

age_next_year = number + 1
print("Next year it will be ", age_next_year," journeys around the sun")

