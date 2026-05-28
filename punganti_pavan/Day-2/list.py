# list mutubale and maintain the sequence order
# we can change data at any time
# Creating a list
students = ["pavan", "rahul", "suhel", "kiran"]
print(students)

students = ["pavan", "rahul", "ssuhel", "kiran"]

# Read single item
print(students[0])
print(students[-1])

students = ["pavan", "rahul", "sneha", "kiran"]

# Update single item
students[1] = "rohit"
print(students)

# DELETE – Removing List Items
students = ["pavan", "rahul", "suhel", "kiran"]
students.remove("rahul")
print(students)
