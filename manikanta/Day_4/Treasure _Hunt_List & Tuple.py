# Python Treasure Hunt – List & Tuple


# 1. Build the Treasure Bag
def build_treasure_bag():

    treasure_bag = []

    treasure_bag.append("gold coin")
    treasure_bag.append("silver coin")
    treasure_bag.append("ruby")
    treasure_bag.append("pearl")

    print("\nTreasure Bag:")
    print(treasure_bag)

    return treasure_bag


# 2. Rare Treasures (Tuple)


def add_rare_treasures(treasure_bag):

    rare_treasures = ("diamond", "magic ring")

    treasure_bag.extend(rare_treasures)

    print("\nAfter Adding Rare Treasures:")
    print(treasure_bag)

    return treasure_bag


# 3. Island Swaps


def island_swaps(treasure_bag):

    # Remove silver coin
    treasure_bag.remove("silver coin")

    # Replace ruby with emerald

    index = treasure_bag.index("ruby")
    treasure_bag[index] = "emerald"

    print("\nAfter Island Swaps:")
    print(treasure_bag)

    return treasure_bag


# 4. Sorting & Counting


def sorting_and_counting(treasure_bag):

    count_gold = treasure_bag.count("gold coin")

    print("\nNumber of Gold Coins:", count_gold)

    treasure_bag.sort()

    print("\nSorted Treasure Bag:")
    print(treasure_bag)

    treasure_bag.reverse()

    print("\nReversed Treasure Bag:")
    print(treasure_bag)


# 5. Searching the Bag


def searching_bag(treasure_bag):

    if "magic ring" in treasure_bag:
        print("\nMagic Ring Exists In The Bag")

    else:
        print("\nMagic Ring Not Found")

    position = treasure_bag.index("emerald")

    print("Position of Emerald:", position)


# 6. Sharing Treasures


def sharing_treasures(treasure_bag):

    middle = len(treasure_bag) // 2

    my_share = treasure_bag[:middle]
    friend_share = treasure_bag[middle:]

    print("\nMy Share:")
    print(my_share)

    print("\nFriend Share:")
    print(friend_share)


# 7. Treasure Map (Tuple Loop)


def treasure_map():

    islands = ("island_1", "island_2", "island_3")

    print("\nSearching Islands:\n")

    for island in islands:

        print(f"Searching {island} for treasures...")


# 8. Final Challenge – Interactive Game


def interactive_game(treasure_bag):

    print("\n--- INTERACTIVE TREASURE GAME ---")

    # Add treasure

    add_item = input("Enter Treasure To Add: ")

    treasure_bag.append(add_item)

    print("\nBag After Adding Treasure:")
    print(treasure_bag)

    # Remove treasure

    remove_item = input("\nEnter Treasure To Remove: ")

    if remove_item in treasure_bag:

        treasure_bag.remove(remove_item)

        print("\nBag After Removing Treasure:")
        print(treasure_bag)

    else:
        print("Treasure Not Found")


# ================= MAIN PROGRAM =================

bag = build_treasure_bag()

bag = add_rare_treasures(bag)

bag = island_swaps(bag)

sorting_and_counting(bag)

searching_bag(bag)

sharing_treasures(bag)

treasure_map()

interactive_game(bag)
