# Session 03: Decisions 3
#
# Author: Adrian Gould
# Filename: decisions_nested.py
#

# ask the user about the weather
hot_or_cold = input("Is it hot today (y/n)?")
lecture = input("Do you have a TAFE lecture (y/n)?")

# provide a suggestion based on the weather
if hot_or_cold == "y":
    if lecture == "y":
        print("Sorry, you have to go to TAFE today.")
    else:
        print("Great! Let's go to the beach.")
else:
    print("Better go to TAFE today.")
    
# end of program
