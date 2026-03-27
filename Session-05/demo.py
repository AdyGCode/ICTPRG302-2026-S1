# Demo File for VS Code
#
# Author: Adrian Gould
# Filename: Session-05/demo.py

# Variables
given_name = "Jacques"
family_name = "d'Carre"
dummy_name = 'd\'Walt'
saying = "the doctor said: \"Knock-Knock.\""
number_of_stars = 30

for count in range(number_of_stars):
    print('*', end='')

print()

if given_name == 'Jacques':
    print("hello")
else:
    print("I do not know you")
    print("do I kow you?")

full_name = given_name + " " + family_name
print(full_name)

greeting  = input("Greeting: ")
