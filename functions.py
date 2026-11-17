from models import Student

from storage import load_students,save_students

from validation import(
    validate_student_id,
    validate_name,
    validate_email,
    validate_age,
    validate_course,
    validate_marks
)

from reports import get_grade


# List to store students
students = load_students()

# Reusable function to display student details

def display_student(student):

    print(f"\nStudent ID: {student.get_student_id()}")
    print(f"Name: {student.get_name()}")
    print(f"Age: {student.get_age()}")
    print(f"Course: {student.get_course()}")
    print(f"Email: {student.get_email()}")
    print(f"marks:{student.get_marks()}")


# Reusable function to find a student by ID

def find_student(student_id):

    for student in students:

        if student.get_student_id() == student_id:
            return student

    return None

# Adding Student Details

def add_student():

    try:

        student_id = int(input("Enter a student ID: "))

        if not validate_student_id(student_id):
            print("Invalid Student ID.")
            return 

        # Check duplicate ID using find_student()
        if find_student(student_id) is not None:
            print(f"\nStudent ID {student_id} already exists! Registration cancelled.")
            return

        name = input("Enter student name: ")
        if not validate_name(name):
            print("Invalid Student Name.")
            return



        age = int(input("Enter student age: "))

        if not validate_age(age):
            print("Invalid Student Age.")
            return 

        course = input("Enter student course: ")
        if not validate_course(course):
            print("Invalid Student Course.")
            return 

        email = input("Enter student email: ")
        if not validate_email(email):
            print("Invalid Student Email")
            return 

    except ValueError:
        print("Invalid input! Please enter numeric values for ID and age.")
        return

    student = Student(student_id,name,age,course,email)

    students.append(student)
    save_students(students)

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

        if not validate_student_id(search_id):
            print("Invalid Student ID")
            return

        student = find_student(search_id)

        if student is not None:
            print("\nStudent Found!")
            display_student(student)

        else:
            print(f"Student with ID {search_id} not found.")

    except ValueError:
        print("Invalid input! Please enter a valid numeric Student ID.")


# update students

def update_student():

    try:

        update_id = int(input("Enter a Student ID: "))

        if not validate_student_id(update_id):
            print("Invalid Student ID.")
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

            # Name
            if not validate_name(new_name):
                print("Invalid Student Name.")
            else:
                student.set_name(new_name)
                updated = True

        # Update Age
        age_require = input("Do you want to update Age? (yes/no): ")

        if age_require.lower() == "yes":

            try:
                new_age = int(input("Enter new age: "))

                if not validate_age(new_age):
                    print("Invalid age. Keeping existing age.")
                else:
                    student.set_age(new_age)
                    updated = True
                    

            except ValueError:
                print("Age should be a numeric value.")

        # Update Course
        course_require = input("Do you want to update Course? (yes/no): ")

        if course_require.lower() == "yes":

            new_course = input("Enter new course: ")

            if not validate_course(new_course):
                print("Invalid course. Keeping existing course.")
                
                
            else:
                student.set_course(new_course)
                updated=True
                
        # Update Email
        email_require = input("Do you want to update Email? (yes/no): ")

        if email_require.lower() == "yes":

            new_email = input("Enter new email: ")

            if not validate_email(new_email):
                print("Invalid email. Keeping existing email.")
            else:
                student.set_email(new_email)
                updated = True
                

        # Display update result
        if updated:
            print("\nStudent details updated successfully!")
            save_students(students)
            display_student(student)
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

        if not validate_student_id(delete_student_id):
            print("Invalid Student ID")
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
            save_students(students)
            print("Student deleted successfully.")

        else:
            print("Student deletion cancelled.")

    except ValueError:
        print("Please enter a valid numeric Student ID.")


# Adding Marks to their subject wise

def add_marks():

    try:

        student_id = int(input("Enter Student ID. "))

        if not validate_student_id(student_id):
            print("Invalid Student ID")
            return 

        student = find_student(student_id)

        if student is None:

            print(f"Student with ID {student_id} not found.")
            return 

        subject = input("Enter Subject: ")

        if not validate_course(subject):
            print("Invalid Subject.")
            return 

        marks = int(input("Enter Marks: "))

        if not validate_marks(marks):
            print("Invalid Marks.Enter marks between o and 100.")
            return 
        
        student.set_marks(subject,marks)
        save_students(students)
        print("Marks added successfully!")
        

    except ValueError:

        print("Invalid input! Please enter numeric values for Student ID and marks.")


# Calculate Student Grade

def calculate_grade():

    try:
    
            student_id = int(input("Enter Student ID. "))
    
            if not validate_student_id(student_id):
                print("Invalid Student ID")
                return 
    
            student = find_student(student_id)
    
            if student is None:
    
                print(f"Student with ID {student_id} not found.")
                return 
            
            marks = student.get_marks()

            if not marks:
                print("No marks found for this student.")
                return 

            for subject,mark in marks.items():

                grade = get_grade(mark)

                print(subject,mark,grade)
            
    except ValueError:
    
            print("Invalid input! Please enter numeric values for Student ID and marks.")


