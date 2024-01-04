def LIB_MENU():
    while True:
        #lib_details.clrscreen()
        print("\t\t...............................................")
        print("\t\t***** Welcome to Student Management System*****")
        print("\t\t...............................................")
        print("\n\t\t***************LIBRARY MENU******************")
        print("1: Book Issue")
        print("2: Book Return")
        print("3: Return to MAIN MENU")
        print("\t\t..............................................")
        choice=int(input("Enter Your Choice:"))

        if choice==1:
            lib_details.book_issue()
        elif choice==2:
            lib_details.book_return()
        elif choice==3:
            return
        else:
            print("Error:Invalid Choice try again....")
            conti=input("Press any key to continue...")
