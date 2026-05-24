color_set = {
    "blue",
    "green",
    "pink",
    "yellow",
    "red",
    "purple",
    "pink",
    "blue",
    "orange",
    "yellow",
}


print(color_set)
print(type(color_set))
print(len(color_set))

vechiles_set = {"BMW", "TATA", "MAHINDRA"}
vechiles_set.add("Suzuki")
print(vechiles_set)

vechiles_set.update(["BMW", "Toyota", "Benz"])
print(vechiles_set)

vechiles_set.remove("BMW")
vechiles_set.remove("MAHINDRA")
print(vechiles_set)

vechiles_set.discard("Toyota")
vechiles_set.discard("Audi")
print(vechiles_set)

print(vechiles_set.pop())

vechiles_set.clear()
print(vechiles_set)

fruits_set1 = {"apple", "banana", "grapes", "guava", "straw berry"}
fruits_set2 = {"grapes", "oranges", "pineapple", "guava"}
print(fruits_set1)
print(fruits_set2)

print("apple" in fruits_set1)
print("oranges" in fruits_set1)

print("grapes" not in fruits_set1)
print("pineapple" not in fruits_set1)

print(fruits_set1.union(fruits_set2))

print(fruits_set1.intersection(fruits_set2))

print(fruits_set2.difference(fruits_set1))
print(fruits_set1.difference(fruits_set2))

str1 = "abcdefgh"

alphabets = set(str1)
print(alphabets)
