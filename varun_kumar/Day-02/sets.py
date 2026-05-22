mylists={"apple","banana","cherry"}
print(mylists)
#add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#remove
thisset.remove("banana")
print(thisset)
#loop
numbersset={23,24,25,26,27,28}
for x in numbersset:
    print(x)
# join
num1=(11,12,13,14,15)
num2=(21,22,23,24,25)
num3=num1+num2
print(num3)
#frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#add
students={"krithi","hema","deepu","harini"}
students.add("minnu")
print(students)
#clear
students.clear()
print(students)
#copy
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
#update

x = {"apple", "banana", "cherry"}