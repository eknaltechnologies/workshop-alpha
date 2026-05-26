# add()
sets_f = {"apple", "banana", "cherry"}
sets_f.add("orange")
print(sets_f)
# clear()
conditions = {"if", "elif", "else"}
conditions.clear()
print(conditions)
# copy()
companies = {"IBM", "eknal", "Infosys"}
x = companies.copy()
print(x)
# difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
# discard()
apps = {"apple store", "blinkit", "contacts"}
apps.discard("blinkit")
print(apps)
# intersection()
end = {"apple", "banana", "cherry"}
to = {"google", "microsoft", "apple"}
endto = end.intersection(to)
print(endto)
# isdisjoint()
xo = {"ani", "bunny", "chinnu"}
yo = {"games", "dance", "singing"}
zo = xo.isdisjoint(yo)
print(zo)
# issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
# issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# pop()
mobiles = {"realme", "redmi", "apple", "samsung", "oneplus", "vivo"}
mobiles.pop()
print(mobiles)
# remove()
games = {"freefire", "arrows", "chess"}
games.remove("arrows")
print(games)
# union()
a = {"potato", "tomato", "onion", "carrot", "beetroot", "cabbage"}
b = {"apple", "banana", "cherry", "grapes", "orange"}
c = a.union(b)
print(c)
# update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
