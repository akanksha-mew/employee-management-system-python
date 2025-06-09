'''import pymysql as db

while True:
    conn = db.connect("127.0.0.1", "root", "", "ems")  # database created
    cur = conn.cursor()
    print("\nSelect option :\n[1] Insert Data \n[2] Update Data \n[3] Delete Data \n[4] Search Data \n[5] View All Data \n[6] Exit")
    option = int(input("\nEnter your choice : "))

    if option == 1:
        # inserting data
        lst = ["Eid ", "Name ", "Email ", "Contact ", "Salary ", "Hiredate ", "Address "]
        val = []
        for i in lst:
            v = input("Enter " + i)
            val.append(v)

        qryins = "insert into Employees values({},'{}','{}','{}',{},'{}','{}')".format(*val)
        cur.execute(qryins)
        conn.commit()

    elif option == 2:
        # update query
        eid = input("Enter Eid to update: ")
        sal = input("Enter new salary: ")
        add = input("Enter new address: ")
        qryupd = "update employees set salary=%s,address=%s where empid=%s"
        cur.execute(qryupd, (sal, add, eid))
        conn.commit()

    elif option == 3:
        # delete query
        eid = input("Enter Eid to delete: ")
        qrydel = "delete from employees where Empid=%s"
        cur.execute(qrydel, (eid,))
        conn.commit()

    elif option == 4:
        # search query
        eid = input("Enter Eid to search: ")
        qrysrch = "select * from employees where empid=%s"
        cur.execute(qrysrch, (eid,))
        rs = cur.fetchall()
        for i in rs:
            print(i)

    elif option == 5:
        # view all data query
        qryview = "select * from Employees"
        cur.execute(qryview)
        rs = cur.fetchall()
        print("Eid\t\tEname\t\tEmail\t\t\t\t\tContact\t\t\tSalary\t\t\tHiredate\t\tAddress")
        for i in rs:
            for j in i:
                print(j, end="\t\t")
            print()

    elif option == 6:
        exit(0)

    else:
        print("Invalid Choice")

    cur.close()
    conn.close()'''
import pymysql as db
import sys

# Establish a single connection outside the loop
try:
    conn = db.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ems"
    )
    cur = conn.cursor()
except db.MySQLError as e:
    print("Error connecting to the database:", e)
    sys.exit(1)  # Exit if connection fails

while True:
    print("\nSelect option :\n[1] Insert Data \n[2] Update Data \n[3] Delete Data \n[4] Search Data \n[5] View All Data \n[6] Exit")
    try:
        option = int(input("\nEnter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if option == 1:
        # Inserting data (Using parameterized query)
        lst = ["Eid", "Name", "Email", "Contact", "Salary", "Hiredate", "Address"]
        val = []
        for i in lst:
            v = input(f"Enter {i}: ")
            val.append(v)

        try:
            qryins = "INSERT INTO Employees (Empid, Name, Email, Contact, Salary, Hiredate, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(qryins, tuple(val))
            conn.commit()
            print("Data inserted successfully!")
        except db.MySQLError as e:
            print("Error inserting data:", e)

    elif option == 2:
        # Updating data
        eid = input("Enter Eid to update: ")
        sal = input("Enter new salary: ")
        add = input("Enter new address: ")

        try:
            qryupd = "UPDATE Employees SET Salary=%s, Address=%s WHERE Empid=%s"
            cur.execute(qryupd, (sal, add, eid))
            conn.commit()
            print("Data updated successfully!")
        except db.MySQLError as e:
            print("Error updating data:", e)

    elif option == 3:
        # Deleting data
        eid = input("Enter Eid to delete: ")
        
        try:
            qrydel = "DELETE FROM Employees WHERE Empid=%s"
            cur.execute(qrydel, (eid,))
            conn.commit()
            print("Data deleted successfully!")
        except db.MySQLError as e:
            print("Error deleting data:", e)

    elif option == 4:
        # Searching data
        eid = input("Enter Eid to search: ")

        try:
            qrysrch = "SELECT * FROM Employees WHERE Empid=%s"
            cur.execute(qrysrch, (eid,))
            rs = cur.fetchall()
            if rs:
                for i in rs:
                    print(i)
            else:
                print("No record found.")
        except db.MySQLError as e:
            print("Error searching data:", e)

    elif option == 5:
        # Viewing all data
        try:
            qryview = "SELECT * FROM Employees"
            cur.execute(qryview)
            rs = cur.fetchall()
            print("\nEid\t\tName\t\tEmail\t\tContact\t\tSalary\t\tHiredate\tAddress")
            for i in rs:
                print("\t\t".join(map(str, i)))
        except db.MySQLError as e:
            print("Error retrieving data:", e)

    elif option == 6:
        # Exiting the program safely
        print("Exiting the program...")
        cur.close()
        conn.close()
        sys.exit(0)

    else:
        print("Invalid Choice. Please enter a number between 1 and 6.")

