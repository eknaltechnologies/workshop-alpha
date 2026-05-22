a = {1, 2, 3, 4}

b = {3, 4, 5, 6}

print("Original Set A:", a)
print("Original Set B:", b)

a.add(7)
print("add():", a)

a.update([8, 9])
print("update():", a)

a.remove(2)
print("remove():", a)

a.discard(10)
print("discard():", a)

x = a.pop()
print("pop():", x)
print("After pop:", a)

copy_set = a.copy()
print("copy():", copy_set)

print("union():", a.union(b))

print("intersection():", a.intersection(b))

print("difference():", a.difference(b))

print("symmetric_difference():", a.symmetric_difference(b))

print("issubset():", {3, 4}.issubset(b))

print("issuperset():", b.issuperset({3, 4}))

print("isdisjoint():", a.isdisjoint({100, 200}))

print("Length:", len(a))

print("Maximum:", max(b))

print("Minimum:", min(b))

print("Sum:", sum(b))

print("Check Element:", 3 in b)

a.clear()
print("clear():", a)
