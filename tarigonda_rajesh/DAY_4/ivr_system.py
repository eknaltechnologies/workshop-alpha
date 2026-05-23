user = {
    'balance': 800,
    'recharge_history': [],
    'current_bill': 1200,
    'broadband_usage': 45,
    'broadband_plan': 'Monthly',
    'fiber_connection': False,
    'tv_status': 'Active'
}

# Main Menu
def main_menu():
    while True:
        print("\n1. Mobile Services" \
        "\n2. Internet Services" \
        "\n3. TV & OTT Services" \
        "\n4. Talk to Customer Support" \
        "\n5. Exit")

        user_choice = int(input("Choose a service(1-5): "))
        if user_choice == 1:
            mobile_services()
        elif user_choice == 2:
            internet_services()
        elif user_choice == 3:
            tv_ott_services()
        elif user_choice == 4:
            print("Connecting to Customer Support")
        elif user_choice == 5:
            print("Thank You")
            break
        else:
            print("Choose correct service")

# Mobile Services
def mobile_services():
    while True:
        print("\n1. Prepaid" \
        "\n2. Postpaid" \
        "\n3. Back")

        mobile_ser = int(input("Choose mobile service(1-3): "))
        if mobile_ser == 1:
            prepaid_services()
        elif mobile_ser == 2:
            postpaid_services()
        elif mobile_ser == 3:
            break
        else:
            print("Choose correct service")

# Prepaid
def prepaid_services():
    while True:
        print("\n1. Balance Inquiry" \
        "\n2. Recharge" \
        "\n3. Recharge History" \
        "\n4. Data Plans" \
        "\n5. Back")

        prepaid_ser = int(input("Choose prepaid service(1-5): "))
        if prepaid_ser == 1:
            print(f"Available Balance : {user['balance']}")
        elif prepaid_ser == 2:
            recharge_menu()
        elif prepaid_ser == 3:
            recharge_history()
        elif prepaid_ser == 4:
            data_plans()
        elif prepaid_ser == 5:
            break
        else:
            print("Choose correct service")

# Recharge
def recharge_menu():
    while True:
        print("\n1. Using Credit Card" \
        "\n2. Using UPI" \
        "\n3. Back")
        recharge_ser = int(input("Choose recharge option(1-3): "))

        if recharge_ser == 1:
            amount = int(input("Enter recharge amount: "))
            if user['balance'] >= amount:
                user['balance'] -= amount
                user['recharge_history'].append(
                    f"Recharge of {amount} done using Credit Card"
                )
                print("Recharge Successful")
            else:
                print("Insufficient Balance")
        elif recharge_ser == 2:
            amount = int(input("Enter recharge amount: "))
            user['recharge_history'].append(
                f"Recharge of {amount} done using UPI"
            )
            print("Recharge Successful")
        elif recharge_ser == 3:
            break
        else:
            print("Choose correct option")

# Recharge History
def recharge_history():
    print("\nRecharge History")
    if len(user['recharge_history']) == 0:
        print("No Recharge History Found")
    else:
        for history in user['recharge_history']:
            print(history)

# Data Plans
def data_plans():
    while True:
        print("\n1. 1GB/day" \
        "\n2. 2GB/day" \
        "\n3. Unlimited" \
        "\n4. Back")

        plan = int(input("Choose data plan(1-4): "))
        if plan == 1:
            print("1GB/day Plan Activated")
        elif plan == 2:
            print("2GB/day Plan Activated")
        elif plan == 3:
            print("Unlimited Plan Activated")
        elif plan == 4:
            break
        else:
            print("Choose correct plan")

# Postpaid
def postpaid_services():
    while True:
        print("\n1. Current Bill" \
        "\n2. Bill Payment" \
        "\n3. Plan Upgrade" \
        "\n4. Back")

        postpaid_ser = int(input("Choose postpaid service(1-4): "))
        if postpaid_ser == 1:
            print(f"Current Bill : {user['current_bill']}")
        elif postpaid_ser == 2:
            bill_payment()
        elif postpaid_ser == 3:
            plan_upgrade()
        elif postpaid_ser == 4:
            break
        else:
            print("Choose correct option")

# Bill Payment
def bill_payment():
    while True:
        print("\n1. Pay via NetBanking" \
        "\n2. Pay via Wallet" \
        "\n3. Back")

        payment = int(input("Choose payment method(1-3): "))
        if payment == 1:
            user['current_bill'] = 0
            print("Bill Paid Successfully using NetBanking")
        elif payment == 2:
            user['current_bill'] = 0
            print("Bill Paid Successfully using Wallet")
        elif payment == 3:
            break
        else:
            print("Choose correct option")

# Plan Upgrade
def plan_upgrade():
    while True:
        print("\n1. Silver to Gold" \
        "\n2. Gold to Platinum" \
        "\n3. Back")

        upgrade = int(input("Choose upgrade option(1-3): "))
        if upgrade == 1:
            print("Plan Upgraded from Silver to Gold")
        elif upgrade == 2:
            print("Plan Upgraded from Gold to Platinum")
        elif upgrade == 3:
            break
        else:
            print("Choose correct option")

