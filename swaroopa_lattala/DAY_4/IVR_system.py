import sys

print("=====================================\nWelcome to the VBC IVR System\n=====================================")


def main_menu():
    print("------ MAIN MENU ------")
    print("1. Mobile Services \n2. Internet Services \n3. TV & OTT Services \n4. Talk to Customer Support \n5. Exit")
    choice = input("\nPlease select an option (1-5):")

    if choice == "1":
        mobile_services()
    elif choice == "2":
        internet_services()
    elif choice == "3":
        tv_ott_services()
    elif choice == "4":
        print("\n {Connecting....} Connecting your call to customer support.\n Thank you for calling!")
    elif choice == "5":
        print("\n Thank you for using IVR systems.")
    else:
        print("\n Invalid Selection !. Please try again.")
        main_menu()


# Mobile services
def mobile_services():
    print("\n---MOBILE SERVICES---")
    print("1. Prepaid \n2. Postpaid \n3. Back")
    choice = input("\nPlease Select an option (1-3):")

    if choice == "1":
        prepaid_menu()
    elif choice == "2":
        postpaid_menu()
    elif choice == "3":
        main_menu()  # Back to main menu
    else:
        print("\n Invalid selection !. Please try again.")
        mobile_services()


# sub-menu 1-prepaid
def prepaid_menu():
    print("\n--- PREPAID SERVICES ---")
    print("1. Balance Inquiry \n2. Recharge \n3. Data plans \n4. Back \n5. Back for Main Menu")
    choice = input("\n Please select an option (1-5):")

    if choice == "1":
        print("\n[INFO] Your prepaid account balance is ₹249.50.")
        prepaid_menu()
    elif choice == "2":
        recharge_menu()
    elif choice == "3":
        data_plans_menu()
    elif choice == "4":
        mobile_services()  # Back to Mobile Services
    elif choice == "5":
        main_menu()  # Back to Main Menu
    else:
        print("\n[!] Invalid selection. Please try again.")
        prepaid_menu()

    # sub-menu 2.Recharge


def recharge_menu():
    print("\n--- RECHARGE OPTIONS ---")
    print("1. Using Credit Card \n2. Using UPI \n3. Recharge History \n4. Back for Prepaid Menu \n. Back for Main Menu")
    choice = input("\nPlease select an option (1-5): ")

    if choice == "1":
        print("\n[SUCCESS] Recharge completed using Credit Card.")
        recharge_menu()
    elif choice == "2":
        print("\n[SUCCESS] Recharge completed using UPI.")
        recharge_menu()
    elif choice == "3":
        print("\n[INFO] Displaying Recharge History details...")
        recharge_menu()
    elif choice == "4":
        prepaid_menu()  # Back to prepaid menu
    elif choice == "5":
        main_menu()  # Back to main menu
    else:
        print("\n Invalid selection!. Please try again.")
        recharge_menu()


# sub-menu 3.Data plan
def data_plans_menu():
    print("\n--- DATA PLANS ---")
    print("1. 1GB/day \n2. 2GB/day \n3. Unlimited \n4. Back for Prepaid Menu \n5. Back for Main Menu")
    choice = input("\nPlease Select an option (1-5):")

    if choice in ["1", "2", "3"]:
        print("\n[SUCCESS] Requested data pack activated successfully.")
        data_plans_menu()
    elif choice == "4":
        prepaid_menu()  # Back to prepaid menu
    elif choice == "5":
        main_menu()  # Back to main menu
    else:
        print("\n Invalid selection !. Please try again.")
        data_plans_menu()


# 2.Postpaid
def postpaid_menu():
    print("\n--- POSTPAID SERVICES ---")
    print("1. Current Bill \n2. Bill Payment \n3. Plan Upgrade \n4. Back \n5. Back for Main Menu ")
    choice = input("\nPlease select an option (1-5): ")

    if choice == "1":
        print("\n[INFO] Your current outstanding postpaid bill is ₹749.00.")
        postpaid_menu()
    elif choice == "2":
        bill_payment_menu()
    elif choice == "3":
        plan_upgrade_menu()
    elif choice == "4":
        mobile_services()
    elif choice == "5":
        main_menu()  # Back to main menu
    else:
        print("\n Invalid selection !. Please try again.")
        postpaid_menu()


# POstpaid sub-menu 2-bill payment
def bill_payment_menu():
    print("\n--- BILL PAYMENT ---")
    print("1. Pay via NetBanking \n2. Pay via Wallet \n3. Back for Postpaid Menu \n4. Back for Main Menu ")
    choice = input("\nPlease select an option (1-4): ")

    if choice == "1":
        print("\n[SUCCESS] Bill paid via NetBanking.")
        bill_payment_menu()
    elif choice == "2":
        print("\n[SUCCESS] Bill paid via Wallet.")
        bill_payment_menu()
    elif choice == "3":
        postpaid_menu()
    elif choice == "4":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        bill_payment_menu()


# submenu - plan upgrade
def plan_upgrade_menu():
    print("\n--- PLAN UPGRADE ---")
    print("1. Silver to Gold \n2. Gold to Platinum \n3. Back for Postpaid Menu \n4. Back for Main Menu")
    choice = input("\nPlease select an option (1-4): ")

    if choice == "1":
        print("\n[SUCCESS] Plan Upgrade registered: Silver to Gold.")
        plan_upgrade_menu()
    elif choice == "2":
        print("\n[SUCCESS] Plan Upgrade registered: Gold to Platinum.")
        plan_upgrade_menu()
    elif choice == "3":
        postpaid_menu()
    elif choice == "4":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        plan_upgrade_menu()


