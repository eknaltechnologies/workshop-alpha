try:

    # Treasure Bag Creation

    treasure_bag = []

    starter_treasures = [
        "gold coin",
        "silver coin",
        "ruby",
        "pearl"
    ]

    treasure_bag.extend(starter_treasures)

    print("Initial Treasure Bag:")
    print(treasure_bag)


    # Rare Treasures

    rare_treasures = (
        "diamond",
        "magic ring"
    )

    treasure_bag.extend(rare_treasures)

    print("\nAfter Adding Rare Treasures:")
    print(treasure_bag)


    # Replace Treasure

    if "silver coin" in treasure_bag:

        treasure_bag.remove("silver coin")

    ruby_position = treasure_bag.index("ruby")

    treasure_bag[ruby_position] = "emerald"

    print("\nAfter Island Swaps:")
    print(treasure_bag)


    # Counting Treasures

    total_gold = treasure_bag.count("gold coin")

    print(f"\nTotal Gold Coins: {total_gold}")


    # Sorting Treasures

    treasure_bag.sort()

    print("\nSorted Treasure Bag:")
    print(treasure_bag)


    # Reverse Order

    treasure_bag.reverse()

    print("\nReverse Order Treasure Bag:")
    print(treasure_bag)


    # Searching Treasure

    if "magic ring" in treasure_bag:

        print("\nMagic ring found successfully!")

    else:
        print("\nMagic ring not found")


    # Emerald Position

    emerald_position = treasure_bag.index("emerald")

    print(f"Emerald Position: {emerald_position}")


    # Sharing Treasure

    middle = len(treasure_bag) // 2

    my_treasures = treasure_bag[:middle]

    friend_treasures = treasure_bag[middle:]

    print("\nMy Treasure Share:")
    print(my_treasures)

    print("\nFriend Treasure Share:")
    print(friend_treasures)


    # Treasure Islands

    islands = (
        "Island_1",
        "Island_2",
        "Island_3",
        "Island_4"
    )

    print("\nSearching Islands:")

    for island in islands:

        print(f"Searching in {island}")


    # Extra Treasure Operations

    print("\nExtra Treasure Operations")

    treasure_bag.append("ancient map")

    print("Added ancient map")

    treasure_bag.insert(2, "pirate sword")

    print("Inserted pirate sword")

    print("\nUpdated Treasure Bag:")
    print(treasure_bag)


    # Length of Treasure Bag

    total_items = len(treasure_bag)

    print(f"\nTotal Items in Treasure Bag: {total_items}")


    # Checking Existing Treasure

    search_item = input("\nEnter treasure to search: ")

    if search_item in treasure_bag:

        print(f"{search_item} exists in treasure bag")

    else:

        print(f"{search_item} not found")


    # User Adds Treasure

    add_item = input("\nEnter a treasure to add: ")

    treasure_bag.append(add_item)

    print(f"{add_item} added successfully")

    print(treasure_bag)


    # User Removes Treasure

    remove_item = input("\nEnter a treasure to remove: ")

    if remove_item in treasure_bag:

        treasure_bag.remove(remove_item)

        print(f"{remove_item} removed successfully")

    else:

        print(f"{remove_item} not found")


    # Copy Treasure Bag

    copied_bag = treasure_bag.copy()

    print("\nCopied Treasure Bag:")
    print(copied_bag)


    # Final Treasure Bag

    print("\nFinal Treasure Bag:")
    print(treasure_bag)


except KeyboardInterrupt:

    print("\nProgram stopped by user")