print("==================\nTreasure Hunt challenge\n==================")
#Build Treasure Bag
treasure_bag=[]
treasure_bag.append("gold coin")
treasure_bag.append("silver coin")
treasure_bag.append("ruby")
treasure_bag.append("pearl")
print(f"Treasure Bag:{treasure_bag}\n")
#Rare treasure
rare_treasures=("diamond","magic ring")
treasure_bag.extend(rare_treasures)
print(f"Bag with rare treasures: {treasure_bag}\n")
#Island swaps
treasure_bag.remove("silver coin")
#replace-swap
ruby_index=treasure_bag.index("ruby")
treasure_bag[ruby_index]="emerald"
print(f"Bag after swaps: {treasure_bag}\n")
#sorting and counting
gold_count=treasure_bag.count("gold coin")
print(f"Number of gold coins:{gold_count}")
treasure_bag.sort()
print(f"sorted the bag alphabetically:{treasure_bag}")
#Reverse-opposite order
treasure_bag.reverse()
print(f"Reversed the bag:{treasure_bag}")
#search the bag
if "magic ring" in treasure_bag:
     print("yes ! 'magic ring' safe in the bag")
else:
     print("oh my god! 'magic ring'is missing")     
pos_index=treasure_bag.index("emerald")  
print(f"Position of emerald:{pos_index}")
#sharing treasures
my_share = []
friend_share = []
for index, item in enumerate(treasure_bag):
    if index % 2 == 0:
        my_share.append(item)
    else:
        friend_share.append(item)

print("My Share:", my_share)
print("Friend's Share:", friend_share)
#Treasure map
islands=("island_1","island_2","island_3")
for island in islands:
    print(f"Searching {islands}for treasures...")
    print("\n")

print("--- Interactive Game Mode ---")
current_bag=["gold coin", "ruby", "pearl", "diamond", "magic ring"]
print(f"Your starting bag:{current_bag}")
#Add a treasure
new_treasure=input("Enter a treasure to ADD in your bag :")
current_bag.append(new_treasure)
print(f"Bag after adding new treasure:{current_bag}\n ")
#remove a treasure
current_bag.remove("ruby")
print(f"Bag after removing:{current_bag}")

print("\n--- Hunt Complete! You are a master of Python Lists and Tuples! ---")