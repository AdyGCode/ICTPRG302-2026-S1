# B-COM-2

# …
print(3 + 4)
print("3" + "4")


# B-COM-4


#B-OUT-1

print("Welcome to Byte-Sized Shop!")


#B-OUT-4

total = 12.5
print('Total: $', total)
# Output: Total: $ 12.5

# ---or---

total = 12.5  # Python knows the number is decimal (floating point)
print('Total: $' + str(total))
# Output: Total: $12.5


class_subject = "Physics"

# 2 + 3 * 4 = 14
# (2 + 3) * 4 = 20

print(2 / 5)
print(2 // 5)
print(12 // 5)
print(12 % 5)


print(5 == "5")

age = 18
if age >= 18:
    print("Access granted")


state = 'yellow'

if state == 'green':
    print('Go')
elif state == 'yellow':
    print('Caution')
else:
    print('Stop')


if state == "red":
    print('Stop')
elif state == "yellow":
    print('Caution')
elif state == "green":
    print('Go')
else:
    print("OOPS!")