# tuple operations
numbers = (12, 24, 36, 48, 60)
a = ((1, 2), (3, 4))
# index
print(numbers[0])
# length
print(len(numbers))
# nested tuples
print(a[1][0])
# count
print(numbers.count(24))
# slicing
print(numbers[1:4])
# concatenation
b = numbers + (72, 84)
print(b)
# membership
print(48 in numbers)
# maximum value
print(max(numbers))
# minimum value
print(min(numbers))
# sum
print(sum(numbers))
# sorted
print(sorted(numbers))
# tuple conversion
d = list(numbers)
print(d)
# list to tuple
e = tuple(d)
print(e)
# iterate tuple
for i in numbers:
    print(i)
# Item Exists
if 36 in numbers:
    print("number exists")
else:
    print("number not exists")
