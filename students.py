class Student:
    def __init__(self, name, student_id, age, marks):
        self.name = name
        self.id = student_id
        self.age = age
        self.marks = marks

    def display(self):
        print("-" * 30)
        print("Name :", self.name)
        print("ID   :", self.id)
        print("Age  :", self.age)
        print("Marks:", self.marks)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, student_id, age, marks):
        # Check for duplicate ID
        for student in self.students:
            if student.id == student_id:
                print(f"Student with ID {student_id} already exists!")
                return

        self.students.append(Student(name, student_id, age, marks))
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()

    def search_by_name(self, name):
        found = False

        for student in self.students:
            if student.name.lower() == name.lower():
                student.display()
                found = True

        if not found:
            print("Student not found.")

    def search_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                student.display()
                return

        print("Student not found.")

    def update_student(self, student_id, age, marks):
        for student in self.students:
            if student.id == student_id:
                student.age = age
                student.marks = marks
                print("Student updated successfully!")
                return

        print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")

    def highest_marks(self):
        if not self.students:
            print("No students available.")
            return

        highest_student = max(self.students, key=lambda s: s.marks)

        print("\nStudent with Highest Marks:")
        highest_student.display()

    def exit_system(self):
        print("Thank you for using the Student Management System!")


sms = StudentManagementSystem()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by Name")
    print("4. Search Student by ID")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Highest Marks")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter Name: ").strip()
        student_id = int(input("Enter ID: "))
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        sms.add_student(name, student_id, age, marks)

    elif choice == 2:
        sms.display_students()

    elif choice == 3:
        name = input("Enter Name to Search: ")
        sms.search_by_name(name)

    elif choice == 4:
        student_id = int(input("Enter ID to Search: "))
        sms.search_by_id(student_id)

    elif choice == 5:
        student_id = int(input("Enter ID to Update: "))
        age = int(input("Enter New Age: "))
        marks = float(input("Enter New Marks: "))

        sms.update_student(student_id, age, marks)

    elif choice == 6:
        student_id = int(input("Enter ID to Delete: "))
        sms.delete_student(student_id)

    elif choice == 7:
        sms.highest_marks()

    elif choice == 8:
        sms.exit_system()
        break

    else:
        print("Invalid choice. Please try again.")