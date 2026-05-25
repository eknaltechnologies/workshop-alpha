# access
mylists = ("sita", "rama", "krishan")
print(mylists[1])
print(mylists)
# update
mylists[1] = "honey"
print(mylists)
# remove
mylists.remove("sita")
# join
colours1 = ("blue", "yellow", "black", "white")
colours2 = ("hi", "hello", "namasthe")
colours3 = colours1 + colours2
print(colours3)
# loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# method
mylists = (1, 2, 3, 2, 4, 2, 5, 6, 4, 3, 8)
x = mylists.count(2)
print(x)
# index
x = mylists.index(4)
print(x)
# length
mylists = [1, 2, 3, 4, 5]
print(len(mylists))
# count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
# index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
