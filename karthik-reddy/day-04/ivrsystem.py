import json

# -------- CONSTANTS --------

ENTER_CHOICE = "Enter choice: "
INVALID_CHOICE = "Invalid choice"
INVALID_INPUT = "Invalid Input"

# -------- LOAD JSON DATA --------

try:
    with open("ivr_data.json", "r") as f:
        ivr_data = json.load(f)

except FileNotFoundError:

    ivr_data = {"recharges": [], "data_plans": [], "bill_payments": [], "plan_upgrades": [], "complaints": []}


# -------- SAVE DATA --------


def save_data():

    with open("ivr_data.json", "w") as f:
        json.dump(ivr_data, f, indent=4)


# -------- SUCCESS MENU --------


def success_menu():

    while True:

        print("\n1. Continue")
        print("2. Exit")

        try:

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                return

            elif choice == 2:
                print("Thank You for using our service!")
                exit()

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print("Enter numbers only!")


# -------- MAIN MENU --------


def main_menu():

    while True:

        try:

            print(
                "\n===== MAIN MENU ====="
                "\n1. Mobile Services"
                "\n2. Internet Services"
                "\n3. TV & OTT Services"
                "\n4. Talk to Customer Support"
                "\n5. Exit"
            )

            choice = int(input(ENTER_CHOICE))

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
                print(INVALID_CHOICE)

        except ValueError:
            print("Please enter numbers only!")


# -------- MOBILE SERVICES --------


def mobile_services():

    while True:

        try:

            print("\n--- MOBILE SERVICES ---" "\n1. Prepaid" "\n2. Postpaid" "\n3. Back")

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                prepaid()

            elif choice == 2:
                postpaid()

            elif choice == 3:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print("Enter valid number!")


# -------- PREPAID --------


def prepaid():

    while True:

        try:

            print("\n--- PREPAID ---" "\n1. Balance Inquiry" "\n2. Recharge" "\n3. Data Plans" "\n4. Back")

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                print("Balance = ₹250")

            elif choice == 2:
                recharge_menu()

            elif choice == 3:
                data_plans()

            elif choice == 4:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print("Numbers only!")


# -------- RECHARGE FUNCTIONS --------


def recharge_success():

    print("Recharge Successful!\nThank you for recharging!")


def process_recharge(method):

    amount = int(input("Enter recharge amount: "))

    recharge = {"method": method, "amount": amount}

    ivr_data["recharges"].append(recharge)

    save_data()

    recharge_success()

    success_menu()


def show_recharge_history():

    if not ivr_data["recharges"]:
        print("No recharge history found")

    else:

        print("\n--- RECHARGE HISTORY ---")

        for recharge in ivr_data["recharges"]:

            print(f"Method : {recharge['method']}")
            print(f"Amount : ₹{recharge['amount']}")
            print("----------------------")


# -------- RECHARGE MENU --------


def recharge_menu():

    while True:

        try:

            print("\n--- RECHARGE ---" "\n1. Credit Card" "\n2. UPI" "\n3. Recharge History" "\n4. Back")

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                process_recharge("Credit Card")

            elif choice == 2:
                process_recharge("UPI")

            elif choice == 3:
                show_recharge_history()

            elif choice == 4:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print(INVALID_INPUT)


# -------- DATA PLANS --------


def data_plans():

    plans = {1: "1GB/day Plan", 2: "2GB/day Plan", 3: "Unlimited Plan"}

    while True:

        try:

            print("\n--- DATA PLANS ---" "\n1. 1GB/day" "\n2. 2GB/day" "\n3. Unlimited" "\n4. View Selected Plans" "\n5. Back")

            choice = int(input(ENTER_CHOICE))

            if choice in plans:

                plan = {"plan": plans[choice]}

                ivr_data["data_plans"].append(plan)

                save_data()

                print(f"{plans[choice]} Selected\n" "Thank you for choosing our service!")

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
                print(INVALID_CHOICE)

        except ValueError:
            print(INVALID_INPUT)


# -------- POSTPAID --------


def postpaid():

    while True:

        try:

            print("\n--- POSTPAID ---" "\n1. Current Bill" "\n2. Bill Payment" "\n3. Plan Upgrade" "\n4. Back")

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                print("Current Bill = ₹999")

            elif choice == 2:
                bill_payment()

            elif choice == 3:
                plan_upgrade()

            elif choice == 4:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print("Enter number only")


# -------- BILL PAYMENT --------


def process_payment(method):

    payment = {"method": method}

    ivr_data["bill_payments"].append(payment)

    save_data()

    print(f"Paid via {method}\nPayment Successful!")

    success_menu()


def bill_payment():

    while True:

        try:

            print("\n--- BILL PAYMENT ---" "\n1. NetBanking" "\n2. Wallet" "\n3. View Payment History" "\n4. Back")

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                process_payment("NetBanking")

            elif choice == 2:
                process_payment("Wallet")

            elif choice == 3:

                print("\n--- PAYMENT HISTORY ---")

                for payment in ivr_data["bill_payments"]:
                    print(payment["method"])

            elif choice == 4:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print(INVALID_INPUT)


# -------- PLAN UPGRADE --------


def process_upgrade(plan_name, message):

    upgrade = {"upgrade": plan_name}

    ivr_data["plan_upgrades"].append(upgrade)

    save_data()

    print(message)

    success_menu()


def plan_upgrade():

    while True:

        try:

            print(
                "\n--- PLAN UPGRADE ---"
                "\n1. Silver → Gold (2GB/day throughout 1 year)"
                "\n2. Gold → Platinum (Unlimited 5G network throughout the year)"
                "\n3. View Upgrade History"
                "\n4. Back"
            )

            choice = int(input(ENTER_CHOICE))

            if choice == 1:

                process_upgrade("Silver to Gold", "Silver upgraded to Gold\nThank you for upgrading!")

            elif choice == 2:

                process_upgrade("Gold to Platinum", "Gold upgraded to Platinum\nThank you for upgrading!")

            elif choice == 3:

                print("\n--- UPGRADE HISTORY ---")

                for upgrade in ivr_data["plan_upgrades"]:
                    print(upgrade["upgrade"])

            elif choice == 4:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print("Wrong Input")


# -------- INTERNET SERVICES --------


def internet_services():

    while True:

        try:

            print("\n--- INTERNET SERVICES ---" "\n1. Broadband" "\n2. Fiber" "\n3. Back")

            choice = int(input(ENTER_CHOICE))

            if choice == 1:

                print("Broadband Selected")

                success_menu()

            elif choice == 2:

                print("Fiber Selected")

                success_menu()

            elif choice == 3:
                return

            else:
                print(INVALID_CHOICE)

        except ValueError:
            print("Numbers only")


# -------- TV & OTT SERVICES --------


def tv_ott_services():

    while True:

        try:

            print("\n--- TV & OTT SERVICES ---" "\n1. Channel Packs" "\n2. Recharge Plans" "\n3. Complaint" "\n4. View Complaints" "\n5. Back")

            choice = int(input(ENTER_CHOICE))

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
                print(INVALID_CHOICE)

        except ValueError:
            print(INVALID_INPUT)


# -------- START PROGRAM --------

try:
    main_menu()

except KeyboardInterrupt:
    print("\nProgram stopped by user")
