def add_student():

    file = open("students.txt", "a")

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    Reg_no = input("Enter student Reg.no: ")
    Semester = input("Enter student semester: ")
    
    CGPA = input("Enter student CGPA: ")

    file.write("-----------------------------\n")
    file.write("Name      : " + name + "\n")
    file.write("Age       : " + age + "\n")
    file.write("Reg No    : " + Reg_no + "\n")
    file.write("Semester  : " + Semester + "\n")
    file.write("CGPA      : " + CGPA + "\n")
    file.write("-----------------------------\n\n")

    file.close()

    print("Student Data Entered Successfully.")

def View_student():
    try:
        file = open("student.txt", "r")
    except:
        print("No student record found\n")
        return

    print("---- Student Record -----")

    for line in file:
        line = line.strip()
        data = line.split(",")

        print("Name:", data[0])
        print("Age:", data[1])
        print("Reg.no:", data[2])
        print("Semester:", data[3])
        print("CGPA:", data[4])
        print("-----------------------------")

    file.close()


def Search_student():

    name = input("Enter the student name for search: ")

    try:
        file = open("student.txt", "r")

    except:
        print("Not Found the Data.")
        return

    found = False

    for line in file:

        line = line.strip()
        data = line.split(",")

        if data[0].lower() == name.lower():

            print("------ Student Found ------")

            print("Name:", data[0])
            print("Age:", data[1])
            print("Reg.no:", data[2])
            print("Semester:", data[3])
            print("CGPA:", data[4])

            found = True
            break

    if not found:
        print("Student not found.")

    file.close()



while True:

    print("\n---------- Student Management System -----------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Please select the Choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        View_student()

    elif choice == '3':
        Search_student()

    elif choice == '4':
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid Choice.")