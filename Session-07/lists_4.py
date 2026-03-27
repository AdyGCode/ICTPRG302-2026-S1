# List Demo 4
#
# Sorted shopping list
#
# Filename: lists_4.py
# Author:   YOUR_NAME


# Fruitless function, as it DISPLAYS values only
def print_shopping_list(list_of_items):
    print("Our shopping list 🧺")
    for item in list_of_items:
        print("-", item)


shopping_list = ["bread", "apples", "bananas", "salmon"]

print_shopping_list(shopping_list)
print()

shopping_list.sort()

print_shopping_list(shopping_list)
