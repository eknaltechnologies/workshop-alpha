import json

try:
    with open("ivr_data.json", "r") as f:
        ivr_data = json.load(f)

except FileNotFoundError:
    ivr_data = {
        "recharges": [],
        "data_plans": [],
        "bill_payments": [],
        "plan_upgrades": [],
        "complaints": []
    }


# SAVE DATA

def save_data():
    with open("ivr_data.json", "w") as f:
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
            print("\n===== MAIN MENU =====")
            print("1. Mobile Services")
            print("2. Internet Services")
            print("3. TV & OTT Services")
            print("4. Talk to Customer Support")
            print("5. Exit")

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
            print("\n--- MOBILE SERVICES ---")
            print("1. Prepaid")
            print("2. Postpaid")
            print("3. Back")

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
            print("\n--- PREPAID ---")
            print("1. Balance Inquiry")
            print("2. Recharge")
            print("3. Data Plans")
            print("4. Back")

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
            print("\n--- RECHARGE ---")
            print("1. Credit Card")
            print("2. UPI")
            print("3. Recharge History")
            print("4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                amount = int(input("Enter recharge amount: "))

                recharge = {
                    "method": "Credit Card",
                    "amount": amount
                }

                ivr_data["recharges"].append(recharge)

                save_data()

                print("Recharge Successful!")
                print("Thank you for recharging!")

                success_menu()

            elif choice == 2:

                amount = int(input("Enter recharge amount: "))

                recharge = {
                    "method": "UPI",
                    "amount": amount
                }

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
            print("\n--- DATA PLANS ---")
            print("1. 1GB/day")
            print("2. 2GB/day")
            print("3. Unlimited")
            print("4. View Selected Plans")
            print("5. Back")

            choice = int(input("Enter choice: "))

            plans = {
                1: "1GB/day Plan",
                2: "2GB/day Plan",
                3: "Unlimited Plan"
            }

            if choice in plans:

                plan = {
                    "plan": plans[choice]
                }

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
            print("\n--- POSTPAID ---")
            print("1. Current Bill")
            print("2. Bill Payment")
            print("3. Plan Upgrade")
            print("4. Back")

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
            print("\n--- BILL PAYMENT ---")
            print("1. NetBanking")
            print("2. Wallet")
            print("3. View Payment History")
            print("4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                payment = {
                    "method": "NetBanking"
                }

                ivr_data["bill_payments"].append(payment)

                save_data()

                print("Paid via NetBanking")
                print("Payment Successful!")

                success_menu()

            elif choice == 2:

                payment = {
                    "method": "Wallet"
                }

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
            print("\n--- PLAN UPGRADE ---")
            print("1. Silver → Gold")
            print("2. Gold → Platinum")
            print("3. View Upgrade History")
            print("4. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                upgrade = {
                    "upgrade": "Silver to Gold"
                }

                ivr_data["plan_upgrades"].append(upgrade)

                save_data()

                print("Silver upgraded to Gold")
                print("Thank you for upgrading!")

                success_menu()

            elif choice == 2:

                upgrade = {
                    "upgrade": "Gold to Platinum"
                }

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
            print("\n--- INTERNET SERVICES ---")
            print("1. Broadband")
            print("2. Fiber")
            print("3. Back")

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
            print("\n--- TV & OTT SERVICES ---")
            print("1. Channel Packs")
            print("2. Recharge Plans")
            print("3. Complaint")
            print("4. View Complaints")
            print("5. Back")

            choice = int(input("Enter choice: "))

            if choice == 1:

                print("Sports / Movies / All-in-One Pack")

                success_menu()

            elif choice == 2:

                print("1 Month / 6 Months / 12 Months Plans")

                success_menu()

            elif choice == 3:

                issue = input("Enter complaint: ")

                complaint = {
                    "issue": issue
                }
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