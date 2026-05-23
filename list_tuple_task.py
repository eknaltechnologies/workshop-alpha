# Python Treasure Hunt – List & Tuple Challenge

# 1. Build the Treasure Bag
treasure_bag = []

treasure_bag.append("gold coin")
treasure_bag.append("silver coin")
treasure_bag.append("ruby")
treasure_bag.append("pearl")

print("Treasure Bag:", treasure_bag)


# 2. Rare Treasures (Tuples)
rare_treasures = ("diamond", "magic ring")

# Add rare treasures into the bag
treasure_bag.extend(rare_treasures)

print("\nAfter adding rare treasures:")
print(treasure_bag)


# 3. Island Swaps
# Remove "silver coin"
treasure_bag.remove("silver coin")

# Replace "ruby" with "emerald"
ruby_index = treasure_bag.index("ruby")
treasure_bag[ruby_index] = "emerald"

print("\nAfter swaps:")
print(treasure_bag)


# 4. Sorting & Counting
gold_count = treasure_bag.count("gold coin")

print("\nNumber of gold coins:", gold_count)

# Sort alphabetically
treasure_bag.sort()

print("\nSorted Treasure Bag:")
print(treasure_bag)

# Reverse order
treasure_bag.reverse()

print("\nReversed Treasure Bag:")
print(treasure_bag)


# 5. Searching the Bag
# Check if "magic ring" exists
if "magic ring" in treasure_bag:
    print("\nMagic ring exists in the bag.")
else:
    print("\nMagic ring not found.")

# Find position of emerald
emerald_position = treasure_bag.index("emerald")

print("Position of emerald:", emerald_position)


# 6. Sharing Treasures
mid = len(treasure_bag) // 2

my_share = treasure_bag[:mid]
friend_share = treasure_bag[mid:]

print("\nMy Share:", my_share)
print("Friend Share:", friend_share)


# 7. Treasure Map (Tuple Loop)
islands = ("island_1", "island_2", "island_3")

print("\nSearching Islands:")
for island in islands:
    print(f"Searching {island} for treasures...")


# 8. Final Challenge – Interactive Game

print("\n--- Interactive Treasure Game ---")

# Start with treasures + rare treasures
game_bag = ["gold coin", "pearl", "emerald"]
game_bag.extend(rare_treasures)

print("Starting Bag:", game_bag)

# Ask user to add treasure
add_treasure = input("Enter a treasure to add: ")
game_bag.append(add_treasure)

print("Bag after adding treasure:")
print(game_bag)

# Ask user to remove treasure
remove_treasure = input("Enter a treasure to remove: ")

if remove_treasure in game_bag:
    game_bag.remove(remove_treasure)
    print("Treasure removed successfully.")
else:
    print("Treasure not found in bag.")

print("Final Treasure Bag:")
print(game_bag)