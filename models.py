class Student:

    def __init__(self,student_id,name,age,course,email):
        self.__student_id = student_id
        self.__name=name
        self.__age=age
        self.__course = course
        self.__email = email

    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        if new_name.strip() != "":
            self.__name = new_name.strip()
            print("Success")
        else:
            print("Invalid empty field")

    def set_age(self,new_age):
        if new_age > 0:
            self.__age = new_age
            print("Success")
        else:
            print("Inavlid age")

    def get_age(self):
        return self.__age

    def get_course(self):
        return self.__course
    
    def set_course(self, new_course):
        if new_course.strip() != "":
            self.__course = new_course.strip()
            print("Success")
        else:
            print("Invalid empty field")

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if new_email.strip() != "":
            self.__email = new_email.strip()
            print("Success")
        else:
            print("Invalid empty field")

    
            
    

student1 = Student(101,"Rahul",22,"Python","rahul@gmail.com")
student1.set_age(-1)
print(student1.get_age())       