# Session 03: Decisions 2
#
# Author: Adrian Gould
# Filename: decisions_multi_way.py
#

# ask the user about the weather
print("What's the weather like?")
print("Choices: rainy, sunny, hail, snow")
weather = input("Enter your choice:")

# provide a suggestion based on the weather
if weather == "sunny":
    print("It's sunny today...")
    print("Don't forget your hat.")
elif weather == "rainy":
    print("It's rainy today...")
    print("Don't forget your umbrella.")
else:
    print("Sorry, I dont know what you mean.")
    
# end of program
