

my_list = ["a","b","c"]

# Add item to the END of the list
my_list.append("d")
print(my_list)

# Add item at the FRONT of the list
my_list.insert(0,'e')
print(my_list)

# Add item at position 3 of the list
my_list.insert(2,'f')
print(my_list)


# Another way to add to the END
# which is easier to understand?
my_list.insert(len(my_list),'g')
print(my_list)
