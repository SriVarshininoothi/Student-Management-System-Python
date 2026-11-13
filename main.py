
#code

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
      print("9. Attendance Management")
      print("10. Exit")



def handle_menu_choice(choice):

    if choice == 1:
       
        print("You selected: Add Student")
        add_student()
        
    elif choice == 2:
        print("You selected: View All Students")
        view_students()

    elif choice ==3:
        print("You selected: Search Student")
    elif choice == 4:
        print("You selected: Update Student")
    elif choice ==5:
        print("You selected: Delete Student")
    elif choice ==6:
        print("You selected: Update/Add Marks")
    elif choice ==7:
        print("You selected: Calculate Grade")
    elif choice == 8:
         print("You selected: Student Report")
    elif choice ==9:
         print("You selected: Attendance Management")
    elif choice ==10:
        print("Exiting Application")
    else:
        print("Invalid choice, please try again..")


students = []

def add_student():

    try:

        student_id = int(input("enter a student id: "))


        if student_id<=0:
            print(f"Student ID {student_id} not negative and zero")
            return
        

        for student in students:
            if student["student_id"] == student_id:
                print(f"\n Student ID {student_id} already exists! Registered cancelled")
                return
            

        name = input("Enter student name: ")
        if name == "":
            print(f"name should not empty")
            return 



        age = int(input("enter student age: "))
        if age<=0:
            print(f"\n Age {age} should be positive")
            return 

        course = input("Enter student course: ")
        email = input("enter student email: ")

    except ValueError:
        print("Invalid input! Please enter numeric values for ID and age.")
        return 
        
    
    student = {

        "student_id" : student_id,
        "name" : name,
        "age" : age,
        "course" : course,
        "email" : email
    }

    students.append(student)

    
    print("\n Student Registration successfully...")


def view_students():

    if not students:
        print("\n No students registered yet.")
        return 

    print("=================== REGISTERED STUDENTS ======================")

    for student in students:

        print(f"Student ID: {student['student_id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Email: {student['email']}")
        print("-"*23)



def main():

    choice=0
    while(choice!=10):
        display_menu()

        try:

            choice = int(input("Enter your choice: "))
            handle_menu_choice(choice)

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 10.")
            choice = 0
           
if __name__ == "__main__":
    main()