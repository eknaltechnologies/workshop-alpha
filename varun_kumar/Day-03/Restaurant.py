import json
try:
    with open("restaurant.json", "r") as f:
        menu = json.load(f)

except FileNotFoundError:
    print("File not found, creating new menu...")
    menu = {}


while True:

    print("\n---- RESTAURANT MENU ----")
    print("1. Add Item")
    print("2. View Menu")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Order Food")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    # Add Item
    if choice == 1:

        item = input("Enter item name: ")
        price = int(input("Enter item price: "))

        menu[item] = price

        print("Item Added Successfully")

    # View Menu
    elif choice == 2:

        if menu == {}:
            print("Menu is empty")

        else:
            print("\nAvailable Items")

            for i, j in menu.items():
                print(i, ":", j)

    # Update Item
    elif choice == 3:

        item = input("Enter item name to update: ")

        if item in menu:

            new_price = int(input("Enter new price: "))

            menu[item] = new_price

            print("Item Updated")

        else:
            print("Item not found")

    # Delete Item
    elif choice == 4:

        item = input("Enter item name to delete: ")

        if item in menu:

            del menu[item]

            print("Item Deleted")

        else:
            print("Item not found")

    # Order Food
    elif choice == 5:

        total = 0

        while True:

            print("\nMENU")

            for i, j in menu.items():
                print(i, ":", j)

            food = input("Enter food name: ")

            if food in menu:

                qty = int(input("Enter quantity: "))

                bill = menu[food] * qty

                total += bill

                print("Added Successfully")
                print("Item Bill =", bill)

            else:
                print("Food not available")

            more = input("Want more items? yes/no: ")

            if more == "no":
                break

        print("\nTotal Bill =", total)

    # Exit
    elif choice == 6:

        print("Thank You Visit Again")
        break

    else:
        print("Invalid Choice")

    # Save Data
    with open("restaurant.json", "w") as f:
        json.dump(menu, f, indent=4)