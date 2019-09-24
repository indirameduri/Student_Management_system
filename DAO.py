import Models

class StudentDAO:
#This method reads the Students.csv file and initiates the student data as a List
    def __init__(self):
        self.student_list=[]
        
        with open('students.csv',mode = 'r',encoding = 'utf-8') as f:
            for line in f:
                email, name, pwd = line.strip().split(',')
                s = Models.Student(email,name,pwd)
                self.student_list.append(s)

#This method returns the student data as a List 
    def get_students(self):
        return self.student_list
    
#This method takes an email and a password from the user input. Return whether or not a Student with the given information is found.   
    def validate_user(self, email, pw):
        for student in self.student_list:
            if (email == student.get_email() and pw == student.get_password()):
                return True
            
        return False
    
#This method takes a Student’s email as a String searches the List of Students for a Student with that email and returns a Student Object.    
    def get_student_by_email(self, email):

        for student in self.student_list:
            if (email == student.get_email()):
                return student

#This method creates a new student entry in the students.csv file            
    def add_new_student(self,email,name,pwd):
        
        self.email = email
        self.name = name
        self.pwd = pwd
        new = '\n' + email + ',' + name.title() + ',' + pwd +'\n'
        
        with open('students.csv',mode = 'a') as f4:
            f4.write(new)
        
    
class CourseDAO:
#This method reads the courses.csv file and initiates the data as a List
    def __init__(self):
        self.course_list=[]
       
        with open('courses.csv',mode='r',encoding = 'utf-8') as f1:
            for course in f1:                 
                cid,cname,instr = course.strip().split(',')
                c_obj = Models.Course(cid,cname,instr)
                self.course_list.append(c_obj)
                
#This method takes no parameters and returns every Course in the system.        
    def get_courses(self):
        return self.course_list
    
class AttendingDAO:
#This method reads the attending.csv file and initiates the data as a List    
    def __init__(self):
        self.attending_list = []
        
        with open('attending.csv',mode = 'r') as f2:
            for attending in f2:
                c_id,stud_email=attending.strip().split(',')
                a_obj = Models.Attending(c_id,stud_email)
                self.attending_list.append(a_obj)
                
#This method returns the data as a List      
    def get_attending(self):
        return self.attending_list

#This method takes a Student’s Email and a Course List as parameters and searches the Attending List for all the courses a student is registered to.
#Then the course objects that correspond to each of these are added to a new List of courses. This list of courses the Student is attending is returned
    def get_student_courses(self, course_list, email):
        attd_list=[]

        for attending in self.attending_list:
            for course in course_list:
                if (attending.get_student_email() == email and course.get_id() == attending.get_course_id()):
                    attd_list.append(course)
        
        return attd_list
    
# This method takes a Student’s email, a Course ID, and a Course List. It checks if a Student with that Email is currently attending a Course with that ID.
# If the Student is not attending that Course and the Course ID is valid, then add a new Attending object with the Student’s Email and Course ID to the List and return True.
# Otherwise, return False.
    
    def register_student_to_course(self, email, course_id, course_list):
        
        for attending in self.attending_list:
            for course in course_list:
                if (email == attending.get_student_email()):
                    if(course_id == course.get_id()):
                        if(attending.get_course_id()!= course_id):
                            a = Models.Attending(course_id,email)
                            self.attending_list.append(a)
                            self.save_attending()
                            return True
                        else:
                            return False
                    
                        
                    
#This method overwrites the original Attending.csv file with the new data        
    def save_attending(self):
        
        with open('attending.csv',mode = 'w',encoding = 'utf-8') as f3:
            
            for attending in self.attending_list:
                
                f3.write(f"{attending.get_course_id()},{attending.get_student_email()}\n")