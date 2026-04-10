# File Opening & Reading 6
#
# Author: Adrian Gould
#
# Filename: file_readlines_into_list_qbf

file = open("quick_brown_fox.txt", "r")
poem = []

for poem_line in file:
    poem.append(poem_line.strip())

file.close()

print(poem)
