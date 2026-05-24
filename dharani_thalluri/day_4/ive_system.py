import json

IVR_FILE = "ivr_data.json"

DEFAULT_DATA = {"recharges": [], "data_plans": [], "bill_payments": [], "plan_upgrades": [], "complaints": []}

try:
    with open(IVR_FILE, "r") as f:
        ivr_data = json.load(f)

except FileNotFoundError:
    ivr_data = DEFAULT_DATA.copy()

except json.JSONDecodeError:
    print("Invalid JSON file. Creating new data...")
    ivr_data = DEFAULT_DATA.copy()


# SAVE DATA


def save_data():
    with open(IVR_FILE, "w") as f:
        json.dump(ivr_data, f, indent=4)


# SUCCESS MENU


def success_menu():

    while True:

        print("\n1. Continue Exploring")
        print("2. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                return

            elif choice == 2:
                print("Thank You for using our service!")
                exit()

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter numbers only!")


# MAIN MENU


def main_menu():

    while True:

        try:
            print(
                "===== MAIN MENU ====="
                "\n 1. Mobile Services"
                "\n 2. Internet Services"
                "\n 3. TV & OTT Services"
                "\n 4. Talk to Customer Support"
                "\n 5. Exit"
            )

            choice = int(input("Enter choice: "))

            if choice == 1:
                mobile_services()

            elif choice == 2:
                internet_services()

            elif choice == 3:
                tv_ott_services()

            elif choice == 4:
                print("Connecting to Customer Support...")

            elif choice == 5:
                print("Thank You for using our service!")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter numbers only!")


#  MOBILE SERVICES


def mobile_services():

    while True:

        try:
            print("--- MOBILE SERVICES ---" "\n 1. Prepaid" "\n 2. Postpaid" "\n 3. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:
                prepaid()

            elif choice == 2:
                postpaid()

            elif choice == 3:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter valid number!")


# PREPAID


def prepaid():

    while True:

        try:
            print("\n--- PREPAID ---" "\n 1. Balance Inquiry" "\n 2. Recharge" "\n 3. Data Plans" "\n 4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("Balance = ₹250")

            elif choice == 2:
                recharge_menu()

            elif choice == 3:
                data_plans()

            elif choice == 4:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Numbers only!")


# RECHARGE


def recharge_menu():

    while True:

        try:
            print("--- RECHARGE ---" "\n 1. Credit Card" "\n 2. UPI" "\n 3. Recharge History" "\n 4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                amount = int(input("Enter recharge amount: "))

                recharge = {"method": "Credit Card", "amount": amount}

                ivr_data["recharges"].append(recharge)

                save_data()

                print("Recharge Successful!")
                print("Thank you for recharging!")

                success_menu()

            elif choice == 2:

                amount = int(input("Enter recharge amount: "))

                recharge = {"method": "UPI", "amount": amount}

                ivr_data["recharges"].append(recharge)

                save_data()

                print("Recharge Successful!")
                print("Thank you for recharging!")

                success_menu()

            elif choice == 3:

                if not ivr_data["recharges"]:
                    print("No recharge history found")

                else:

                    print("\n--- RECHARGE HISTORY ---")

                    for recharge in ivr_data["recharges"]:

                        print(f"Method : {recharge['method']}")
                        print(f"Amount : ₹{recharge['amount']}")
                        print("----------------------")

            elif choice == 4:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid Input")


# DATA PLANS


def data_plans():

    while True:

        try:
            print("--- DATA PLANS ---" "\n 1. 1GB/day" "\n 2. 2GB/day" "\n 3. Unlimited" "\n 4. View Selected Plans" "\n 5. Back")

            choice = int(input("Enter choice: "))

            plans = {1: "1GB/day Plan", 2: "2GB/day Plan", 3: "Unlimited Plan"}

            if choice in plans:

                plan = {"plan": plans[choice]}

                ivr_data["data_plans"].append(plan)

                save_data()

                print(plans[choice], "Selected")
                print("Thank you for choosing our service!")

                success_menu()

            elif choice == 4:

                if not ivr_data["data_plans"]:
                    print("No plans selected")

                else:

                    print("\n--- SELECTED PLANS ---")

                    for plan in ivr_data["data_plans"]:
                        print(plan["plan"])

            elif choice == 5:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid Input")


# POSTPAID


def postpaid():

    while True:

        try:
            print("\n--- POSTPAID ---" "\n 1. Current Bill" "\n 2. Bill Payment" "\n 3. Plan Upgrade" "\n 4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("Current Bill = ₹999")

            elif choice == 2:
                bill_payment()

            elif choice == 3:
                plan_upgrade()

            elif choice == 4:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter number only")


# BILL PAYMENT


def bill_payment():

    while True:

        try:
            print("--- BILL PAYMENT ---" "\n 1. NetBanking" "\n 2. Wallet" "\n 3. View Payment History" "\n 4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                payment = {"method": "NetBanking"}

                ivr_data["bill_payments"].append(payment)

                save_data()

                print("Paid via NetBanking")
                print("Payment Successful!")

                success_menu()

            elif choice == 2:

                payment = {"method": "Wallet"}

                ivr_data["bill_payments"].append(payment)

                save_data()

                print("Paid via Wallet")
                print("Payment Successful!")

                success_menu()

            elif choice == 3:

                print("\n--- PAYMENT HISTORY ---")

                for payment in ivr_data["bill_payments"]:
                    print(payment["method"])

            elif choice == 4:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid Input")


# PLAN UPGRADE


def plan_upgrade():

    while True:

        try:
            print("\n--- PLAN UPGRADE ---" "\n 1. Silver → Gold" "\n 2. Gold → Platinum" "\n 3. View Upgrade History" "\n 4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                upgrade = {"upgrade": "Silver to Gold"}

                ivr_data["plan_upgrades"].append(upgrade)

                save_data()

                print("Silver upgraded to Gold")
                print("Thank you for upgrading!")

                success_menu()

            elif choice == 2:

                upgrade = {"upgrade": "Gold to Platinum"}

                ivr_data["plan_upgrades"].append(upgrade)

                save_data()

                print("Gold upgraded to Platinum")
                print("Thank you for upgrading!")

                success_menu()

            elif choice == 3:

                print("\n--- UPGRADE HISTORY ---")

                for upgrade in ivr_data["plan_upgrades"]:
                    print(upgrade["upgrade"])

            elif choice == 4:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Wrong Input")


# INTERNET SERVICES


def internet_services():

    while True:

        try:
            print("\n--- INTERNET SERVICES ---" "\n 1. Broadband" "\n 2. Fiber" "\n 3. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("Broadband Selected")

                success_menu()

            elif choice == 2:
                print("Fiber Selected")

                success_menu()

            elif choice == 3:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Numbers only")


# TV & OTT SERVICES


def tv_ott_services():

    while True:

        try:
            print("\n--- TV & OTT SERVICES ---" "\n1. Channel Packs" "\n 2. Recharge Plans" "\n 3. Complaint" "\n 4. View Complaints" "\n 5. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                print("Sports / Movies / All-in-One Pack")

                success_menu()

            elif choice == 2:

                print("1 Month / 6 Months / 12 Months Plans")

                success_menu()

            elif choice == 3:

                issue = input("Enter complaint: ")

                complaint = {"issue": issue}
                ivr_data["complaints"].append(complaint)

                save_data()

                print("Complaint Registered Successfully")

                success_menu()

            elif choice == 4:

                print("\n--- COMPLAINT HISTORY ---")

                for complaint in ivr_data["complaints"]:
                    print(complaint["issue"])

            elif choice == 5:
                return

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid Input")


main_menu()
