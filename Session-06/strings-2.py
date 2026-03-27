# Get text from the user v2
#
# Asks the user to enter text between a minimum and 
# maximum length.
# 
# This version uses the break keyword
#
# Filename: get_text_2.py
# Author:   YOUR_NAME


def get_text(prompt, min_length, max_length):
    text = None
    
    prompt = prompt + " " 

    error_message = "The text must be between " + str(min_length)
    error_message = error_message + " and " +  str(max_length) + " characters."

    while True :
        text = input(prompt)
        if (len(text) >= min_length and len(text) <= max_length):
            break

        print("ERROR: Sorry you entered an invalid string of text.")
        print(error_message)

    return text


# name = get_text("Please enter your name:", 1, 10)

given_name = get_text("Please enter your given name:", 1, 10)
family_name = get_text("Please enter your family name:", 1, 10)
