import json
import os

DATA_FILE = "data.json"

# ---------------------------
# Utility Functions
# ---------------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"


# ---------------------------
# CRUD Operations
# ---------------------------

def add_student(students):
    try:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        if any(student["roll_no"] == roll_no for student in students):
            print("❌ Roll number already exists!")
            return

        student = {
            "roll_no": roll_no,
            "name": name,
            "marks": marks,
            "grade": calculate_grade(marks)
        }

        students.append(student)
        save_data(students)
        print("✅ Student added successfully!")

    except ValueError:
        print("❌ Invalid input! Please enter correct data types.")


def view_students(students):
    if not students:
        print("📂 No student records found.")
        return

    print("\n📋 Student Records:")
    for student in students:
        print(f"Roll: {student['roll_no']} | "
              f"Name: {student['name']} | "
              f"Marks: {student['marks']} | "
              f"Grade: {student['grade']}")


def search_student(students):
    roll_no = int(input("Enter Roll Number to Search: "))
    for student in students:
        if student["roll_no"] == roll_no:
            print(student)
            return
    print("❌ Student not found.")


def update_student(students):
    roll_no = int(input("Enter Roll Number to Update: "))
    for student in students:
        if student["roll_no"] == roll_no:
            try:
                new_marks = float(input("Enter New Marks: "))
                student["marks"] = new_marks
                student["grade"] = calculate_grade(new_marks)
                save_data(students)
                print("✅ Student updated successfully!")
                return
            except ValueError:
                print("❌ Invalid marks input.")
                return
    print("❌ Student not found.")


def delete_student(students):
    roll_no = int(input("Enter Roll Number to Delete: "))
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_data(students)
            print("🗑 Student deleted successfully!")
            return
    print("❌ Student not found.")


def sort_students(students):
    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    print("\n🏆 Students Sorted by Marks:")
    for student in sorted_students:
        print(student)


def top_performer(students):
    if not students:
        print("No records found.")
        return
    top = max(students, key=lambda x: x["marks"])
    print("\n🌟 Top Performer:")
    print(top)


# ---------------------------
# Main Menu
# ---------------------------

def main():
    students = load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort by Marks")
        print("7. Show Top Performer")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            sort_students(students)
        elif choice == "7":
            top_performer(students)
        elif choice == "8":
            print("Exiting system. Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
