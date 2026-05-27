names_tuple = ("Ramu", "Hari", "Sara", "Krishna", "Sai", "Geetha")

print(names_tuple)
print(type(names_tuple))
print(len(names_tuple))

print(names_tuple[3])
print(names_tuple[-1])
print(names_tuple[-4])
print(names_tuple[1:5])

names = ("Andy", "Victor", "Arjun")
updated_names = names_tuple + names
print(updated_names)

print(names_tuple * 2)

marks_tuple = (20, 23, 18, 19, 20, 24, 25, 17, 16, 15, 20, 21)
print(marks_tuple.count(20))


print(marks_tuple.index(21))
print(marks_tuple.index(17))
print(marks_tuple.index(24))

print(25 in marks_tuple)
print(13 in marks_tuple)

print(25 not in marks_tuple)
print(13 not in marks_tuple)
