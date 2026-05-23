# Build Treasure bag list
try:
    treasure_bag = []
    treasure_bag.extend(["gold coin", "silver coin", "ruby", "pearl"])
    print("Initial treasure bag:", treasure_bag)

    # build rare treasures tuple
    rare_treasures = ("diamond", "magic ring")
    treasure_bag.extend(rare_treasures)
    print("After adding rare treasures:", treasure_bag)

    # island swaps (list operations)
    treasure_bag.remove("silver coin")
    index_ruby = treasure_bag.index("ruby")
    treasure_bag[index_ruby] = "emerald"
    print("Treasure bag after island swaps:", treasure_bag)

    # sorting and counting (list operations)
    gold_coins_count = treasure_bag.count("gold coin")
    print(f"Total gold coins collected: {gold_coins_count}")

    treasure_bag.sort()
    treasure_bag.reverse()
    print("Sorted treasure bag (highest to lowest):", treasure_bag)

    # searching for treasures
    if "magic ring" in treasure_bag:
        print("Congratulations! You discovered the Magic Ring!")

    index_emerald = treasure_bag.index("emerald")
    print(f"Emerald is located at position: {index_emerald}")

    # sharing treasures
    mid = len(treasure_bag) // 2
    my_share = treasure_bag[:mid]
    friend_share = treasure_bag[mid:]

    print("My treasure share:", my_share)
    print("Friend's treasure share:", friend_share)

    # Treasure map
    islands = ("island_1", "island_2", "island_3")

    for island in islands:
        print(f"Searching treasures on {island}...")

    # final challenge
    add_item = input("Enter a treasure to add: ")
    treasure_bag.append(add_item)
    print(f"{add_item} has been added to the treasure bag.")

    remove_item = input("Enter a treasure to remove: ")

    if remove_item in treasure_bag:
        treasure_bag.remove(remove_item)
        print(f"{remove_item} has been removed from the treasure bag.")
    else:
        print(f"{remove_item} was not found in the treasure bag.")

    print("Final treasure bag:", treasure_bag)

except KeyboardInterrupt:
    print("Treasure hunt ended by player.")