def display(title, data):
    print(f"\n{title}:")
    print(data)


def build_treasure_bag():
    treasure_bag = ["gold coin", "silver coin", "ruby", "pearl"]
    display("Treasure Bag", treasure_bag)
    return treasure_bag


def add_rare_treasures(treasure_bag):
    treasure_bag.extend(("diamond", "magic ring"))
    display("After Adding Rare Treasures", treasure_bag)
    return treasure_bag


def island_swaps(treasure_bag):
    if "silver coin" in treasure_bag:
        treasure_bag.remove("silver coin")

    if "ruby" in treasure_bag:
        treasure_bag[treasure_bag.index("ruby")] = "emerald"

    display("After Island Swaps", treasure_bag)
    return treasure_bag


def sorting_and_counting(treasure_bag):
    print("\nNumber of Gold Coins:", treasure_bag.count("gold coin"))

    treasure_bag.sort()
    display("Sorted Treasure Bag", treasure_bag)

    treasure_bag.reverse()
    display("Reversed Treasure Bag", treasure_bag)

    return treasure_bag


def search_bag(treasure_bag):
    print("\nSearching the Bag")

    print(
        "Magic Ring Found!"
        if "magic ring" in treasure_bag
        else "Magic Ring Not Found!"
    )

    if "emerald" in treasure_bag:
        print("Emerald Position:", treasure_bag.index("emerald"))
    else:
        print("Emerald Not Found!")


def share_treasures(treasure_bag):
    middle = len(treasure_bag) // 2

    my_share = treasure_bag[:middle]
    friend_share = treasure_bag[middle:]

    display("My Share", my_share)
    display("Friend Share", friend_share)


def treasure_map():
    islands = ("island_1", "island_2", "island_3")

    print("\nTreasure Map Search")
    for island in islands:
        print(f"Searching {island} for treasures...")


def interactive_game(treasure_bag):
    print("\nFinal Challenge - Interactive Game")

    treasure_bag.append(input("Enter a treasure to add: "))
    display("Bag After Adding", treasure_bag)

    remove_treasure = input("Enter a treasure to remove: ")

    if remove_treasure in treasure_bag:
        treasure_bag.remove(remove_treasure)
        print(f"{remove_treasure} removed successfully.")
    else:
        print("Treasure not found in bag.")

    display("Final Treasure Bag", treasure_bag)


def main():
    bag = build_treasure_bag()
    add_rare_treasures(bag)
    island_swaps(bag)
    sorting_and_counting(bag)
    search_bag(bag)
    share_treasures(bag)
    treasure_map()
    interactive_game(bag)


main()