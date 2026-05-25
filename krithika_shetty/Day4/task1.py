def show_menu(title, options):
    print(f"\n--- {title} ---")
    for key, value in options.items():
        print(f"{key}. {value}")


def customer_support():
    print("\nConnecting to Customer Support...")
    print("Please wait...")


def prepaid_menu():
    while True:
        show_menu("Prepaid", {"1": "Balance Inquiry", "2": "Recharge", "3": "Data Plans", "4": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            print("Your balance is ₹250.")
        elif choice == "2":
            print("Recharge successful.")
        elif choice == "3":
            print("Data Plan Activated.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def postpaid_menu():
    while True:
        show_menu("Postpaid", {"1": "Current Bill", "2": "Bill Payment", "3": "Plan Upgrade", "4": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current bill amount: ₹899")
        elif choice == "2":
            print("Bill payment successful.")
        elif choice == "3":
            print("Plan upgraded successfully.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def mobile_services():
    while True:
        show_menu("Mobile Services", {"1": "Prepaid", "2": "Postpaid", "3": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            prepaid_menu()
        elif choice == "2":
            postpaid_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def broadband_menu():
    while True:
        show_menu("Broadband", {"1": "Usage Details", "2": "Renew Plan", "3": "Change Router", "4": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current usage: 120 GB")
        elif choice == "2":
            print("Plan renewed successfully.")
        elif choice == "3":
            print("Router change request submitted.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def fiber_menu():
    while True:
        show_menu("Fiber", {"1": "New Connection", "2": "Status Check", "3": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            print("New connection request submitted.")
        elif choice == "2":
            print("Connection status: Processing")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def internet_services():
    while True:
        show_menu("Internet Services", {"1": "Broadband", "2": "Fiber", "3": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            broadband_menu()
        elif choice == "2":
            fiber_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def tv_ott_services():
    while True:
        show_menu("TV & OTT Services", {"1": "Channel Packs", "2": "Recharge", "3": "Complaint", "4": "Back"})

        choice = input("Enter choice: ")

        if choice == "1":
            print("Channel Pack Activated.")
        elif choice == "2":
            print("OTT Recharge Successful.")
        elif choice == "3":
            print("Complaint Registered.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def main_menu():
    while True:
        show_menu(
            "IVR MAIN MENU",
            {"1": "Mobile Services", "2": "Internet Services", "3": "TV & OTT Services", "4": "Talk to Customer Support", "5": "Exit"},
        )

        choice = input("Enter choice: ")

        if choice == "1":
            mobile_services()
        elif choice == "2":
            internet_services()
        elif choice == "3":
            tv_ott_services()
        elif choice == "4":
            customer_support()
        elif choice == "5":
            print("Thank you for using IVR System!")
            break
        else:
            print("Invalid choice!")


main_menu()
