# String slicing
#
# Demonstrate sliging strings using indexes
# and how to loop thorugh each character in a string
#
# Filename: string_slicing.py
# Author:   YOUR_NAME


fruit = "cumquat"

print( fruit[1] )

print( fruit[-1] )

print( fruit[3] )

letter_in_word = fruit[2]
print(letter_in_word)

print("hello"[2])

# This will not work
# fruit[0] = "K"

print()

index = 0
while index < len(fruit):
    letter_in_word = fruit[index]
    print(index, letter_in_word)
    index = index + 1

print()
word_length = len(fruit)
for index in range(word_length):
    letter_in_word = fruit[index]
    print(index, letter_in_word)

print()
for index in range(len(fruit)):
    letter_in_word = fruit[index]
    print(index, letter_in_word)
