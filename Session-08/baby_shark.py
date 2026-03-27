# Baby Shark Lyrics
#
# Author: Adrian Gould
#
# Filename: baby_shark.py

# Define Global Constants and Variables (if required)
# shark_name_list = []
# shark_names = ""

# Define a print_shark function
def print_shark(name):
    name = name.strip()
    for count in range(0,3):
        print(name + ", doo-doo" * 3)
    print(name + "\n")


# Get names of sharks (as a string)
# e.g. Barney, Wilma, Fred, Betty, Bam-Bam, Dino
shark_names = input("Enter the shark names: ")

# Make a list of the shark names from the string of shark names
shark_name_list = shark_names.split(',')

# Loop through list of names, printing shark's verse
# \n is the NEWLINE character and will print a blank line
print("\n\nBaby Shark Lyrics\n")
for name in shark_name_list:
    print_shark(name)
