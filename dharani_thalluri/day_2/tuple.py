# count
main_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
yy = main_tuple.count(5)
print(yy)
# index
numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
oo = numbers.index(8)
print(oo)
# access
fruits = ("apple", "banana", "cherry")
print(fruits[1])
# Update
xi = ("apple", "banana", "cherry")
yi = list(xi)
yi[1] = "kiwi"
xi = tuple(yi)
print(xi)
# loop
banks = ("Union", "SBI", "HDFC ")
for x in banks:
    print(x)
# join
letters1 = ("a", "b", "c")
letters2 = (1, 2, 3)
letters3 = letters1 + letters2
print(letters3)
