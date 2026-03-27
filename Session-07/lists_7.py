# List Demo 7
#
# Making a shopping list with locations
#
# This stores the product and location using
# nested lists:
#   shopping_list = [ [product, location], ... ]
#
# Asks user for a product and then a location
# When the product and/or the location is QUIT
# the shopping list is then displayed.
#
# We ask for input to BOTH location & product
# so we have to enter QUIT twice.
#
# Filename: lists_7.py
# Author:   YOUR_NAME


def display_shopping_list(shopping_list):
    print()
    print()
    print("Our Shopping List 🧺")
    print("=" * 40)
    total_items = len(shopping_list)

    # When there are items in the shopping_list, display
    # our shopping list
    if total_items > 0:
        for index in range(total_items):
            details = shopping_list[index]
            product = details[0]
            location = details[1]
            print(str(index + 1) + "> Aisle:", location, "-", product)
    else:
        # otherwise tell us the list is empty
        print("Empty shopping list")

    print("-" * 40)


def get_text_from_user(prompt):
    # Ask user for text
    text = input(prompt)

    # while text is empty:
    #   display error message
    #   ask user for text
    while text.strip() == "":
        print("Text must be at least one non-whitespace character.")
        print()
        text = input("Enter the item to add: ")

    # return the text value
    return text


# set up the shopping and location list
my_shopping_list = []

# ask user for first product and location
product = get_text_from_user("Product to purchase: ")
location = get_text_from_user("Location of product: ")

# While the product and/or location are NOT QUIT:
#   create "item and location" list with product and location
#   add the "item and location" list to the shopping list
#   ask user for next product and location
while "QUIT" not in [product.upper(), location.upper()]:
    item_and_location = [product, location]
    my_shopping_list.append(item_and_location)

    print()
    product = get_text_from_user("Product to purchase: ")
    location = get_text_from_user("Location of product: ")

display_shopping_list(my_shopping_list)
