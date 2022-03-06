import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="Ganesh@123",
    database="assignment"
)
mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password="Ganesh@123",
    database = "assignment"
)


mycursor = mydb.cursor()
def user_login(login_details):
    user= input("Enter the username : ")
    password = input("enter the pass : ")
    sql = f"SELECT username fROM login_details WHERE username='{user}' AND Passwords = '{password}'"
    mycursor.execute(sql)




def add_employee():
    id = input("enter the id : ")
    name = input("enter the name : ")
    age = input("enter the age ")
    designation = input("enter the designation : ")
    
    cursor = con.cursor()
    
    sql = 'INSERT INTO employee(id, name, age, designation) values (%s, %s, %s, %s)'

    cursor.execute(sql,(id,name,age,designation))
    con.commit()
    print("\n")
    print("added succesfully")

def view_employee():
    cursor= con.cursor()
    sql = "select * from employee"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\n")
    print(tabulate(result,headers=["ID","NAME","AGE","DESIGNATION"]))

def delete_employee():

    id = input("Enter your ID: ")
    cu = con.cursor()
    sql = "delete from employee where id = %s"
    cu.execute(sql, (id,))
    con.commit()
    print("\n")
    view_employee()
    print("Deleted Successfully")
    
def update_employee():
    print("1.Name: ")
    print("2.Age: ")
    print("3.Designation ")
    option = int(input("\nWhich field you need to update? : "))

    if option == 1:
        id = input("Enter your ID: ")
        name = input("Enter your Name: ")
        cu = con.cursor()
        sql = "update employee set name = %s where id = %s"
        cu.execute(sql,(name,id))
        con.commit()
        view_employee()
        print("\n")
        print("Updated Successfully")
    elif option ==2:
        id = input("Enter your ID: ")
        age = input("Enter your Age: ")
        cu = con.cursor()
        sql = "update employee set age = %s where id = %s"
        cu.execute(sql, (age, id))
        con.commit()
        view_employee()
        print("\n")
        print("Updated Successfully")
    elif option == 3:
        id = input("Enter your ID: ")
        email = input("Enter your Designation: ")
        cu = con.cursor()
        sql = "update employee set designation = %s where id = %s"
        cu.execute(sql, (email, id))
        con.commit()
        view_employee()
        print("\n")
        print("Updated Successfully")
    else:
        print("Invalid")

def exit_details():
    exit()


user_login("login_details")

if mycursor.fetchone():

    while True:
        print("\n")
        print("1.Add User ")
        print("2.View User ")
        print("3.Delete User ")
        print("4.Update User")
        print("5.Exit")
        print("\n")

        option = int(input("Enter Your Option : "))

        if option == 1:
            add_employee()
        elif option == 2:
            view_employee()
        elif option == 3:
            delete_employee()        
        elif option == 4:
            update_employee()
        elif option == 5:
            exit_details()
    else:
        print("invalid")
    exit()
