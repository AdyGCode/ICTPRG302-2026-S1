student = {"name": "Alex",
           "age": 21}

name = student["name"]
print(name)

# alternative way to get the name
name=student.get("name","Anonymous")
print(name)

# get a grade... missing so None value
grade = student.get("grade")
print(grade)

# Alex is studying Python
student["unit"] = "Python"
print(student)

# Alex has had a birthday
student["age"] = 22
print(student)

# Remove Alex's age
del student["age"]
print(student)

# get the dictionary's keys
keys = student.keys()
print(keys)

# get the dictionary's values
values = student.values()
print(values)

# get the dictionary items
items = student.items()
print(items)

# Clear (remove/empty) the student data
student.clear()
print(student)

