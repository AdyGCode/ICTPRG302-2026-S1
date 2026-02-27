# Indefinite Loop - without BREAK v2

number = input("Enter number (0 to 9):")
number = int(number)

while number < 0 or number > 9:
    print("error! Please make sure number is in the range 0 to 9.")

    number = input("Enter number (0 to 9):")
    number = int(number)


        