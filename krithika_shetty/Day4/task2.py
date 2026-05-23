def build_treasure_bag():
    treasure_bag = []

    treasures = ["gold coin", "silver coin", "ruby", "pearl"]

    for item in treasures:
        treasure_bag.append(item)

    print("\nTreasure Bag:")
    print(treasure_bag)

    return treasure_bag


def add_rare_treasures(treasure_bag):
    rare_treasures = ("diamond", "magic ring")

    treasure_bag.extend(rare_treasures)

    print("\nAfter Adding Rare Treasures:")
    print(treasure_bag)

    return treasure_bag


def island_swaps(treasure_bag):
    if "silver coin" in treasure_bag:
        treasure_bag.remove("silver coin")

    if "ruby" in treasure_bag:
        index = treasure_bag.index("ruby")
        treasure_bag[index] = "emerald"

    print("\nAfter Island Swaps:")
    print(treasure_bag)

    return treasure_bag


def sorting_and_counting(treasure_bag):
    count = treasure_bag.count("gold coin")
    print("\nNumber of Gold Coins:", count)

    treasure_bag.sort()
    print("\nSorted Treasure Bag:")
    print(treasure_bag)

    treasure_bag.reverse()
    print("\nReversed Treasure Bag:")
    print(treasure_bag)

    return treasure_bag


def search_bag(treasure_bag):
    print("\nSearching the Bag")

    if "magic ring" in treasure_bag:
        print("Magic Ring Found!")
    else:
        print("Magic Ring Not Found!")

    if "emerald" in treasure_bag:
        print("Emerald Position:", treasure_bag.index("emerald"))
    else:
        print("Emerald Not Found!")


def share_treasures(treasure_bag):
    middle = len(treasure_bag) // 2

    my_share = treasure_bag[:middle]
    friend_share = treasure_bag[middle:]

    print("\nMy Share:")
    print(my_share)

    print("\nFriend Share:")
    print(friend_share)


def treasure_map():
    islands = ("island_1", "island_2", "island_3")

    print("\nTreasure Map Search")

    for island in islands:
        print(f"Searching {island} for treasures...")


def interactive_game(treasure_bag):
    print("\nFinal Challenge - Interactive Game")

    new_treasure = input("Enter a treasure to add: ")
    treasure_bag.append(new_treasure)

    print("\nBag After Adding:")
    print(treasure_bag)

    remove_treasure = input("Enter a treasure to remove: ")

    if remove_treasure in treasure_bag:
        treasure_bag.remove(remove_treasure)
        print(f"{remove_treasure} removed successfully.")
    else:
        print("Treasure not found in bag.")

    print("\nFinal Treasure Bag:")
    print(treasure_bag)


def main():
    bag = build_treasure_bag()

    bag = add_rare_treasures(bag)

    bag = island_swaps(bag)

    bag = sorting_and_counting(bag)

    search_bag(bag)

    share_treasures(bag)

    treasure_map()

    interactive_game(bag)


main()