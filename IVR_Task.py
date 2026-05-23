# Recursive IVR System in Python

def prepaid_menu():
    while True:
        print("\n--- Prepaid Menu ---")
        print("1. Balance Inquiry")
        print("2. Recharge")
        print("3. Data Plans")
        print("4. Back to Mobile Services")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Your balance is Rs. 250")

        elif choice == "2":
            recharge_menu()

        elif choice == "3":
            data_plans_menu()

        elif choice == "4":
            return

        elif choice == "5":
            main_menu()

        else:
            print("Invalid choice!")


def recharge_menu():
    while True:
        print("\n--- Recharge Menu ---")
        print("1. Using Credit Card")
        print("2. Using UPI")
        print("3. Recharge History")
        print("4. Back to Prepaid Menu")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Recharge done using Credit Card")

        elif choice == "2":
            print("Recharge done using UPI")

        elif choice == "3":
            print("Showing Recharge History")

        elif choice == "4":
            return

        elif choice == "5":
            main_menu()

        else:
            print("Invalid choice!")


def data_plans_menu():
    while True:
        print("\n--- Data Plans Menu ---")
        print("1. 1GB/day")
        print("2. 2GB/day")
        print("3. Unlimited")
        print("4. Back to Prepaid Menu")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("1GB/day Plan Activated")

        elif choice == "2":
            print("2GB/day Plan Activated")

        elif choice == "3":
            print("Unlimited Plan Activated")

        elif choice == "4":
            return

        elif choice == "5":
            main_menu()

        else:
            print("Invalid choice!")


def postpaid_menu():
    while True:
        print("\n--- Postpaid Menu ---")
        print("1. Current Bill")
        print("2. Bill Payment")
        print("3. Plan Upgrade")
        print("4. Back to Mobile Services")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Your current bill is Rs. 999")

        elif choice == "2":
            bill_payment_menu()

        elif choice == "3":
            plan_upgrade_menu()

        elif choice == "4":
            return

        elif choice == "5":
            main_menu()

        else:
            print("Invalid choice!")


def bill_payment_menu():
    while True:
        print("\n--- Bill Payment Menu ---")
        print("1. Pay via NetBanking")
        print("2. Pay via Wallet")
        print("3. Back to Postpaid Menu")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Payment done using NetBanking")

        elif choice == "2":
            print("Payment done using Wallet")

        elif choice == "3":
            return

        elif choice == "4":
            main_menu()

        else:
            print("Invalid choice!")


def plan_upgrade_menu():
    while True:
        print("\n--- Plan Upgrade Menu ---")
        print("1. Silver to Gold")
        print("2. Gold to Platinum")
        print("3. Back to Postpaid Menu")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Plan upgraded from Silver to Gold")

        elif choice == "2":
            print("Plan upgraded from Gold to Platinum")

        elif choice == "3":
            return

        elif choice == "4":
            main_menu()

        else:
            print("Invalid choice!")


def mobile_services_menu():
    while True:
        print("\n--- Mobile Services ---")
        print("1. Prepaid")
        print("2. Postpaid")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            prepaid_menu()

        elif choice == "2":
            postpaid_menu()

        elif choice == "3":
            return

        else:
            print("Invalid choice!")


def broadband_menu():
    while True:
        print("\n--- Broadband Menu ---")
        print("1. Usage Details")
        print("2. Renew Plan")
        print("3. Change Router")
        print("4. Back to Internet Services")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Usage: 250GB used")

        elif choice == "2":
            renew_plan_menu()

        elif choice == "3":
            router_menu()

        elif choice == "4":
            return

        elif choice == "5":
            main_menu()

        else:
            print("Invalid choice!")


def renew_plan_menu():
    while True:
        print("\n--- Renew Plan Menu ---")
        print("1. Monthly Plan")
        print("2. Quarterly Plan")
        print("3. Yearly Plan")
        print("4. Back to Broadband Menu")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Monthly Plan Activated")

        elif choice == "2":
            print("Quarterly Plan Activated")

        elif choice == "3":
            print("Yearly Plan Activated")

        elif choice == "4":
            return

        elif choice == "5":
            main_menu()

        else:
            print("Invalid choice!")


def router_menu():
    while True:
        print("\n--- Change Router Menu ---")
        print("1. Request Technician Visit")
        print("2. Self Installation Guide")
        print("3. Back to Broadband Menu")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Technician Visit Requested")

        elif choice == "2":
            print("Showing Self Installation Guide")

        elif choice == "3":
            return

        elif choice == "4":
            main_menu()

        else:
            print("Invalid choice!")


def fiber_menu():
    while True:
        print("\n--- Fiber Menu ---")
        print("1. New Connection")
        print("2. Status Check")
        print("3. Back to Internet Services")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            new_connection_menu()

        elif choice == "2":
            print("Connection Status: Active")

        elif choice == "3":
            return

        elif choice == "4":
            main_menu()

        else:
            print("Invalid choice!")


def new_connection_menu():
    while True:
        print("\n--- New Connection Menu ---")
        print("1. Residential")
        print("2. Business")
        print("3. Back to Fiber Menu")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Residential Connection Requested")

        elif choice == "2":
            print("Business Connection Requested")

        elif choice == "3":
            return

        elif choice == "4":
            main_menu()

        else:
            print("Invalid choice!")


def internet_services_menu():
    while True:
        print("\n--- Internet Services ---")
        print("1. Broadband")
        print("2. Fiber")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            broadband_menu()

        elif choice == "2":
            fiber_menu()

        elif choice == "3":
            return

        else:
            print("Invalid choice!")


def ott_menu():
    while True:
        print("\n--- TV & OTT Services ---")
        print("1. Channel Packs")
        print("2. Recharge")
        print("3. Complaint")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("1. Sports Pack")
            print("2. Movies Pack")
            print("3. All-in-One Pack")

        elif choice == "2":
            print("1 Month / 6 Months / 12 Months Recharge")

        elif choice == "3":
            print("Complaint Registered")

        elif choice == "4":
            return

        else:
            print("Invalid choice!")


def main_menu():
    while True:
        print("\n====== MAIN MENU ======")
        print("1. Mobile Services")
        print("2. Internet Services")
        print("3. TV & OTT Services")
        print("4. Talk to Customer Support")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            mobile_services_menu()

        elif choice == "2":
            internet_services_menu()

        elif choice == "3":
            ott_menu()

        elif choice == "4":
            print("Connecting to Customer Support...")

        elif choice == "5":
            print("Thank you for using IVR System!")
            break

        else:
            print("Invalid choice!")


# Start Program
main_menu()