def display(title, menu):
    print("\n" + "*" * 10, title, "*" * 10)

    for num, item in menu.items():
        print(f"{num}. {item}")


def prepaid_services():
    while True:
        display("PREPAID SERVICES", {
            "1": "Check Balance",
            "2": "Recharge Account",
            "3": "View Plans",
            "4": "Return"
        })

        option = input("Enter choice: ")

        if option == "1":
            print("Current Balance : ₹450")

        elif option == "2":
            recharge_services()

        elif option == "3":
            plans()

        elif option == "4":
            return

        else:
            print("Please enter valid option")


def recharge_services():
    while True:
        display("RECHARGE OPTIONS", {
            "1": "Debit Card",
            "2": "UPI Payment",
            "3": "Recharge Records",
            "4": "Back"
        })

        option = input("Enter choice: ")

        if option == "1":
            print("Recharge successful using Debit Card")

        elif option == "2":
            print("Recharge successful using UPI")

        elif option == "3":
            print("Showing previous recharges")

        elif option == "4":
            return

        else:
            print("Please enter valid option")


def plans():
    while True:
        display("AVAILABLE PLANS", {
            "1": "Daily 1GB",
            "2": "Daily 2GB",
            "3": "Unlimited Data",
            "4": "Back"
        })

        option = input("Enter choice: ")

        if option in ["1", "2", "3"]:
            print("Selected plan activated")

        elif option == "4":
            return

        else:
            print("Please enter valid option")


def postpaid_services():
    while True:
        display("POSTPAID SERVICES", {
            "1": "Check Bill",
            "2": "Pay Bill",
            "3": "Upgrade Subscription",
            "4": "Return"
        })

        option = input("Enter choice: ")

        if option == "1":
            print("Bill Amount : ₹799")

        elif option == "2":
            bill()

        elif option == "3":
            upgrade()

        elif option == "4":
            return

        else:
            print("Please enter valid option")


def bill():
    while True:
        display("PAYMENT OPTIONS", {
            "1": "Net Banking",
            "2": "Digital Wallet",
            "3": "Back"
        })

        option = input("Enter choice: ")

        if option == "1":
            print("Bill paid successfully")

        elif option == "2":
            print("Wallet payment completed")

        elif option == "3":
            return

        else:
            print("Please enter valid option")


def upgrade():
    while True:
        display("UPGRADE OPTIONS", {
            "1": "Basic → Premium",
            "2": "Premium → Ultimate",
            "3": "Back"
        })

        option = input("Enter choice: ")

        if option == "1":
            print("Upgraded to Premium")

        elif option == "2":
            print("Upgraded to Ultimate")

        elif option == "3":
            return

        else:
            print("Please enter valid option")


def mobile():
    while True:
        display("MOBILE MENU", {
            "1": "Prepaid",
            "2": "Postpaid",
            "3": "Back"
        })

        option = input("Enter choice: ")

        if option == "1":
            prepaid_services()

        elif option == "2":
            postpaid_services()

        elif option == "3":
            return

        else:
            print("Please enter valid option")


def internet():
    print("Current Usage Details")
    print("Renew Existing Plan")
    print("Router Configuration")


def ott():
    print("Entertainment Pack")
    print("Monthly Recharge")
    print("Complaint Section")


def help_center():
    print("Connecting...")
    print("Customer executive will assist you shortly")


def start():
    while True:
        display("IVR SYSTEM", {
            "1": "Mobile Services",
            "2": "Internet Services",
            "3": "OTT Services",
            "4": "Customer Support",
            "5": "Exit"
        })

        option = input("Enter choice: ")

        if option == "1":
            mobile()

        elif option == "2":
            internet()

        elif option == "3":
            ott()

        elif option == "4":
            help_center()

        elif option == "5":
            print("Thank You for Visiting")
            break

        else:
            print("Please enter valid option")


start()