try:

    # -------- CONSTANTS --------

    SILVER_COIN = "silver coin"
    GOLD_COIN = "gold coin"
    MAGIC_RING = "magic ring"
    RUBY = "ruby"
    EMERALD = "emerald"

    # -------- TREASURE BAG CREATION --------

    treasure_bag = []

    starter_treasures = [
        GOLD_COIN,
        SILVER_COIN,
        RUBY,
        "pearl"
    ]

    treasure_bag.extend(starter_treasures)

    print("Initial Treasure Bag:")
    print(treasure_bag)

    # -------- RARE TREASURES --------

    rare_treasures = (
        "diamond",
        MAGIC_RING
    )

    treasure_bag.extend(rare_treasures)

    print("\nAfter Adding Rare Treasures:")
    print(treasure_bag)

    # -------- REPLACE TREASURE --------

    if SILVER_COIN in treasure_bag:
        treasure_bag.remove(SILVER_COIN)

    ruby_position = treasure_bag.index(RUBY)

    treasure_bag[ruby_position] = EMERALD

    print("\nAfter Island Swaps:")
    print(treasure_bag)

    # -------- COUNTING TREASURES --------

    total_gold = treasure_bag.count(GOLD_COIN)

    print(f"\nTotal Gold Coins: {total_gold}")

    # -------- SORTING TREASURES --------

    treasure_bag.sort()

    print("\nSorted Treasure Bag:")
    print(treasure_bag)

    # -------- REVERSE ORDER --------

    treasure_bag.reverse()

    print("\nReverse Order Treasure Bag:")
    print(treasure_bag)

    # -------- SEARCHING TREASURE --------

    if MAGIC_RING in treasure_bag:
        print("\nMagic ring found successfully!")

    else:
        print("\nMagic ring not found")

    # -------- EMERALD POSITION --------

    emerald_position = treasure_bag.index(EMERALD)

    print(f"Emerald Position: {emerald_position}")

    # -------- SHARING TREASURE --------

    middle = len(treasure_bag) // 2

    my_treasures = treasure_bag[:middle]

    friend_treasures = treasure_bag[middle:]

    print("\nMy Treasure Share:")
    print(my_treasures)

    print("\nFriend Treasure Share:")
    print(friend_treasures)

    # -------- TREASURE ISLANDS --------

    islands = (
        "Island_1",
        "Island_2",
        "Island_3",
        "Island_4"
    )

    print("\nSearching Islands:")

    for island in islands:
        print(f"Searching in {island}")

    # -------- EXTRA TREASURE OPERATIONS --------

    print("\nExtra Treasure Operations")

    treasure_bag.append("ancient map")

    print("Added ancient map")

    treasure_bag.insert(2, "pirate sword")

    print("Inserted pirate sword")

    print("\nUpdated Treasure Bag:")
    print(treasure_bag)

    # -------- LENGTH OF TREASURE BAG --------

    total_items = len(treasure_bag)

    print(f"\nTotal Items in Treasure Bag: {total_items}")

    # -------- CHECKING EXISTING TREASURE --------

    search_item = input("\nEnter treasure to search: ")

    if search_item in treasure_bag:
        print(f"{search_item} exists in treasure bag")

    else:
        print(f"{search_item} not found")

    # -------- USER ADDS TREASURE --------

    add_item = input("\nEnter a treasure to add: ")

    treasure_bag.append(add_item)

    print(f"{add_item} added successfully")

    print(treasure_bag)

    # -------- USER REMOVES TREASURE --------

    remove_item = input("\nEnter a treasure to remove: ")

    if remove_item in treasure_bag:

        treasure_bag.remove(remove_item)

        print(f"{remove_item} removed successfully")

    else:
        print(f"{remove_item} not found")

    # -------- COPY TREASURE BAG --------

    copied_bag = treasure_bag.copy()

    print("\nCopied Treasure Bag:")
    print(copied_bag)

    # -------- FINAL TREASURE BAG --------

    print("\nFinal Treasure Bag:")
    print(treasure_bag)

except KeyboardInterrupt:

    print("\nProgram stop by user")