# 3-INTERNET SERVICES
def internet_services():
    print("\n--- INTERNET SERVICES ---")
    print("1. Broadband \n2. Fiber \n3. Back")
    choice = input("\nPlease select an option (1-3): ")

    if choice == "1":
        broadband_menu()
    elif choice == "2":
        fiber_menu()
    elif choice == "3":
        main_menu()
    else:
        print("\nInvalid selection !. Please try again.")
        internet_services()


# submenu Broadband
def broadband_menu():
    print("\n--- BROADBAND SERVICES ---")
    print("1. Usage Details \n2. Renew Plan \n3. Change Router \n4. Back \n5. Back for Main Menu")
    choice = input("\nPlease select an option (1-5): ")

    if choice == "1":
        print("\n[INFO] You have consumed 145 GB of your high-speed quota.")
        broadband_menu()
    elif choice == "2":
        renew_plan_menu()
    elif choice == "3":
        change_router()
    elif choice == "4":
        internet_services()
    elif choice == "5":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        broadband_menu()


# submenu REnew
def renew_plan_menu():
    print("\n--- RENEW BROADBAND PLAN ---")
    print("1. Monthly Plan \n2. Quarterly Plan \n3. Yearly Plan \n4. Back for Broadband Menu \n5. Back for Main Menu ")
    choice = input("\nPlease select an option (1-5): ")

    if choice in ["1", "2", "3"]:
        print("\n[SUCCESS] Renewal request processed successfully!")
        renew_plan_menu()
    elif choice == "4":
        broadband_menu()
    elif choice == "5":
        main_menu()
    else:
        print("\nInvalid selection !. Please try again.")
        renew_plan_menu()


# submenu Change router
def change_router():
    print("\n--- CHANGE ROUTER ---")
    print(
        "1. Request Technician Visit \n2. Self Installation Guide \n3. Back for Broadband Menu \n4. Back for Main Menu ")
    choice = input("\nPlease select an option (1-4): ")

    if choice == "1":
        print("\n[SUCCESS] A technician visit has been scheduled.")
        change_router()
    elif choice == "2":
        print("\n[GUIDE] Power off device. Swap WAN cable to the new router...")
        change_router()
    elif choice == "3":
        broadband_menu()
    elif choice == "4":
        main_menu()
    else:
        print("\nInvalid selection !. Please try again.")
        change_router()


# FIBER
def fiber_menu():
    print("\n--- FIBER SERVICES ---")
    print("1. New Connection \n2. Status Check \n3. Back \n4. Back for Main Menu ")
    choice = input("\nPlease select an option (1-4): ")

    if choice == "1":
        fiber_new_conn()
    elif choice == "2":
        print("\n[STATUS] Your fiber installation request is currently in progress.")
        fiber_menu()
    elif choice == "3":
        internet_services()
    elif choice == "4":
        main_menu()
    else:
        print("\n[!] Invalid selection. Please try again.")
        fiber_menu()


def fiber_new_conn():
    print("\n--- NEW FIBER CONNECTION ---")
    print("1. Residential \n2. Business \n3. Back for Fiber Menu \n4. Back for Main Menu")
    choice = input("\nPlease select an option (1-4): ")

    if choice == "1":
        print("\n[SUCCESS] Residential fiber tracking ticket logged.")
        fiber_new_conn()
    elif choice == "2":
        print("\n[SUCCESS] Corporate business fiber inquiry logged.")
        fiber_new_conn()
    elif choice == "3":
        fiber_menu()
    elif choice == "4":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        fiber_new_conn()


def tv_ott_services():
    print("\n--- TV & OTT SERVICES ---")
    print("1. Channel Packs \n2. Recharge \n3. Complaint \n4. Back")
    choice = input("\nPlease select an option (1-4): ")

    if choice == "1":
        tv_channels()
    elif choice == "2":
        tv_recharge()
    elif choice == "3":
        tv_complaint()
    elif choice == "4":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        tv_ott_services()


def tv_channels():
    print("\n--- CHANNEL PACKS ---")
    print("1. Sports Pack \n2. Movies Pack \n3. All-in-One Pack \n4. Back for Main Menu")
    choice = input("\nPlease select an option (1-4): ")

    if choice in ["1", "2", "3"]:
        print("\n[SUCCESS] Requested Channel Pack activated.")
        tv_channels()
    elif choice == "4":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        tv_channels()


def tv_recharge():
    print("\n--- TV RECHARGE ---")
    print("1. 1 Month \n2. 6 Months \n3. 12 Months \n4. Back for Main Menu")
    choice = input("\nPlease select an option (1-4): ")

    if choice in ["1", "2", "3"]:
        print("\n[SUCCESS] :TV subscription renewal payment received.")
        tv_recharge()
    elif choice == "4":
        main_menu()
    else:
        print("\n Invalid selection !. Please try again.")
        tv_recharge()


def tv_complaint():
    print("\n--- COMPLAINTS ---")
    print("1. No Signal \n2. Overcharged \n3. Back for Main Menu")
    choice = input("\nPlease select an option (1-3): ")

    if choice == "1":
        print("\n[TICKET CREATED] Complaint filed: No Signal.")
        tv_complaint()
    elif choice == "2":
        print("\n[TICKET CREATED] Complaint filed: Overcharged bill adjustment requested.")
        tv_complaint()
    elif choice == "3":
        main_menu()
    else:
        print("\n[!] Invalid selection. Please try again.")
        tv_complaint()


# FUNCTION CALL
if __name__ == "__main__":
    main_menu()