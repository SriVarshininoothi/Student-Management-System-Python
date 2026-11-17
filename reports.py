from validation import validate_student_id

from functions import find_student

def get_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"
    

def generate_student_report():

    try:

        student_id = int(input("enter Student ID. "))

        if not validate_student_id(student_id):
            print("Invalid Student ID.")
            return

        student = find_student(student_id)

        if student is None:
            print(f"Student with ID {student_id} not found.")
            return 

        marks = student.get_marks()

        print("\n ======== STUDENT REPORT =============")

        print(f"Student ID : {student.get_student_id()}")
        print(f"Name       :  {student.get_name()}")
        print(f"Age        :  {student.get_age()}")
        print(f"Course     :   {student.get_course()}")
        print(f"Email      :   {student.get_email()}")

        if not marks:
            print("\nNo marks available for this student.")
            return

        total = 0
        overall_result = "Pass"

        print("\n---------- Subject Details ----------")

        for subject,mark in marks.items():

            grade = get_grade(mark)

            if mark < 40:
                overall_result = "Fail"

            total += mark


            print(f"{subject}  :  {mark} - Grade {grade}")

        average = total/len(marks)



        print("\n--------- Academic Summary -----------") 

        print(f"Total Marks : {total}")
        print(f"Average     : {average:.2f}")
        print(f"Result      : {overall_result}")


        print("==============================================")




    except ValueError:
        print("Inavlid input! Pkease enter a numeric Student ID.")
