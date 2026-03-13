# Get text from the user
#
# Asks the user to enter text between a minimum and 
# maximum length
#
# Filename: get_text.py
# Author:   YOUR_NAME


def get_text(prompt, min_length, max_length):
    """
    Function to get text of a defined length

    Written by Adrian Gould.
    """
    
    text = None
    
    prompt = prompt + " " 

    error_message = "The text must be between " + str(min_length)
    error_message = error_message + " and " +  str(max_length) + " characters."

    while text == None :
        text = input(prompt)
        text = text.strip()
        if (len(text) < min_length or len(text) > max_length):
            print("ERROR: Sorry you entered an invalid string of text.")
            print(error_message)
            text = None

    return text

def display_results(given, family):
    print("Full name: " + given + " " + family)


given_name = get_text("Please enter your given name:", 1, 10)
family_name = get_text("Please enter your family name:", 1, 10)

display_results(given_name, family_name)