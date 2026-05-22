#example
fruits=("apple", "banana", "cherry")
print(fruits)
#tuple length
print(len(fruits))
#data type of tuple
print(type(fruits))
#tuple constructor
fruits1=tuple(("apple", "banana", "cherry"))
print(fruits1)
#indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])
#negative indexing
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
#range of indexing
print(fruits[0:2])
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
#range of negative indexing
print(fruits[-3:-1])
print(fruits[-2:])
#checking the presence of an element in the tuple
print("apple" in fruits)
#using for loop
for fruit in fruits:
    print(fruit)
#using while loop
i=0
while i < len(fruits):
    print(fruits[i])
    i+=1