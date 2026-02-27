# Indefinite Loop - with BREAK

while True:
    number = input("Enter number (0 to 9):")
    number = int(number)
    if number >=0 and number <=9:
        break
    else:
        print("error! Please make sure number is in the range 0 to 9.")


        