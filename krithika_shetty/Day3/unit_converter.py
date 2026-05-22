import json

try:
    with open("unit_converter.json", "r") as file:
        unit_data = json.load(file)
except FileNotFoundError:
    unit_data = {"history": {}}

while True:

    print("\n===== UNIT CONVERTER =====")
    print("1.KM->M  2.M->KM  3.KG->G  4.G->KG  5.View History  6.Delete History  7.Total Conversions  8.Exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:

        km = float(input("Enter kilometers: "))
        result = km * 1000

        unit_data["history"][f"{km} KM"] = f"{result} M"

        print(f"Converted Value = {result} M")

    elif choice == 2:

        meters = float(input("Enter meters: "))
        result = meters / 1000

        unit_data["history"][f"{meters} M"] = f"{result} KM"

        print(f"Converted Value = {result} KM")

    elif choice == 3:

        kg = float(input("Enter kilograms: "))
        result = kg * 1000

        unit_data["history"][f"{kg} KG"] = f"{result} G"

        print(f"Converted Value = {result} G")

    elif choice == 4:

        grams = float(input("Enter grams: "))
        result = grams / 1000

        unit_data["history"][f"{grams} G"] = f"{result} KG"

        print(f"Converted Value = {result} KG")

    elif choice == 5:

        if not unit_data["history"]:
            print("No conversion history available.")

        else:
            print("\nConversion History")

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
        unit_data ["history"][f"{inches} IN"] = f"{cm} CM"
        print(f"{inches} IN = {cm} CM")

    elif choice == 8:
        cm = float(input("Enter centimeters: "))
        inches = cm / 2.54
        unit_data ["history"][f"{cm} CM"] = f"{inches} IN"
        print(f"{cm} CM = {inches} IN")


    elif choice == 9:

        total = len(unit_data["history"])
        print(f"Total Conversions = {total}")

    elif choice == 10:

        with open("unit_converter.json", "w") as file:
            json.dump(unit_data, file, indent=4)

        print("Data saved successfully.")
        print("Exiting Unit Converter...")
        break
    # EXIT

    elif choice == 11:

        with open("unit_converter.json", "w") as f:

            json.dump(unit_data, file, indent=4)

        print("Data saved successfully!")

        print("Exiting...")

        break
    

    
    else:
        print("Invalid Choice!")

    with open("unit_converter.json", "w") as file:
        json.dump(unit_data, file, indent=4)