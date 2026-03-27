# Get a number function demo #2
#
# Filename: get_number_function_v2.py
# Author:   YOUR_NAME

MIN_NUMBER = -100
MAX_NUMBER = 100

def get_integer(prompt, min_integer, max_integer):
    prompt = prompt + " " + str(min_integer) 
    prompt = prompt + " and " + str(max_integer)
    while True:
        print(prompt)
        number = input("Enter value: ")
        number = int(number)
        if number >= min_integer and number <= max_integer:
            break
        print("ERROR: Sorry you entered and invalid number.")
    return number


number_1 = get_integer("Enter first number between", 0, 123)

number_2 = get_integer("Enter second number between", MIN_NUMBER, MAX_NUMBER)


print(number_1)
print(number_2)