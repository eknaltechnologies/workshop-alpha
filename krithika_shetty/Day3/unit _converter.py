# Day 3 Unit Converter

import json

FILENAME = "unit_converter.json"


def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def add_history(data, original, converted):
    data["history"][original] = converted


try:
    with open(FILENAME, "r") as file:
        unit_data = json.load(file)
except FileNotFoundError:
    unit_data = {"history": {}}

while True:

    print("\n===== UNIT CONVERTER =====")
    print("1. KM -> M")
    print("2. M -> KM")
    print("3. KG -> G")
    print("4. G -> KG")
    print("5. View History")
    print("6. Delete History")
    print("7. Inches -> CM")
    print("8. CM -> Inches")
    print("9. Total Conversions")
    print("10. Exit")

    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        km = float(input("Enter kilometers: "))
        result = km * 1000
        add_history(unit_data, f"{km} KM", f"{result} M")
        print(f"Converted Value = {result} M")

    elif choice == 2:
        meters = float(input("Enter meters: "))
        result = meters / 1000
        add_history(unit_data, f"{meters} M", f"{result} KM")
        print(f"Converted Value = {result} KM")

    elif choice == 3:
        kg = float(input("Enter kilograms: "))
        result = kg * 1000
        add_history(unit_data, f"{kg} KG", f"{result} G")
        print(f"Converted Value = {result} G")

    elif choice == 4:
        grams = float(input("Enter grams: "))
        result = grams / 1000
        add_history(unit_data, f"{grams} G", f"{result} KG")
        print(f"Converted Value = {result} KG")

    elif choice == 5:
        if not unit_data["history"]:
            print("No conversion history available.")
        else:
            print("\n===== CONVERSION HISTORY =====")
            for original, converted in unit_data["history"].items():
                print(f"{original} --> {converted}")

    elif choice == 6:
        key = input("Enter conversion key to delete: ")

        if key in unit_data["history"]:
            del unit_data["history"][key]
            print("History deleted successfully.")
        else:
            print("Conversion record not found.")

    elif choice == 7:
        inches = float(input("Enter inches: "))
        cm = inches * 2.54
        add_history(unit_data, f"{inches} IN", f"{cm} CM")
        print(f"{inches} IN = {cm} CM")

    elif choice == 8:
        cm = float(input("Enter centimeters: "))
        inches = cm / 2.54
        add_history(unit_data, f"{cm} CM", f"{inches} IN")
        print(f"{cm} CM = {inches} IN")

    elif choice == 9:
        print(f"Total Conversions = {len(unit_data['history'])}")

    elif choice == 10:
        save_data(unit_data)
        print("Data saved successfully.")
        print("Exiting Unit Converter...")
        break

    else:
        print("Invalid Choice!")

    save_data(unit_data)