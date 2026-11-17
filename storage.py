
import json
import os

from models import Student

# Conversion of  Object into Dictionary (python => JSON)

def student_to_dict(student):

    student_data = {

        "student_id":student.get_student_id(),
        "name": student.get_name(),
        "age": student.get_age(),
        "course": student.get_course(),
        "email":student.get_email(),
        "marks":student.get_marks()

    }
    return student_data
   
   
    
# Conversion of Dictionary to Object (JSON => Python)

def dict_to_student(student_data):

    student_id = student_data["student_id"]
    name = student_data["name"]
    age = student_data["age"]
    course = student_data["course"]
    email = student_data["email"]

    student = Student(student_id,name,age,course,email)

    marks = student_data.get("marks",{})

    for subject, mark in marks.items():

        student.set_marks(subject,mark)

    return student


# Save Students Data 

def save_students(students):

    student_data = []

    for student in students:

        student_data.append(student_to_dict(student)) # object to JSON {key:value} 

    os.makedirs("data", exist_ok=True)

    with open("data/students.json","w") as file:

        json.dump(student_data,file,indent=4)

    print("Student data saved successfully!")




# Loading students Data

def load_students():

    try:
        if not os.path.exists("data/students.json"):
            return []
        
        with open("data/students.json","r") as file:

            student_data =  json.load(file)

        students = []

        for data in student_data:
            
            students.append(dict_to_student(data)) # Json to Object

        return students
    
    except json.JSONDecodeError:

        print("Invalid or empty JSON file.Starting with an empty student List.")
        return []

