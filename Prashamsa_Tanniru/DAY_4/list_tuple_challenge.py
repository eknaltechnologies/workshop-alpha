# Build Treasure bag list
try:
    treasure_bag = []
    treasure_bag.extend(["gold coin", "silver coin", "ruby", "pearl"])
    print(treasure_bag)

    # build rare treasures tuple
    rare_treasures = ("diamond", "magic ring")
    treasure_bag.extend(rare_treasures)
    print(treasure_bag)

    # island swaps (list operations)
    treasure_bag.remove("silver coin")
    index_ruby = treasure_bag.index("ruby")
    treasure_bag[index_ruby] = "emerald"
    print(treasure_bag)

    # sorting and counting (list operations)
    gold_coins_count = treasure_bag.count("gold coin")
    print(f"Number of gold coins: {gold_coins_count}")
    treasure_bag.sort()
    treasure_bag.reverse()
    print(treasure_bag)

    # searching for treasures
    if "magic ring" in treasure_bag:
        print("You found the magic ring!")
    index_emerald = treasure_bag.index("emerald")
    print(f"Position of emerald: {index_emerald}")

    # sharing treasures (divide list by len/2 and use slicing)
    mid = len(treasure_bag) // 2
    my_share = treasure_bag[:mid]
    friend_share = treasure_bag[mid:]
    print(f"My treasures: {my_share}")
    print(f"Friend's treasures: {friend_share}")

    # Treasure map
    islands = ("island_1", "island_2", "island_3")
    for island in islands:
        print(f"Searching {island}")

    # final challenge
    add_item = input("Enter a treasure to add: ")
    treasure_bag.append(add_item)
    print(f"Added {add_item} to the treasure bag.")

    remove_item = input("Enter a treasure to remove: ")
    if remove_item in treasure_bag:
        treasure_bag.remove(remove_item)
        print(f"Removed {remove_item} from the treasure bag.")
    else:
        print(f"{remove_item} not found in the treasure bag.")
    print(treasure_bag)

except KeyboardInterrupt:
    print("\nGame interrupted by user.")