# Internet Services
def internet_services():
    while True:
        print("\n1. Broadband" \
        "\n2. Fiber" \
        "\n3. Back")

        internet_serv = int(input("Choose internet service(1-3): "))
        if internet_serv == 1:
            broadband_services()
        elif internet_serv == 2:
            fiber_services()
        elif internet_serv == 3:
            break
        else:
            print("Choose correct service")

# Broadband
def broadband_services():
    while True:
        print("\n1. Usage Details" \
        "\n2. Renew Plan" \
        "\n3. Change Router" \
        "\n4. Back")

        broadband_ser = int(input("Choose broadband service(1-4): "))
        if broadband_ser == 1:
            print(f"Broadband Usage : {user['broadband_usage']} GB")
        elif broadband_ser == 2:
            renew_plan()
        elif broadband_ser == 3:
            change_router()
        elif broadband_ser == 4:
            break
        else:
            print("Choose correct service")

# Renew Plan
def renew_plan():
    while True:
        print("\n1. Monthly Plan" \
        "\n2. Quarterly Plan" \
        "\n3. Yearly Plan" \
        "\n4. Back")

        renew = int(input("Choose renew option(1-4): "))
        if renew == 1:
            user['broadband_plan'] = "Monthly"
            print("Monthly Plan Activated")
        elif renew == 2:
            user['broadband_plan'] = "Quarterly"
            print("Quarterly Plan Activated")
        elif renew == 3:
            user['broadband_plan'] = "Yearly"
            print("Yearly Plan Activated")
        elif renew == 4:
            break
        else:
            print("Choose correct option")

# Change Router
def change_router():
    while True:
        print("\n1. Request Technician Visit" \
        "\n2. Self Installation Guide" \
        "\n3. Back")

        router = int(input("Choose option(1-3): "))
        if router == 1:
            print("Technician Visit Requested")
        elif router == 2:
            print("Self Installation Guide Sent")
        elif router == 3:
            break
        else:
            print("Choose correct option")

# Fiber
def fiber_services():
    while True:
        print("\n1. New Connection" \
        "\n2. Status Check" \
        "\n3. Back")

        fiber_ser = int(input("Choose fiber service(1-3): "))
        if fiber_ser == 1:
            new_connection()
        elif fiber_ser == 2:
            print(f"Fiber Connection Status : {user['fiber_connection']}")
        elif fiber_ser == 3:
            break
        else:
            print("Choose correct option")

# New Connection
def new_connection():
    while True:
        print("\n1. Residential" \
        "\n2. Business" \
        "\n3. Back")
        connection = int(input("Choose connection type(1-3): "))

        if connection == 1:
            user['fiber_connection'] = True
            print("Residential Connection Requested")
        elif connection == 2:
            user['fiber_connection'] = True
            print("Business Connection Requested")
        elif connection == 3:
            break
        else:
            print("Choose correct option")

# TV & OTT Services
def tv_ott_services():
    while True:
        print("\n1. Channel Pack" \
        "\n2. Recharge" \
        "\n3. Complaint" \
        "\n4. Back")

        tv_serv = int(input("Choose TV service(1-4): "))
        if tv_serv == 1:
            channel_pack()
        elif tv_serv == 2:
            tv_recharge()
        elif tv_serv == 3:
            complaint_services()
        elif tv_serv == 4:
            break
        else:
            print("Choose correct service")

# Channel Pack
def channel_pack():
    while True:
        print("\n1. Sports Pack" \
        "\n2. Movies Pack" \
        "\n3. All-in-One Pack" \
        "\n4. Back")

        pack = int(input("Choose pack(1-4): "))
        if pack == 1:
            print("Sports Pack Activated")
        elif pack == 2:
            print("Movies Pack Activated")
        elif pack == 3:
            print("All-in-One Pack Activated")
        elif pack == 4:
            break
        else:
            print("Choose correct pack")

# TV Recharge
def tv_recharge():
    while True:
        print("\n1. 1 Month" \
        "\n2. 6 Months" \
        "\n3. 12 Months" \
        "\n4. Back")

        recharge = int(input("Choose recharge option(1-4): "))
        if recharge == 1:
            print("1 Month Recharge Successful")
        elif recharge == 2:
            print("6 Months Recharge Successful")
        elif recharge == 3:
            print("12 Months Recharge Successful")
        elif recharge == 4:
            break
        else:
            print("Choose correct option")

# Complaint
def complaint_services():
    while True:
        print("\n1. No Signal" \
        "\n2. Overcharged" \
        "\n3. Back")

        complaint = int(input("Choose complaint option(1-3): "))
        if complaint == 1:
            print("Complaint Registered for No Signal")
        elif complaint == 2:
            print("Complaint Registered for Overcharged")
        elif complaint == 3:
            break
        else:
            print("Choose correct option")
main_menu()