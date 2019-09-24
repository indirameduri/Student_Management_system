import DAO


def show_my_courses(student, course_list):
    print('\nMy Courses:')
    print('#\tCOURSE NAME\tINSTRUCTOR NAME')
    attending_dao = DAO.AttendingDAO()
    my_courses = attending_dao.get_student_courses(course_list, student.get_email())
    i = 1
    for course in my_courses:
        print('{}\t{}\t{}'.format(i,course.get_name(),course.get_instructor()))
        i+=1

def show_all_courses(course_list):
    print('\nAll Courses:')
    print('ID\tCOURSE NAME\tINSTRUCTOR NAME')
    for course in course_list:
        print('{}\t{}\t{}'.format(course.get_id(),course.get_name(),course.get_instructor()))
        
def main():
    print('Welcome!')
    entry=None
    while entry!='3':
        entry = input('\n1. Student\n2. Add New Student\n3. Quit\nPlease, enter 1 or 2 or 3: ')
        
        if entry=='1':
            student_dao = DAO.StudentDAO()
            email = input('\nEnter Your Email: ')
            pw = input('Enter Your Password: ')
            
            if student_dao.validate_user(email, pw):
                course_dao = DAO.CourseDAO()
                attending_dao = DAO.AttendingDAO()
                student = student_dao.get_student_by_email(email)
                course_list = course_dao.get_courses()

                show_my_courses(student, course_list)
                print('\nWhat Would You Like To Do?')
                
                while entry!='2':
                    entry = input('\n1. Register To Course\n2. Logout\nPlease, enter 1 or 2: ')
                    
                    if entry=='1':
                        show_all_courses(course_list)
                        course_id = input('\nSelect Course By ID Number: ')
                        print("\nAttempting to Register...")
                        if attending_dao.register_student_to_course(email, course_id, course_list):
                            show_my_courses(student, course_list)
                        else:
                            print(f'Already registered to {course_id}! Choose wisely!')
                    elif entry=='2':
                        print('\nYou Have Been Logged Out.')
                    else:
                        print('\nInvalid Option...')
                
                       
            else:
                print('\nWrong Credentials!')
        elif entry=='2':
            s_dao = DAO.StudentDAO()
            
            print('\nTo add new student enter your Name and chosen Password!\n')
            fname=input('Enter First name here: ')
            lname=input('Enter your Last name here: ')
            if (fname !=""):
                email = fname.strip().lower()+'@pysc.edu'
                print(f'Your Email Id is: {email} ')
                pwd=input('Enter your password here: ')
                s_dao.add_new_student(email,fname+ ' '+lname,pwd)
                print('\nCongratulations! You are enrolled now!\n')
        elif entry=='3':
                print('\nClosing Program. Goodbye.')
        else:
            print('\nInvalid Option...')
    
if __name__=='__main__':
    main()