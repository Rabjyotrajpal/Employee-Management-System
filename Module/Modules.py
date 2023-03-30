def addEmployee(mydb, mycursor) :
    print("Add an Employee");
    name= input("Elease enter your name ")
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
    employeeID= input("Please enter your Employee Id ")

    sql = "DELETE FROM EMPLOYEE where ID=%s"
    val = (employeeID,)

    mycursor.execute(sql, val)

    mydb.commit();
    print("===Employee with id "+ employeeID + " deleted succesfully===")
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
    name1= input("Please enter yoour name ")

    sql = "SELECT * FROM EMPLOYEE where NAME=%s"
    val = (name1,)

    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print ("===List of Employees found with name are below===")
    for x in myresult:
        print("Employee Id ; " + str(x[0]))
        print("Employee Name ; " + x[1])
        print("Employee Post ; " + x[2])
        print("Employee Salary ; " + str(x[3]))
        print()
    print()
