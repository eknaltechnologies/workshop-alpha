#set operations
myset = {"apple", "banana", "cherry"}
#Length of a Set
print(len(myset))
#add items
myset.add("orange")
print(myset)
#Remove Item
myset.remove("banana")
print(myset)
#union
set2 = {"google", "microsoft", "apple"}
set3 = myset.union(set2)
print(set3)
#intersection
set4 = myset.intersection(set2)
print(set4)
#difference
set5=myset.difference(set2)
print(set5)
#symmantic difference
set6 = myset.symmetric_difference(set2)
print(set6)
#creating frozenset (frozen set is immutable)
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#copy
set=myset.copy()
print(set)
#discard
myset.discard("banana")
print(myset)
#is superset
set7= myset.issuperset(set2)
print(set7)
#is subset
set8=myset.issubset(set2)
print(set8)
#is disjoint
set9=myset.isdisjoint(set2)
print(set9)