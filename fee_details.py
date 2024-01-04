def FEE_MENU():
    while True:
        #fees_details.clrscreen()
        print("\t\t...............................................")
        print("\t\t***** Welcome to Student Management System*****")
        print("\t\t...............................................")
        print("\n\t\t*************STUDENT FEE MENU****************")
        print("1: Fee Deposit")
        print("2: Fee Details")
        print("3: Return to MAIN MENU")
        print("\t\t..............................................")
        choice=int(input("Enter Your Choice:"))

        if choice==1:
            fees_details.fees_Deposit()
        elif choice==2:
            fees_details.FDetails()
        elif choice==3:
            return
        else:
            print("Error:Invalid Choice try again....")
            conti=input("Press any key to continue...")
