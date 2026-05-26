# list operations

numbers = [12, 24, 36]
a = [[1, 2], [3, 4]]

# index-based
print(numbers[0])

# length
print(len(numbers))

# append
numbers.append(48)
print(numbers)

# delete
del numbers[3]
print(numbers)

# pop
numbers.pop()
print(numbers)

# nested lists
print(a[1][0])

# insert
numbers.insert(2, 72)
print(numbers)

# update
numbers[1] = 26
print(numbers)

# remove
numbers.remove(26)
print(numbers)

# extend
numbers.extend([50, 60, 70])
print(numbers)

# sort
numbers.sort()
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# count
print(numbers.count(50))

# index
print(numbers.index(60))

# copy
b = numbers.copy()
print(b)

# clear
temp = [1, 2, 3]
temp.clear()
print(temp)

# concatenation
c = numbers + [100, 200]
print(c)
