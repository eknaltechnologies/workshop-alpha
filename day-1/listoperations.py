fruits = ["apple", "banana", "mango"]

print("Original List:", fruits)

fruits.append("orange")
print("append():", fruits)

fruits.extend(["grape", "kiwi"])
print("extend():", fruits)

fruits.insert(1, "pineapple")
print("insert():", fruits)

fruits.remove("banana")
print("remove():", fruits)  

fruits.pop()
print("pop():", fruits)

print("index():", fruits.index("mango"))

print("count():", fruits.count("apple"))

fruits.sort()
print("sort():", fruits)

new_sorted = sorted(fruits)
print("sorted():", new_sorted)

fruits.reverse()
print("reverse():", fruits)

new_list = list(reversed(fruits))
print("reversed()", new_list)

copy_list = fruits.copy()
print("copy():", copy_list)

fruits.clear()
print("clear():", fruits)
