def mobile_services():
    while True:
        print("\n--- Mobile Services ---")
        print("1. Prepaid")
        print("2. Postpaid")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            prepaid_menu()
        elif choice == "2":
            postpaid_menu()
        elif choice == "3":
            return
        else:
            print("Invalid choice!")


def prepaid_menu():
    while True:
        print("\n--- Prepaid ---")
        print("1. Balance Inquiry")
        print("2. Recharge")
        print("3. Data Plans")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Your balance is ₹250.")
        elif choice == "2":
            recharge_menu()
        elif choice == "3":
            data_plans()
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


def recharge_menu():
    while True:
        print("\n--- Recharge ---")
        print("1. Using Credit Card")
        print("2. Using UPI")
        print("3. Recharge History")
        print("4. Back for Prepaid Menu")
        print("5. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Recharge via Credit Card successful.")
        elif choice == "2":
            print("Recharge via UPI successful.")
        elif choice == "3":
            print("Showing recharge history...")
        elif choice == "4":
            return
        elif choice == "5":
            main_menu()
            return
        else:
            print("Invalid choice!")


def data_plans():
    while True:
        print("\n--- Data Plans ---")
        print("1. 1GB/day")
        print("2. 2GB/day")
        print("3. Unlimited")
        print("4. Back for Prepaid Menu")
        print("5. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("1GB/day plan selected.")
        elif choice == "2":
            print("2GB/day plan selected.")
        elif choice == "3":
            print("Unlimited plan selected.")
        elif choice == "4":
            return
        elif choice == "5":
            main_menu()
            return
        else:
            print("Invalid choice!")


def postpaid_menu():
    while True:
        print("\n--- Postpaid ---")
        print("1. Current Bill")
        print("2. Bill Payment")
        print("3. Plan Upgrade")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current bill amount: ₹899")
        elif choice == "2":
            bill_payment()
        elif choice == "3":
            plan_upgrade()
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


def bill_payment():
    while True:
        print("\n--- Bill Payment ---")
        print("1. Pay via NetBanking")
        print("2. Pay via Wallet")
        print("3. Back for Postpaid Menu")
        print("4. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Payment via NetBanking successful.")
        elif choice == "2":
            print("Payment via Wallet successful.")
        elif choice == "3":
            return
        elif choice == "4":
            main_menu()
            return
        else:
            print("Invalid choice!")


def plan_upgrade():
    while True:
        print("\n--- Plan Upgrade ---")
        print("1. Silver to Gold")
        print("2. Gold to Platinum")
        print("3. Back for Postpaid Menu")
        print("4. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Upgraded from Silver to Gold.")
        elif choice == "2":
            print("Upgraded from Gold to Platinum.")
        elif choice == "3":
            return
        elif choice == "4":
            main_menu()
            return
        else:
            print("Invalid choice!")


def internet_services():
    while True:
        print("\n--- Internet Services ---")
        print("1. Broadband")
        print("2. Fiber")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            broadband_menu()
        elif choice == "2":
            fiber_menu()
        elif choice == "3":
            return
        else:
            print("Invalid choice!")


def broadband_menu():
    while True:
        print("\n--- Broadband ---")
        print("1. Usage Details")
        print("2. Renew Plan")
        print("3. Change Router")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current usage: 120 GB")
        elif choice == "2":
            renew_plan()
        elif choice == "3":
            change_router()
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


def renew_plan():
    while True:
        print("\n--- Renew Plan ---")
        print("1. Monthly Plan")
        print("2. Quarterly Plan")
        print("3. Yearly Plan")
        print("4. Back for Broadband Menu")
        print("5. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Monthly plan renewed.")
        elif choice == "2":
            print("Quarterly plan renewed.")
        elif choice == "3":
            print("Yearly plan renewed.")
        elif choice == "4":
            return
        elif choice == "5":
            main_menu()
            return
        else:
            print("Invalid choice!")


def change_router():
    while True:
        print("\n--- Change Router ---")
        print("1. Request Technician Visit")
        print("2. Self Installation Guide")
        print("3. Back for Broadband Menu")
        print("4. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Technician visit requested.")
        elif choice == "2":
            print("Self installation guide sent.")
        elif choice == "3":
            return
        elif choice == "4":
            main_menu()
            return
        else:
            print("Invalid choice!")


def fiber_menu():
    while True:
        print("\n--- Fiber ---")
        print("1. New Connection")
        print("2. Status Check")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            new_connection()
        elif choice == "2":
            print("Connection status: Processing")
        elif choice == "3":
            return
        else:
            print("Invalid choice!")


def new_connection():
    while True:
        print("\n--- New Connection ---")
        print("1. Residential")
        print("2. Business")
        print("3. Back for Fiber Menu")
        print("4. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Residential connection requested.")
        elif choice == "2":
            print("Business connection requested.")
        elif choice == "3":
            return
        elif choice == "4":
            main_menu()
            return
        else:
            print("Invalid choice!")


def tv_ott_services():
    while True:
        print("\n--- TV & OTT Services ---")
        print("1. Channel Packs")
        print("2. Recharge")
        print("3. Complaint")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            channel_packs()
        elif choice == "2":
            ott_recharge()
        elif choice == "3":
            complaint_menu()
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


def channel_packs():
    while True:
        print("\n--- Channel Packs ---")
        print("1. Sports Pack")
        print("2. Movies Pack")
        print("3. All-in-One Pack")
        print("4. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Sports Pack activated.")
        elif choice == "2":
            print("Movies Pack activated.")
        elif choice == "3":
            print("All-in-One Pack activated.")
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


def ott_recharge():
    while True:
        print("\n--- OTT Recharge ---")
        print("1. 1 Month")
        print("2. 6 Months")
        print("3. 12 Months")
        print("4. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("1 Month Recharge successful.")
        elif choice == "2":
            print("6 Months Recharge successful.")
        elif choice == "3":
            print("12 Months Recharge successful.")
        elif choice == "4":
            return
        else:
            print("Invalid choice!")


def complaint_menu():
    while True:
        print("\n--- Complaint ---")
        print("1. No Signal")
        print("2. Overcharged")
        print("3. Back for Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print("No Signal complaint registered.")
        elif choice == "2":
            print("Overcharged complaint registered.")
        elif choice == "3":
            return
        else:
            print("Invalid choice!")


def customer_support():
    print("\nConnecting to Customer Support...")
    print("Please wait...")


def main_menu():
    while True:
        print("\n===== IVR MAIN MENU =====")
        print("1. Mobile Services")
        print("2. Internet Services")
        print("3. TV & OTT Services")
        print("4. Talk to Customer Support")
        print("5. Exit")

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