import os
import csv

filename = "Employe.csv"

# Create CSV file
if not os.path.exists(filename):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["NAME", "ID", "Department", "Salary"])


while True:

    print("\n------- Employee Database --------------")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter the Choice: ")

    # Add Employee
    if choice == '1':

        name = input("Enter your name: ")
        empID = input("Enter your employee ID: ")
        department = input("Enter your department: ")
        salary = input("Enter your Salary: ")

        with open(filename, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, empID, department, salary])

        print("Added Successfully!")


    # View Employee
    elif choice == '2':

        print("\nEmployee Records")

        with open(filename, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)


    # Search Employee
    elif choice == '3':

        search = input("Enter employee ID: ")

        found = False

        with open(filename, 'r') as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) > 0 and row[1] == search:

                    print("\nEmployee Found")
                    print("Name:", row[0])
                    print("ID:", row[1])
                    print("Department:", row[2])
                    print("Salary:", row[3])

                    found = True


        if not found:
            print("Employee Not Found")


    # Exit
    elif choice == '4':

        print("Thank you for using Employee Database")
        break


    else:
        print("Invalid Choice!")