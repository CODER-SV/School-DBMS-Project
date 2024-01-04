import main_menu
import student_data
import mysql.connector as co
def STU_MENU():
    while True:
        #student_data.clrscreen()
        print("\t\t...............................................")
        print("\t\t***** Welcome to Student Management System*****")
        print("\t\t...............................................")
        print("\n\t\t*************STUDENT DATA MENU***************")
        print("1: Add Student Record")
        print("2: Show Student Details")
        print("3: Search Student Record")
        print("4: Delete Student Record")
        print("5: Edit Student Record")
        print("6: Return to MAIN MENU")
        print("\t\t..............................................")
        choice=int(input("Enter Your Choice:"))

        if choice==1:
            student_data.Add_Records()
        elif choice==2:
            student_data.Show_Stu_Details()
        elif choice==3:
            student_data.Search_Stu_Details()
        elif choice==4:
            student_data.Delete_Stu_Details()
        elif choice==5:
            student_data.Edit_Stu_Details()
        elif choice==6:
            return
        else:
            print("Error:Invalid Choice try again....")
            conti=input("Press any key to continue...")

def Add_Records():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
        mycur=mycon.cursor()
        Id=input("Enter Student Id:")
        Name=input("Enter Student Name:")
        Email=input("Enter Student Email_Id:")
        Address=input("Enter Student Address(max=255):")
        Gender=input("Enter Student Gender:")
        DOB=input("Enter Student Date of Birth(i.e YYYYMMDD):")

        Query="insert into student(Id,Name,Email,Address,Gender,DOB) values('{}','{}','{}','{}','{}','{}')".format(Id,Name,Email,Address,Gender,DOB)
        mycur.execute(Query)
        mycon.commit()
        mycon.close()
        mycur.close()
        print("Record hass been Saved .. in Student Data Table.... ")
    except:
        print("Error")
        
def Show_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    mycur.execute("select * from student")
    data=mycur.fetchall()
    for row in data:
        print(row)
        
def Search_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Student Id Number:")
    st="select * from student where Id='%s'"%ac
    mycur.execute(st)
    data=mycur.fetchall()
    print(data)
    
def Delete_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Student Id Number:")
    st="delete from student where Id='%s'"%ac
    mycur.execute(st)
    mycon.commit()
    print("Data deleted successfully")

def Edit_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    cursor=mycon.cursor()
    print("1: Edit Name")
    print("2: Edit Address")
    print("3: Edit Gender")
    print("4: Edit DOB")
    print("5: Return")
    print("\t\t...................................................")
    choice=int(input("Enter your choice:"))

    if choice==1:
        student_data.Edit_name()
    elif choice==2:
        student_data.Edit_address()
    elif choice==3:
        student_data.Edit_gender()
    elif choice==4:
        student_data.Edit_DOB()
    elif choice==5:
        return
    else:
        print("Error:Invalid Choice try again....")
        conti=input("Press any key to continue...")
        
def Edit_name():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Student ID Number:")
    nm=input("Enter correct name:")
    st="update student set Name='%s' where Id='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")

def Edit_address():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Student ID Number:")
    nm=input("Enter correct address:")
    st="update student set Address='%s' where Id='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")

def Edit_gender():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Student ID Number:")
    nm=input("Enter correct Gender:")
    st="update student set Gender='%s' where Id='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")

def Edit_DOB():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Student ID Number:")
    nm=input("Enter correct DOB:")
    st="update student set DOB='%s' where Id='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")
    
    
    
