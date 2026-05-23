def main_menu():

    print("\n--- MAIN MENU ---")
    print("1. Mobile Services")
    print("2. Internet services")
    print("3. Tv&ott series")
    print("4. Talk to customer support")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        mobile_services()

    elif choice == "3":
        Tv_and_ott_offers()
    
    elif choice == "2":
        print("Thank You")
    
    else:
        print("Invalid Choice")
        main_menu()


def mobile_services():

    print("\n--- MOBILE SERVICES ---")
    print("1. Prepaid")
    print("2. Postpaid")
    print("3. Back")

    choice = input("Enter Choice: ")

    if choice == "1":
        prepaid_menu()

    elif choice == "2":
        Postpaid_menu()
    
    elif choice == "3":
        main_menu()
    
    else:
        print("Invalid Choice")
        mobile_services()


def prepaid_menu():

    print("\n--- PREPAID MENU ---")
    print("1. Balance Inquiry")
    print("2. Recharge")
    print("3. Back")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("Your Balance is Rs.250")
        prepaid_menu()

    elif choice == "2":
        print("Recharge Successful")
        prepaid_menu()

    elif choice == "3":
        mobile_services()

    else:
        print("Invalid Choice")
        prepaid_menu()
def Postpaid_menu():

    print("\n--- Postpaid MENU ---")
    print("1. Current bill")
    print("2. Bill payment")
    print("3. Back")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("Your Balance is Rs.250")
        Postpaid_menu()

    elif choice == "2":
        print("Recharge Successful")
        Postpaid_menu()

    elif choice == "3":
        mobile_services()

    else:
        print("Invalid Choice")
        Postpaid_menu()

#======================Internet services======================================
1
def internet_services():

    print("\n--- INTERNET SERVICES ---")
    print("1. Internet Balance")
    print("2. Recharge Internet Pack")
    print("3. Back")

    choice = input("Enter Choice: ")

    if choice == "1":

        print("Your Internet Balance is 2.5GB")
        internet_services()

    elif choice == "2":

        amount = int(input("Enter Recharge Amount: "))

        if amount >= 199:
            print("Internet Pack Activated Successfully")

        else:
            print("Minimum Internet Recharge is Rs.199")

        internet_services()

    elif choice == "3":
        main_menu()

    else:
        print("Invalid Choice")
        internet_services()
#=======================Tv_and_ott_offers():========================================

def Tv_and_ott_offers():
        
    print("\n1.Channel_pack")
    print("2.Recharge")
    print("3.complaint")
    print("4.back")
    
    choice = input("Enter Choice: ")

    if choice == "1":
        print("Channel_pack")
        Tv_and_ott_offers()

    elif choice == "2":
        print("Recharge")
        Tv_and_ott_offers()

    elif choice == "3":
        print("Complaint")
        Tv_and_ott_offers()
    
    elif choice == "4":
        print("back")
        Tv_and_ott_offers()
    
    else:
        print("invaild choice")
        Tv_and_ott_offers()

def Tv_and_ott_offers():

    print("\n--- TV & OTT Services ---")
    print("1. Channel Pack")
    print("2. Back")

    choice = input("Enter Choice: ")

    if choice == "1":
        channel_pack()        

    elif choice == "2":
        main_menu()           

    else:
        print("\n  Invalid Choice!")
        Tv_and_ott_offers()
def channel_pack():

  print("\n---Channel pack---")
  print("1. Sports pack")
  print("2. Movies pack")
  print("3. All-in-onepack")
  print("4. Back for Main Menu")

  choice = input("Enter Choice: ")

  if choice == "1":
        print("Sportspack")
        channel_pack()  
  elif choice == "2":
        print("Movies pack")
        channel_pack()
    
  elif choice=="3":
        print("All-in-onepack")
        channel_pack()
  elif choice == "4":
        print("Back for Main Menu")
        main_menu()
    
  else:
        print("Invalid Choice")
        channel_pack()


main_menu()