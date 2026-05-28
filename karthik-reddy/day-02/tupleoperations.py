colors = ("red", "blue", "green")

print("Original Tuple:", colors)

print("Indexing:", colors[1])

print("Negative Indexing:", colors[-1])

print("Slicing:", colors[0:2])

new_tuple = colors + ("yellow",)
print("Concatenation:", new_tuple)

print("Repetition:", ("Hi",) * 3)

print("Count:", colors.count("red"))

print("Index:", colors.index("green"))

print("Length:", len(colors))

print("Check Element:", "blue" in colors)

numbers = (4, 2, 9, 1)

print("Maximum:", max(numbers))

print("Minimum:", min(numbers))

print("Sum:", sum(numbers))

print("Sorted:", sorted(numbers))

print("Reversed:", tuple(reversed(numbers)))

packed = 1, 2, 3
print("Tuple Packing:", packed)

a, b, c = packed
print("Tuple Unpacking:", a, b, c)
