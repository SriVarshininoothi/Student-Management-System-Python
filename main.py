
from functions import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    add_marks,
    calculate_grade,
    mark_attendance,
)

from reports import (
    generate_student_report,
    view_attendance,
    calculate_attendance_percentage,
)


# Display the menu list

def display_menu():

    print("===============================================")
    print("           STUDENT MANAGEMENT SYSTEM          ")
    print("===============================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add/Update Marks")
    print("7. Calculate Grade")
    print("8. Student Report")
    print("9. Mark Attendance")
    print("10. View Attendance")
    print("11. Calculate Attendance Percentage")
    print("12. Exit")


# Handling User Choices

def handle_menu_choice(choice):

    if choice == 1:
        print("You selected: Add Student")
        add_student()

    elif choice == 2:
        print("You selected: View All Students")
        view_students()

    elif choice == 3:
        print("You selected: Search Student")
        search_student()

    elif choice == 4:
        print("You selected: Update Student")
        update_student()

    elif choice == 5:
        print("You selected: Delete Student")
        delete_student()

    elif choice == 6:
        print("You selected: Update/Add Marks")
        add_marks()

    elif choice == 7:
        print("You selected: Calculate Grade")
        calculate_grade()

    elif choice == 8:
        print("You selected: Student Report")
        generate_student_report()

    elif choice == 9:
        print("You selected: Mark Attendance")
        mark_attendance()

    elif choice == 10:
        print("You selected: View Attendance")
        view_attendance()

    elif choice == 11:
        print("You selected: Calculate Attendance Percentage")
        calculate_attendance_percentage()

    elif choice == 12:
        print("Exiting Application. Thank you!")
        return

    else:
        print("Invalid choice, please try again.")


# Main Function

def main():

    choice = 0

    while choice != 12:

        display_menu()

        try:
            choice = int(input("Enter your choice: "))
            handle_menu_choice(choice)

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 12.")
            choice = 0


if __name__ == "__main__":
    main()
