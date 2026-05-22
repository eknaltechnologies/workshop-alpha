# tuple is immutable 
# once data is inserted we cant change the data 
# # CREATE a tuple
students = ("pavan", "rahul", "sneha")
print("Created :", students)

# READ a tuple
print("Read    :", students[1])

# UPDATE a tuple
temp = list(students)
temp[1] = "rohit"
students = tuple(temp)
print("Updated :", students)

# DELETE a tuple
temp = list(students)
temp.remove("sneha")
students = tuple(temp)
print("Deleted :", students)