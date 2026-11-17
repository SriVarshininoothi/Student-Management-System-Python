

def validate_student_id(student_id):
    if isinstance(student_id,int) and not isinstance(student_id,bool) and student_id>0:
        return True
    return False

def validate_name(name):

    if isinstance(name,str) and name.strip()!= "" :
        return True
    return False

def validate_age(age):

    if isinstance(age,int) and not isinstance(age,bool) and age>0:
        return True
    return False

def validate_course(course):

    if isinstance(course,str) and course.strip()!="":
        return True
    return False

def validate_email(email):
    if isinstance(email,str) and email.strip()!="" and "@" in email and "." in email:
        return True
    return False

def validate_marks(marks):
    if isinstance(marks,int) and not isinstance(marks,bool) and 0<=marks<=100:
        return True
    return False