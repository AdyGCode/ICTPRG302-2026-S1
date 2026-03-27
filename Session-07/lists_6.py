# List Demo 6
#
# Making a shopping list with locations
#
# Asks user for a product and then a location
# When the product and/or the location is QUIT
# the shopping list is then displayed.
#
# We ask for input to BOTH location & product
# so we have to enter QUIT twice.
#
# Filename: lists_6.py
# Author:   YOUR_NAME


def display_shopping_list(items_list, locations_list):
    print()
    print()
    print("Our Shopping List 🧺")
    print("=" * 40)
    total_items = len(items_list)

    # When there are items in the items_list, display
    # our shopping list
    if total_items > 0:
        for index in range(total_items):
            product = items_list[index]
            location = locations_list[index]
            print("Aisle:", location, "-", product)
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
shopping_list = []
location_list = []

# ask user for first product and location
product = get_text_from_user("Product to purchase: ")
location = get_text_from_user("Location of product: ")

# While the product and location are NOT QUIT:
#   add the product to the shopping list
#   add the location to the location list
#   ask user for next product and location
while "QUIT" not in [product.upper(), location.upper()]:
    shopping_list.append(product)
    location_list.append(location)
    
    print()
    product = get_text_from_user("Product to purchase:  ")
    location = get_text_from_user("Location of product: ")

display_shopping_list(shopping_list, location_list)