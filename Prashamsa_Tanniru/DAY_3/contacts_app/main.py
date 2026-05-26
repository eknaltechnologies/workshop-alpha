import json

DATA_FILE = "contacts.json"

try:
    with open(DATA_FILE, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}
print("Welcome to contacts app")
while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. Exit")

    choice = input("Choice: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        if name in contacts:
            print("Contact already exists.")
            continue
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        with open(DATA_FILE, "w") as file:
            json.dump(contacts, file, indent=2)
        print("Contact added.")

    elif choice == "2":
        query = input("Enter name or phone: ").strip().lower()
        found = False
        for name, data in contacts.items():
            if query in name.lower() or query == data.get("phone", "").lower():
                print(f"\nName: {name}")
                print(f"Phone: {data.get('phone','')}")
                print(f"Email: {data.get('email','')}")
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "3":
        query = input("Enter name or phone to update: ").strip().lower()
        for name, data in list(contacts.items()):
            if query in name.lower() or query == data.get("phone", "").lower():
                print("\n1. Update Name\n2. Update Phone\n3. Update Email")
                opt = input("Select option: ").strip()
                if opt == "1":
                    new_name = input("New Name: ").strip()
                    if new_name and new_name not in contacts:
                        contacts[new_name] = contacts.pop(name)
                        print("Name updated.")
                    else:
                        print("Invalid or duplicate name.")
                elif opt == "2":
                    contacts[name]["phone"] = input("New Phone: ").strip()
                    print("Phone updated.")
                elif opt == "3":
                    contacts[name]["email"] = input("New Email: ").strip()
                    print("Email updated.")
                with open(DATA_FILE, "w") as file:
                    json.dump(contacts, file, indent=2)
                break
        else:
            print("Contact not found.")

    elif choice == "4":
        query = input("Enter name or phone to delete: ").strip().lower()
        for name, data in list(contacts.items()):
            if query in name.lower() or query == data.get("phone", "").lower():
                del contacts[name]
                with open(DATA_FILE, "w") as file:
                    json.dump(contacts, file, indent=2)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid choice. Please select 1–5.")
