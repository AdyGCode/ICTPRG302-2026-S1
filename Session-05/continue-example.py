# Show the numbers 1 to 10 
# on one line, omitting those
# divisible by 3.
#
# All three of these examples
# solve the same problem
#
# One with continue, the other
# two without using it.


# Version 1 - using continue

for count in range(0,10):
    if (count % 3 == 0):
        continue
    print(str(count)+" ", end="")

print()

# Version 2 - using not

for count in range(0,10):
    if not (count % 3 == 0):
        print(str(count)+" ", end="")
    
print()

# Version 3 - using not equals

for count in range(0,10):
    if (count % 3 != 0):
        print(str(count)+" ", end="")

print()