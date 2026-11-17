class Student:

    def __init__(self,student_id,name,age,course,email):

        self.__student_id = student_id
        self.__name=name
        self.__age=age
        self.__course = course
        self.__email = email
        self.__subject_marks={}
        self.__attendance = {}

    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        if isinstance(new_name,str) and new_name.strip() != "":
            self.__name = new_name.strip()
            return True
        
        return False

    def set_age(self,new_age):
        if isinstance(new_age,int) and not isinstance(new_age,bool) and new_age > 0:
            self.__age = new_age
            return True
                    
        return False

    def get_age(self):
        return self.__age

    def get_course(self):
        return self.__course
    
    def set_course(self, new_course):
        if isinstance(new_course, str) and new_course.strip() != "":
            self.__course = new_course.strip()
            return True
                
        return False

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.strip() != "" and "@" in new_email and "." in new_email:
            self.__email = new_email.strip()
            return True

        return False

    def get_marks(self):
        return self.__subject_marks

    def set_marks(self,subject,marks):
          
          if ( isinstance(subject,str) 
          and subject.strip() != "" 
          and isinstance(marks,int)
          and not isinstance(marks,bool)
          and 0 <= marks<=100
          ):
              self.__subject_marks[subject.strip()] = marks
              return True
          return False

    def get_attendance(self):
        return self.__attendance

    def set_attendance(self, date, status):
        if isinstance(date, str) and date.strip() != "" and isinstance(status, str):

            clean_status = status.strip().capitalize()

            if clean_status in ("Present", "Absent"):
                self.__attendance[date.strip()] = clean_status

                return True
            
        return False

    
   