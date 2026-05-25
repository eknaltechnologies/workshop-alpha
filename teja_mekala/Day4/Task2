def create_inventory():
    inventory = []

    items = ["sword", "shield", "helmet", "boots"]

    for thing in items:
        inventory.append(thing)

    print("\nPlayer Inventory:")
    print(inventory)

    return inventory


def add_special_items(inventory):
    special_items = ("magic potion", "dragon egg")

    inventory.extend(special_items)

    print("\nAfter Adding Special Items:")
    print(inventory)

    return inventory


def update_inventory(inventory):

    if "shield" in inventory:
        inventory.remove("shield")

    if "helmet" in inventory:
        position = inventory.index("helmet")
        inventory[position] = "armor"

    print("\nUpdated Inventory:")
    print(inventory)

    return inventory


def organize_inventory(inventory):

    total = inventory.count("sword")
    print("\nNumber of Swords:", total)

    inventory.sort()
    print("\nSorted Inventory:")
    print(inventory)

    inventory.reverse()
    print("\nReverse Order:")
    print(inventory)

    return inventory


def search_inventory(inventory):

    print("\nSearching Inventory")

    if "dragon egg" in inventory:
        print("Dragon Egg Found")
    else:
        print("Dragon Egg Missing")

    if "armor" in inventory:
        print("Armor Position:", inventory.index("armor"))
    else:
        print("Armor Not Available")


def divide_items(inventory):

    half = len(inventory) // 2

    player1 = inventory[:half]
    player2 = inventory[half:]

    print("\nPlayer 1 Items:")
    print(player1)

    print("\nPlayer 2 Items:")
    print(player2)


def game_levels():

    levels = ("Forest", "Castle", "Dungeon")

    print("\nExploring Game Levels")

    for area in levels:
        print(f"Entering {area}")


def game_action(inventory):

    print("\nBonus Round")

    new_item = input("Enter item to collect: ")
    inventory.append(new_item)

    print("\nInventory After Collection:")
    print(inventory)

    remove_item = input("Enter item to discard: ")

    if remove_item in inventory:
        inventory.remove(remove_item)
        print(remove_item, "removed")
    else:
        print("Item not found")

    print("\nFinal Inventory:")
    print(inventory)


def start_game():

    bag = create_inventory()

    bag = add_special_items(bag)

    bag = update_inventory(bag)

    bag = organize_inventory(bag)

    search_inventory(bag)

    divide_items(bag)

    game_levels()

    game_action(bag)


start_game()