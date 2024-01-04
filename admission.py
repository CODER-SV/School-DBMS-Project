import main_menu
import admission
import mysql.connector as co
def ADM_MENU():
    while True:
        #admission.clrscreen()
        print("\t\t...............................................")
        print("\t\t***** Welcome to Student Management System*****")
        print("\t\t...............................................")
        print("\n\t\t***************ADMISSION MENU****************")
        print("1: Admission Details")
        print("2: Show Admi.Details")
        print("3: Search")
        print("4: Deletion")
        print("5: Update Admission Details")
        print("6: Return to MAIN MENU")
        print("\t\t..............................................")
        choice=int(input("Enter Your Choice:"))

        if choice==1:
            admission.Admin_Details()
        elif choice==2:
            admission.Show_Admin_Details()
        elif choice==3:
            admission.Search_Admin_Details()
        elif choice==4:
            admission.Delete_Admin_Details()
        elif choice==5:
            admission.Edit_Admin_Details()
        elif choice==6:
            return
        else:
            print("Error:Invalid Choice try again....")
            conti=input("Press any key to continue...")

def Admin_Details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
        mycur=mycon.cursor()
        adno=input("Enter Admission No:")
        rno=int(input("Enter Roll no:"))
        sname=input("Enter Student Name:")
        address=input("Enter State:")
        phon=input("Enter phone number:")
        clas=input("Enter Class:")

        Query="insert into admission(adno,rno,sname,address,phon,clas) values('{}','{}','{}','{}','{}','{}')".format(adno, rno, sname, address, phon, clas) 
        mycur.execute(Query)
        mycon.commit()
        mycon.close()
        mycur.close()
        print("Record hass been Saved .. in Admission Data Table.... ")
    except:
        print("error")        
def Show_Admin_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    mycur.execute("select * from admission")
    data=mycur.fetchall()
    for row in data:
        print(row)
        
def Search_Admin_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Admission Number:")
    st="select * from admission where adno='%s'"%ac
    mycur.execute(st)
    data=mycur.fetchall()
    print(data)
    
def Delete_Admin_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Admission Number:")
    st="delete from admission where adno='%s'"%ac
    mycur.execute(st)
    mycon.commit()
    print("Data deleted successfully")
    
def Edit_Admin_Details():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    cursor=mycon.cursor()
    print("1: Edit Name")
    print("2: Edit Address")
    print("3: Phone number")
    print("4: Return")
    print("\t\t...................................................")
    choice=int(input("Enter your choice:"))

    if choice==1:
        admission.Edit_name()
    elif choice==2:
        admission.Edit_address()
    elif choice==3:
        admission.Edit_phno()
    elif choice==4:
        return
    else:
        print("Error:Invalid Choice try again....")
        conti=input("Press any key to continue...")
        
def Edit_name():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Admission Number:")
    nm=input("Enter correct name:")
    st="update admission set sname='%s' where adno='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")

def Edit_address():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Admission Number:")
    nm=input("Enter correct address:")
    st="update admission set address='%s' where adno='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")
def Edit_phno():
    mycon=co.connect(host="localhost", user="root", passwd="789&*(gmail", database="project")
    mycur=mycon.cursor()
    ac=input("Enter Admission Number:")
    nm=input("Enter correct phone:")
    st="update admission set phon='%s' where adno='%s'"%(nm,ac)
    mycur.execute(st)
    mycon.commit()
    print("Data updated successfully")
