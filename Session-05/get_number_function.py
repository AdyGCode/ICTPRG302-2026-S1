# Get a number function demo
#
# Filename: get_number_function.py
# Author:   YOUR_NAME

MIN_NUMBER = -100
MAX_NUMBER = 100

def get_integer(prompt, min_integer, max_integer):
    number = min_integer - 1
    prompt = prompt + " " + str(min_integer) 
    prompt = prompt + " and " +  str(max_integer)

    while number < min_integer or number > max_integer:
        print(prompt)
        number = input("Enter value: ")
        number = int(number)
        if number < min_integer or number > max_integer:
            print("ERROR: Sorry you entered and invalid number.")
    return number

number_1 = get_integer("Enter first number between", 0, 123)
number_2 = get_integer("Enter second number between", MIN_NUMBER, MAX_NUMBER)


print(number_1)
print(number_2)