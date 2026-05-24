import json

try:
    with open("ivr_data.json", "r") as f:
        ivr_data = json.load(f)
except (FileNotFoundError, KeyboardInterrupt):
    ivr_data = {
        "balance": 0.0,
        "recharges": [],
        "data_plans": [],
        "bill_payments": [],
        "plan_upgrades": [],
        "complaints": [],
    }


def save_data():
    with open("ivr_data.json", "w") as file:
        json.dump(ivr_data, file, indent=2)


def main_menu():
    while True:
        print("\nMain Menu:\n1. Mobile Services\n2. Internet Services\n3. TV & OTT Services\n4. Talk to Customer Care\n5. Exit")
        choice = int(input("Choice: ").strip())

        if choice == "1":
            result = mobile_services()
            if result == "main":
                continue
        elif choice == "2":
            internet_services()
        elif choice == "3":
            tv_ott_services()
        elif choice == "4":
            print("Connecting to customer care...")
        elif choice == "5":
            print("Thank you for using our services. Goodbye!")
            break
        else:
            print("Invalid choice.")
    save_data()


def mobile_services():
    while True:
        print("\nMobile Services:\n1. Prepaid\n2. Postpaid\n3. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            result = prepaid_services()
            if result == "main":
                return "main"
        elif choice == "2":
            result = postpaid_services()
            if result == "main":
                return "main"
        elif choice == "3":
            return
        else:
            print("Invalid choice.")


def prepaid_services():
    while True:
        print("\nPrepaid:\n1. Balance Inquiry\n2. Recharge\n3. Data Plans\n4. Back\n5. Back for Main Menu")
        choice = input("Choice: ").strip()

        if choice == "1":
            print(f"Your balance is ₹{ivr_data['balance']:.2f}")
        elif choice == "2":
            result = prepaid_recharge()
            if result == "main":
                return "main"
        elif choice == "3":
            result = prepaid_data_plans()
            if result == "main":
                return "main"
        elif choice == "4":
            return
        elif choice == "5":
            return "main"
        else:
            print("Invalid choice.")


def prepaid_recharge():
    while True:
        print("\nRecharge:\n1. Credit Card\n2. UPI\n3. Recharge History\n4. Back for Prepaid Menu\n5. Back for Main Menu")
        choice = input("Choice: ").strip()

        if choice in ["1", "2"]:
            method = "Credit Card" if choice == "1" else "UPI"
            amount = input(f"Enter recharge amount for {method}: ").strip()
            try:
                amount_value = float(amount)
                if amount_value > 0:
                    ivr_data["balance"] += amount_value
                    ivr_data["recharges"].append({"method": method, "amount": amount_value})
                    save_data()
                    print(f"Recharge successful via {method}. New balance is ₹{ivr_data['balance']:.2f}")
                else:
                    print("Please enter an amount greater than 0.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "3":
            if ivr_data["recharges"]:
                print("\n--- Recharge History ---")
                for i, r in enumerate(ivr_data["recharges"], start=1):
                    print(f"{i}. {r['method']} : ₹{r['amount']:.2f}")
            else:
                print("No recharge history available.")
        elif choice == "4":
            return
        elif choice == "5":
            return "main"
        else:
            print("Invalid choice.")


def prepaid_data_plans():
    while True:
        print("\nData Plans:\n1. 1.1GB/day\n2. 2GB/day\n3. Unlimited\n4. View Selected Plans\n5. Back for Prepaid Menu\n6. Back for Main Menu")
        choice = input("Choice: ").strip()

        if choice in ["1", "2", "3"]:
            plan = "1.1GB/day" if choice == "1" else "2GB/day" if choice == "2" else "Unlimited"
            ivr_data["data_plans"].append(plan)
            save_data()
            print(f"Selected {plan} plan.")
        elif choice == "4":
            if ivr_data["data_plans"]:
                print("\n--- Selected Plans ---")
                for p in ivr_data["data_plans"]:
                    print(p)
            else:
                print("No plans selected yet.")
        elif choice == "5":
            return
        elif choice == "6":
            return "main"
        else:
            print("Invalid choice.")


def postpaid_services():
    while True:
        print("\nPostpaid:\n1. Current Bill\n2. Bill Payment\n3. Plan Upgrade\n4. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            print("Your current bill is ₹999.00")
        elif choice == "2":
            result = postpaid_bill_payment()
            if result == "main":
                return "main"
        elif choice == "3":
            result = postpaid_plan_upgrade()
            if result == "main":
                return "main"
        elif choice == "4":
            return
        else:
            print("Invalid choice.")


def postpaid_bill_payment():
    while True:
        print("\nBill Payment:\n1. NetBanking\n2. Wallet\n3. View Payment History\n4. Back for Postpaid Menu\n5. Back for Main Menu")
        choice = input("Choice: ").strip()

        if choice in ["1", "2"]:
            method = "NetBanking" if choice == "1" else "Wallet"
            ivr_data["bill_payments"].append({"method": method})
            save_data()
            print(f"Payment successful via {method}.")
        elif choice == "3":
            if ivr_data["bill_payments"]:
                print("\n--- Payment History ---")
                for p in ivr_data["bill_payments"]:
                    print(p["method"])
            else:
                print("No payment history yet.")
        elif choice == "4":
            return
        elif choice == "5":
            return "main"
        else:
            print("Invalid choice.")


def postpaid_plan_upgrade():
    while True:
        print("\nPlan Upgrade:\n1. Silver to Gold\n2. Gold to Platinum\n3. View Upgrade History\n4. Back for Postpaid Menu\n5. Back for Main Menu")
        choice = input("Choice: ").strip()

        if choice == "1":
            ivr_data["plan_upgrades"].append("Silver to Gold")
            save_data()
            print("Your plan has been upgraded from Silver to Gold.")
        elif choice == "2":
            ivr_data["plan_upgrades"].append("Gold to Platinum")
            save_data()
            print("Your plan has been upgraded from Gold to Platinum.")
        elif choice == "3":
            if ivr_data["plan_upgrades"]:
                print("\n--- Upgrade History ---")
                for u in ivr_data["plan_upgrades"]:
                    print(u)
            else:
                print("No upgrades yet.")
        elif choice == "4":
            return
        elif choice == "5":
            return "main"
        else:
            print("Invalid choice.")


def internet_services():
    while True:
        print("\nInternet Services:\n1. Broadband\n2. Fiber\n3. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            print("Broadband Selected")
            save_data()
        elif choice == "2":
            print("Fiber Selected")
            save_data()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")


def tv_ott_services():
    while True:
        print("\nTV & OTT Services:\n1. Channel Packs\n2. Recharge Plans\n3. Complaint\n4. View Complaints\n5. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            print("Sports / Movies / All-in-One Pack")
        elif choice == "2":
            print("1 Month / 6 Months / 12 Months Plans")
        elif choice == "3":
            issue = input("Enter complaint: ").strip()
            ivr_data["complaints"].append({"issue": issue})
            save_data()
            print("Complaint Registered Successfully")
        elif choice == "4":
            if ivr_data["complaints"]:
                print("\n--- Complaint History ---")
                for c in ivr_data["complaints"]:
                    print(c["issue"])
            else:
                print("No complaints registered yet.")
        elif choice == "5":
            return
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
