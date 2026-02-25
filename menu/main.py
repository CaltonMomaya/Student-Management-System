from crud.student import add_student, update_student, delete_student
from logic.storage import load_students, save_students


def main():
    # Load students from file
    students = load_students()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        choice = input("Choose: ")

        # ---------------- ADD STUDENT ----------------
        if choice == "1":
            student_id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")

            new_student = {
                "id": student_id,
                "name": name,
                "age": age,
                "course": course
            }

            add_student(students, new_student)
            save_students(students)

            print("Student added successfully.")

        # ---------------- UPDATE STUDENT ----------------
        elif choice == "2":
            student_id = input("Enter ID to update: ")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            course = input("Enter new course: ")

            updated_data = {
                "name": name,
                "age": age,
                "course": course
            }

            success = update_student(students, student_id, updated_data)

            if success:
                save_students(students)
                print("Student updated successfully.")
            else:
                print("Student not found.")

        # ---------------- DELETE STUDENT ----------------
        elif choice == "3":
            student_id = input("Enter ID to delete: ")

            success = delete_student(students, student_id)

            if success:
                save_students(students)
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        # ---------------- VIEW STUDENTS ----------------
        elif choice == "4":
            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(student)

        # ---------------- EXIT ----------------
        elif choice == "5":
            save_students(students)
            print("Goodbye!")
            break

        # ---------------- INVALID OPTION ----------------
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()