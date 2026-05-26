"""
A loop is used to execute a block of code repeatedly, either a fixed number of times or for each item in a collection.
loops are two types in python
1.for loop
2.while loop

"""

# using range in for loop
for i in range(5):
    print(i)

# while loop in sum of first 5 numbers
i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum:", total)
