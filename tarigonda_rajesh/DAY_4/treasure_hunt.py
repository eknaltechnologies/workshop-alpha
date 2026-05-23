#1 Treasure Bag
treasure_bag=[]

treasure_bag.extend(["gold coin","silver coin","ruby","pearl"])
print(f"Treasure Bag: {treasure_bag}")

# 2 Rare Treasures(Tuple)
rare_treasures = ("diamond", "magic ring")
treasure_bag.extend(rare_treasures)

# 3 Island Swaps
print("Before removing and replacing ",treasure_bag)
treasure_bag.remove("silver coin")

treasure_bag[1]="emerald"
print("After remove and replace: ",treasure_bag)

# 4 Sorting & Counting
gold_coins_count=treasure_bag.count("gold coin")
print("Gold coins: ",gold_coins_count)

treasure_bag.sort()
print("Sort: ",treasure_bag)
treasure_bag.reverse()
print("Reverse of Tresure bag: ",treasure_bag)

# 5 searching 
if "magic ring" in treasure_bag:
    print("Magic ring exists in bag")
else:
    print("Magic ring not found")
print("Position of emerald",treasure_bag.index("emerald"))

# 6 Sharing treeasures
mid=len(treasure_bag)//2

my_share=treasure_bag[:mid]
friend_share=treasure_bag[mid:]

print(f"My share: {my_share}\nFriend Share: {friend_share}")

# 7 treasure map
islands=("island_1", "island_2", "island_3")
for island in islands:
    print(f"Searching {island} for treasures...")


print(f"Treasures Bag: {treasure_bag}")

new_treasure=input("Enter a treasure to add: ")
treasure_bag.append(new_treasure)
print("Treasure bag: ",treasure_bag)
treasure=input("Enter the treasure to remove: ")
if treasure in treasure_bag:
    treasure_bag.remove(treasure)
    print(treasure,"Removed sucessfully")
else:
    print("Tresure not found")

print("Treasure: ",treasure_bag)