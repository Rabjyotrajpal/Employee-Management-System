import mysql.connector

def addEmployee(mydb, mycursor) :
    print("Add an Employee");
    name= input("Please enter your name ")
    post= input("Please enter your post ")
    sal= int(input("Please enter your salary "))
    employeId= int(input("Please enter your employee id "))

    sql = "INSERT INTO EMPLOYEE (id, name, post, salary) VALUES (%s,%s,%s,%s)"
    val = (employeId, name, post, sal)

    mycursor.execute(sql, val)
    mydb.commit()
    print ("===Employee with name " + name + " added succesfully===")
    print()

def removeEmployee(mydb, mycursor):
    print("Remove an Employee");
    employeeID= int(input("Please enter your Employee Id "))
    query="SELECT * FROM EMPLOYEE where ID={}".format(employeeID)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if len(myresult)==0:
        print("================")
        print("Record not found")
        print("================")
        print()
    else :
        sql = "DELETE FROM EMPLOYEE where ID=%s"
        val = (employeeID,)

        mycursor.execute(sql, val)

        mydb.commit();
        print("===Employee with id "+ str(employeeID) + " deleted succesfully===")
        print()

def displayEmployees( mycursor ) :
    print("Display the Employee list");
    mycursor.execute("SELECT * FROM EMPLOYEE")
    myresult = mycursor.fetchall()
    print ("===List of Employees are as below===")

    for x in myresult:
        print("Eployee Id : " + str(x[0]))
        print("Employee Name : " + x[1])
        print("Employee Post : " + x[2])
        print("Employee Salary : " + str(x[3]))
        print()
    print()

def searchEmployeeByName(mycursor):
    print("Search an Employee by Name ");
    name1= input("Please enter your name ")

    sql = "SELECT * FROM EMPLOYEE where NAME=%s"
    val = (name1,)

    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if len(myresult)==0:
        print("================")
        print("Record not found")
        print("================")
        print()
    else :
        print ("===List of Employees found with name are below===")
        for x in myresult:
            print("Employee Id : " + str(x[0]))
            print("Employee Name : " + x[1])
            print("Employee Post : " + x[2])
            print("Employee Salary : " + str(x[3]))
            print()
        print()


print("==========================");
print("EMPLOYEE MANAGEMENT SYSTEM");
print("==========================");
n=-1;

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manager",
    database="EMS"
)

print(mydb)

mycursor = mydb.cursor()

while n != 0 :
    print("Please enter the following keys for different functions:")
    print("1 : Add an Employee")
    print("2 : Remove an Employee")
    print("3 : Display the Employee")
    print("4 : Search an Employee list")
    print("0 : Exit")
    n = int(input("Please enter your choice "))
    if n==1 :
        addEmployee(mydb, mycursor);
    if n==2:
        removeEmployee(mydb, mycursor);
    if n==3 :
        displayEmployees(mycursor);
    if n==4 :
        searchEmployeeByName(mycursor);
    if n==0 :
        print ("Thank you for using EMPLOYEE MANAGEMENT SYSTEM ");
