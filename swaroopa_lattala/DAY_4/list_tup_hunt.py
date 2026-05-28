treasure_bag = []
print("======================\nTreasure Hunt challenge\n=====================")
# Build Treasure Bag
print("--- Task 1: Building the Treasure Bag ---")
treasure_bag = []
treasure_bag.append("gold coin")
treasure_bag.append("silver coin")
treasure_bag.append("ruby")
treasure_bag.append("pearl")
print(f"Treasure Bag:{treasure_bag}\n")

print("--- Task 2: Adding Rare Treasures ---")
rare_treasures = ("diamond", "magic ring")
treasure_bag.extend(rare_treasures)
print(f"Bag with rare treasures: {treasure_bag}\n")
print("--- Task 3: Island Swaps ---")
treasure_bag.remove("silver coin")
# replace-swap
ruby_index = treasure_bag.index("ruby")
treasure_bag[ruby_index] = "emerald"
print(f"Bag after swaps: {treasure_bag}\n")

print("--- Task 4: Sorting & Counting ---")
print("Bag has:", treasure_bag)
gold_count = treasure_bag.count("gold coin")
print(f"Number of gold coins:{gold_count}")
# Sort alphabetically
treasure_bag.sort()
print(f"Alphabetically sorted bag: {treasure_bag}")
# Reverse the order
treasure_bag.reverse()
print(f"Reversed bag: {treasure_bag}\n")

# Searching the Bag
print("--- Task 5: Searching the Bag ---")
# Check if "magic ring" exists
if "magic ring" in treasure_bag:
    print("Yes, 'magic ring' is safely in the bag!")
else:
    print("Oh my god, the magic ring is missing!")

# Find the position of "emerald"
emerald_position = treasure_bag.index("emerald")
print(f"'emerald' is at index position: {emerald_position}\n")

print("--- Task 6: Sharing Treasures ---")
# Find the midpoint of the bag
midpoint = len(treasure_bag) // 2

# Split using list slicing [start:stop]
my_share = treasure_bag[:midpoint]
friend_share = treasure_bag[midpoint:]

print(f"My share: {my_share}")
print(f"Friend's share: {friend_share}\n")

print("--- Task 7: Treasure Map Loop ---")
islands = ("island_1", "island_2", "island_3")

for island in islands:
    print(f"Searching {island} for treasures...")
print("\n")


print("--- Task 8: Interactive Game Mode ---")
# Resetting the bag to include standard + rare treasures for the user
current_bag = ["gold coin", "ruby", "pearl", "diamond", "magic ring"]
print(f"Your starting bag: {current_bag}")

# Ask user to add a treasure
new_treasure = input("Enter a treasure to ADD to your bag: ")
current_bag.append(new_treasure)
print(f"Bag after adding: {current_bag}\n")
