"""import json
try:
    with open("unit_converter.json", "r") as f:
        converter = json.load(f)
except FileNotFoundError:
    converter = {
        "history": {}
    }
print("\n ****Unit Convertion****")    
print("1. KM to M")
print("2. M to KM")
print("3. G to KG")
print("4. KG to G")
print("5. IN to CM")
print("6. CM to IN")
print("7. View History")
print("8. Delete History")
print("9. exit")
user_choice = int(input("\nSelect an number(1-9): "))

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
    grams = float(input("Enter grams: "))
    kg = grams / 1000
    converter["history"][f"{grams} G"] = f"{kg} KG"
    print(f"{grams} G = {kg} KG")

elif user_choice == 4:
    kg = float(input("Enter kilograms: "))
    grams = kg * 1000
    converter["history"][f"{kg} KG"] = f"{grams} G"
    print(f"{kg} KG = {grams} G")

elif user_choice == 5:
    inches = float(input("Enter inches: "))
    cm = inches * 2.54
    converter["history"][f"{inches} IN"] = f"{cm} CM"
    print(f"{inches} IN = {cm} CM")

elif user_choice == 6:
    cm = float(input("Enter centimeters: "))
    inches = cm / 2.54
    converter["history"][f"{cm} CM"] = f"{inches} IN"
    print(f"{cm} CM = {inches} IN")

elif user_choice == 7:
    if not converter["history"]:
        print("No conversion history found.")
    else:
        print("Conversion History:")
    for key, value in converter["history"].items():
        print(f"{key} -> {value}")

elif user_choice == 8:
    key = input("Enter conversion to delete: ")

    if key in converter["history"]:
        del converter["history"][key]
        print("History deleted.")
    else:
        print("Record not found.")
elif user_choice == 9:
     print("Thank you!")

with open("unit_converter.json", "w") as f:
    json.dump(converter, f, indent=4)"""
import json

try:
    with open('unit_converter.json', 'r') as f:
        converter = json.load(f)
except FileNotFoundError:
    converter = {'history': {}}

print("\n===== UNIT CONVERTER =====\n1.KM -> M  2.M -> KM  3.G -> KG  4.KG -> G  5.IN -> CM  6.CM -> IN  7.C -> F  8. View History  9.delete history  10.exit")

user_choice = int(input("\nSelect a number (1-10): "))

if user_choice == 1:
    km = float(input("Enter kilometers: "))
    meters = km * 1000
    converter['history'][f"{km} KM"] = f"{meters} M"
    print(f"{km} KM = {meters} M")

elif user_choice == 2:
    meters = float(input("Enter meters: "))
    km = meters / 1000
    converter['history'][f"{meters} M"] = f"{km} KM"
    print(f"{meters} M = {km} KM")

elif user_choice == 3:
    grams = float(input("Enter grams: "))
    kg = grams / 1000
    converter['history'][f"{grams} G"] = f"{kg} KG"
    print(f"{grams} G = {kg} KG")

elif user_choice == 4:
    kg = float(input("Enter kilograms: "))
    grams = kg * 1000
    converter['history'][f"{kg} KG"] = f"{grams} G"
    print(f"{kg} KG = {grams} G")

elif user_choice == 5:
    inches = float(input("Enter inches: "))
    cm = inches * 2.54
    converter['history'][f"{inches} IN"] = f"{cm} CM"
    print(f"{inches} IN = {cm} CM")

elif user_choice == 6:
    cm = float(input("Enter centimeters: "))
    inches = cm / 2.54
    converter['history'][f"{cm} CM"] = f"{inches} IN"
    print(f"{cm} CM = {inches} IN")

elif user_choice == 7:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    converter['history'][f"{celsius} C"] = f"{fahrenheit} F"
    print(f"{celsius}°C = {fahrenheit}°F")

elif user_choice == 8:
    if not converter['history']:
        print("No conversion history found.")
    else:
        print("\nConversion History:")
        for key, value in converter['history'].items():
            print(f"{key} -> {value}")

elif user_choice == 9:
    key = input("Enter conversion to delete : ")
    if key in converter['history']:
        del converter['history'][key]
        print("History deleted.")
    else:
        print("Record not found.")

elif user_choice == 10:
    print("\nThank you!")
    with open('unit_converter.json', 'w') as f:
        json.dump(converter, f, indent=4)

else:
    print("Invalid choice! Please run the program again and select from 1 to 10.")