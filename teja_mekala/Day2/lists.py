# example
flowers = ["rose", "lily", "lotus", "jasmine"]
print(flowers)
# List length
print(len(flowers))
# data type of list
print(type(flowers))
# indexing
print(flowers[0])
print(flowers[1])
print(flowers[2])
print(flowers[3])
# negative indexing
print(flowers[-1])
print(flowers[-2])
print(flowers[-3])
print(flowers[-4])
# range of indexing
print(flowers[1:4])
print(flowers[0:3])
print(flowers[:4])
print(flowers[1:])
#range of negative indexing
print(flowers[-4:-1])
print(flowers[-4:-3])
#checking the presence of an element in the list
print("rose" in flowers)
#changing the value of an element in the list
flowers[1] = ["sunflower"]
#changing the value of an element in the list using negative indexing
flowers[-1] = ["hibiscus"]
#chaing the value of an element in the list using range of indexing
flowers[0:2] = ["marigold", "daisy"]
print(flowers)
#using insert() method
flowers.insert(2, "orchid")
#using append() method
flowers.append("tulip")
print(flowers)
#extend() method
flowers.extend(["lotus", "jasmine"])
print(flowers)
#using remove() method
flowers.remove("lotus")
print(flowers)
#using pop() method
flowers.pop(3)
print(flowers)
#using del keyword
del flowers[1]
print(flowers)
#using clear() method
flowers.clear()
print(flowers)
#using for loop
flowers = ["rose", "lily", "lotus", "jasmine"]
for flower in flowers:
    print(flower)
# using while loop
i = 0
while i < len(flowers):
    print(flowers[i])
    i= i + 1    
# using sort() method
flowers.sort()
print(flowers)
# using sort descending order
flowers.sort(reverse = True)
print(flowers)
# using case insensitive sort
flowers.sort(key=str.lower)
print(flowers)
# using reverse() method
flowers.reverse()
print(flowers)
#using copy() method
flowers = flowers.copy()
print(flowers)
#using list() method
flowers = list(flowers)
print(flowers)
#using slice operator
flowers = flowers[:]
print(flowers)
# using sorted() method
flowers = sorted(flowers)
print(flowers)