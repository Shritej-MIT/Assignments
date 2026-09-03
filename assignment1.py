
student_db = {}

subjects = [
    "Engineering Chemistry",
    "Engineering Mechanics",
    "Engineering Mathematics",
    "Python Programming"
]

while True:
    print("\n===== STUDENT DATA MANAGEMENT =====")
    print("1. Add a new student record")
    print("2. Delete an existing student record")
    print("3. Update student details")
    print("4. Display final student records")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add student
    if choice == 1:
        roll_no = int(input("Enter Roll Number: "))

        if roll_no in student_db:
            print("Student record already exists!")
        else:
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")

            marks = []

            for subject in subjects:
                mark = float(input(f"Enter marks for {subject}: "))
                marks.append(mark)

            student_db[roll_no] = (name, branch, marks)

            print("Student record added successfully!")

    # 2. Delete student
    elif choice == 2:
        roll_no = int(input("Enter Roll Number to delete: "))

        if roll_no in student_db:
            del student_db[roll_no]
            print("Student record deleted successfully!")
        else:
            print("Student record not found!")

    # 3. Update student
    elif choice == 3:
        roll_no = int(input("Enter Roll Number to update: "))

        if roll_no in student_db:
            name = input("Enter new Name: ")
            branch = input("Enter new Branch: ")

            marks = []

            for subject in subjects:
                mark = float(input(f"Enter new marks for {subject}: "))
                marks.append(mark)

            student_db[roll_no] = (name, branch, marks)

            print("Student record updated successfully!")
        else:
            print("Student record not found!")

    # 4. Display records
    elif choice == 4:
        if len(student_db) == 0:
            print("No student records available.")
        else:
            print("\n===== FINAL STUDENT RECORDS =====")

            for roll_no, details in student_db.items():

                name, branch, marks = details

                print("\nRoll Number:", roll_no)
                print("Name:", name)
                print("Branch:", branch)

                print("Marks:")
                for i in range(len(subjects)):
                    print(subjects[i], ":", marks[i])

                print("-----------------------------")

    # 5. Exit
    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please try again.")
