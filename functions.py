
# List to store students
students = []

# Reusable function to display student details

def display_student(student):

    print(f"\nStudent ID: {student['student_id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Email: {student['email']}")


# Reusable function to find a student by ID

def find_student(student_id):

    for student in students:

        if student["student_id"] == student_id:
            return student

    return None

# Adding Student Details

def add_student():

    try:

        student_id = int(input("Enter a student ID: "))

        if student_id <= 0:
            print("Student ID must be positive.")
            return

        # Check duplicate ID using find_student()
        if find_student(student_id) is not None:
            print(f"\nStudent ID {student_id} already exists! Registration cancelled.")
            return

        name = input("Enter student name: ")

        if name.strip() == "":
            print("Student name should not be empty.")
            return

        age = int(input("Enter student age: "))

        if age <= 0:
            print("Age should be a positive number.")
            return

        course = input("Enter student course: ")
        email = input("Enter student email: ")

    except ValueError:
        print("Invalid input! Please enter numeric values for ID and age.")
        return

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    students.append(student)

    print("\nStudent registered successfully!")


# View Student Details

def view_students():

    if not students:
        print("\nNo students registered yet.")
        return

    print("=================== REGISTERED STUDENTS ======================")

    for student in students:

        display_student(student)
        print("-" * 23)


# Search Student

def search_student():

    try:

        search_id = int(input("Enter Student ID to search: "))

        if search_id <= 0:
            print("Student ID must be positive.")
            return

        student = find_student(search_id)

        if student is not None:
            print("\nStudent Found!")
            display_student(student)

        else:
            print(f"Student with ID {search_id} not found.")

    except ValueError:
        print("Invalid input! Please enter a valid numeric Student ID.")


# Update Student Details

def update_student():

    try:

        update_id = int(input("Enter a Student ID: "))

        if update_id <= 0:
            print("Student ID must be positive.")
            return

        student = find_student(update_id)

        if student is None:
            print(f"\nStudent with ID {update_id} not found.")
            return

        print("\nStudent Found!")
        display_student(student)

        updated = False

        # Update Name

        name_require = input("Do you want to update Name? (yes/no): ")

        if name_require.lower() == "yes":

            new_name = input("Enter new name: ")

            if new_name.strip() != "":
                student["name"] = new_name
                updated = True

            else:
                print("Name cannot be empty. Keeping existing name.")

        # Update Age

        age_require = input("Do you want to update Age? (yes/no): ")

        if age_require.lower() == "yes":

            try:

                new_age = int(input("Enter new age: "))

                if new_age <= 0:
                    print("Age should be a positive number.")

                else:
                    student["age"] = new_age
                    updated = True

            except ValueError:
                print("Age should be a numeric value.")

        # Update Course

        course_require = input("Do you want to update Course? (yes/no): ")

        if course_require.lower() == "yes":

            new_course = input("Enter new course: ")

            if new_course.strip() != "":
                student["course"] = new_course
                updated = True

            else:
                print("Course field should not be empty.")

        # Update Email

        email_require = input("Do you want to update Email? (yes/no): ")

        if email_require.lower() == "yes":

            new_email = input("Enter new email: ")

            if new_email.strip() != "":
                student["email"] = new_email
                updated = True

            else:
                print("Email field should not be empty.")

        # Display update result after checking all fields

        if updated:
            print("\nStudent details updated successfully!")

        else:
            print("\nNo changes were made.")

    except ValueError:
        print("Invalid input. Please provide a numeric Student ID.")


# Delete Student

def delete_student():

    if not students:
        print("No students registered yet.")
        return

    try:

        delete_student_id = int(input("Enter Student ID to delete: "))

        if delete_student_id <= 0:
            print("Please enter a positive number.")
            return

        # Reuse find_student() instead of a for loop

        student = find_student(delete_student_id)

        if student is None:
            print(f"Student with ID {delete_student_id} not found.")
            return

        print("\nStudent Found!")
        display_student(student)

        delete_require = input("Are you sure you want to delete this student? (yes/no): ")

        if delete_require.lower() == "yes":

            students.remove(student)
            print("Student deleted successfully.")

        else:
            print("Student deletion cancelled.")

    except ValueError:
        print("Please enter a valid numeric Student ID.")

