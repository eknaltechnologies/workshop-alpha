#Day 3 Unit Converter
import json

try:
    with open("unit_converter.json", "r") as f:
        converter = json.load(f)
except FileNotFoundError:
    converter = {
        "history": {}
    }

print("Welcome to Unit Converter!")
print("1. KM to M")
print("2. M to KM")
print("3. View History")
print("4. Delete History")
print("5. Exit")

user_choice = int(input("Select an option (1-5): "))

if user_choice == 1:
    km = float(input("Enter kilometers: "))
    meters = km * 1000

    converter["history"][f"{km} KM"] = f"{meters} M"

    print(f"{km} KM = {meters} M")

elif user_choice == 2:
    meters = float(input("Enter meters: "))
    km = meters / 1000

    converter["history"][f"{meters} M"] = f"{km} KM"

    print(f"{meters} M = {km} KM")

elif user_choice == 3:
    if not converter["history"]:
        print("No conversion history found.")
    else:
        print("Conversion History:")
        for key, value in converter["history"].items():
            print(f"{key} -> {value}")

elif user_choice == 4:
    key = input("Enter conversion to delete: ")

    if key in converter["history"]:
        del converter["history"][key]
        print("History deleted.")
    else:
        print("Record not found.")

elif user_choice == 5:
    print("Thank you!")

with open("unit_converter.json", "w") as f:
    json.dump(converter, f, indent=4)