import main_menu
import admission
import student_data
import fee_details
import lib_details

while True:
    #main_menu.clrscreen()
    print("\t\t..............................................")
    print("\t\t***** Welcome to Student Management System*****")
    print("\t\t..............................................")
    print("\n\t\t*************KV PICKET-MAIN MENU****************")
    print("1: Admission Menu")
    print("2: Student Menu")
    print("3: Fee Menu")
    print("4: Exit")
    print("\t\t..............................................")
    choice=int(input("Enter Your Choice:"))

    if choice==1:
        admission.ADM_MENU()
    elif choice==2:
        student_data.STU_MENU()
    elif choice==3:
        fee_details.FEE_MENU()
    elif choice==4:
        break
    else:
        print("Error:Invalid Choice try again....")
        conti=input("Press any key to continue...")
         
        
