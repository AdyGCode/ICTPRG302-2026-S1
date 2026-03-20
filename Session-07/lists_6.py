# List Demo 6
#
# Making a shopping list with locations
#
# Asks user for
#
# Filename: lists_6.py
# Author:   YOUR_NAME


def display_list_of_items(list_of_items):
    print("The list contains...")
    for item in list_of_items:
        print("-", item)


def get_item_from_user():
    # Ask user for item
    item = input("Enter the item to add: ")
    # while item is empty:
    while item.strip() == "":
        # print error message
        print("Entered items cannot be empty.")
        # ask user for item
        item = input("Enter the item to add: ")
    # return the item value
    return item


my_item_list = []

# Ask user for an item
item = get_item_from_user()

# While the item is NOT QUIT do:
while item.upper() != "QUIT":
    # Add item to the list
    my_item_list.append(item)
    # Ask user for an item
    item = get_item_from_user()

# Display the items in the list
display_list_of_items(my_item_list)
