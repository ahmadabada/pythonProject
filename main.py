Studentslist = []
Courseslist = []


class Course:
    Course_id = 0

    def __init__(self, name, level):
        self.course_name = name
        self.course_id = Course.Course_id
        self.course_level = level
        Course.Course_id += 1


class Student:
    Student_id = 0

    def __init__(self, name, level):
        self.Student_name = name
        self.Student_level = level
        self.Student_id = Student.Student_id
        self.Student_courses = []
        Student.Student_id += 1

    @staticmethod
    def add_new_course(self):
        count2 = 0
        course_id = int(input('Enter Course ID : '))
        for x in Courseslist:
            if course_id == x.course_id:
                count2 += 1
                if self.Student_level == x.course_level:
                    self.Student_courses.append({"course name": x.course_name, "course id": x.course_id})
                    print(f'Added course "{x.course_name}" to student "{i.Student_name}" was done 👍👍')

                else:
                    print('Course level not match with Student level !!\n😂😂😂')
            if count2 != 1:
                print('This course is not exist !!\n😂😂😂')
                count2 = 0

    def report(self):
        print(f'Student Name : {self.Student_name} ')
        print(f'Student ID : {self.Student_id} ')
        print(f'Student Level : {str(self.Student_level)} ')
        print(f'Student Courses : ')
        count4 = 1
        for i in self.Student_courses:
            print(f'{count4}. Course name : {i["course name"]} ,, course id : {i["course id"]}')
            count4 += 1


boola = True
while boola:
    try:
        xx = int(input(
            'Student Course Management System Menu:\n1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit\nChoose number from menu : '))
        while True:
            if xx == 1:
                print('_____________________________')
                name = input('Enter Student Name : ')
                level = input('Select Student Level from (A-B-C) : ').capitalize()
                if level in ['A', 'B', 'C']:
                    std = Student(name, level)
                    Studentslist.append(std)

                    print(f'Student "{name}" added with ID : {std.Student_id} as successfully 👍')
                else:
                    print(f'This level {level} is invalid 😂😂😂😂😂')
                print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')
                xx = int(input('choice : '))


            elif xx == 2:

                print('_____________________________')
                if len(Studentslist) != 0:
                    student_id1 = int(input('Enter Student ID : '))
                    len_list = len(Studentslist)
                    for i in Studentslist:
                        if student_id1 == i.Student_id:
                            Studentslist.remove(i)
                            print(F'Student {i.Student_name} was removed 😢😢')
                            break
                    if len_list == len(Studentslist):
                        print('There is no student with this ID 😒😒')
                else:
                    print('There is no student to remove !! ')

                print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))

            elif xx == 3:
                print('_____________________________')
                if len(Studentslist) != 0:
                    student_id1 = int(input('Enter Student ID : '))
                    lista = Studentslist
                    count1 = 0
                    for i in Studentslist:
                        if student_id1 == i.Student_id:
                            name = input('Enter New Name : ')
                            level = input('Select New Level from (A-B-C) : ').capitalize()
                            count1 += 1
                            if level in ['A', 'B', 'C']:
                                i.Student_name = name
                                i.Student_level = level
                                print(F'Details of Student {i.Student_id} was updated 👌👌 ')
                            else:
                                print(f'This level {level} is invalid 😂😂😂😂😂')
                    if count1 != 1:
                        print('There is no student with this ID 😒😒')
                else:
                    print('There is no student to edit !! ')

                print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))


            elif xx == 4:
                print('_____________________________')
                if len(Studentslist) == 0:
                    print('there is no any student !!!')
                    print('_____________________________')
                else:
                    for i in Studentslist:
                        i.report()
                        print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))

            elif xx == 5:
                print('_____________________________')
                name = input('Enter Course Name : ')
                level = input('Select Student Level from (A-B-C) : ').capitalize()
                if level in ['A', 'B', 'C']:
                    course = Course(name, level)
                    Courseslist.append(course)
                    print(f'Course "{name}" added with ID : {course.course_id} as successfully 👍')
                else:
                    print(f'This level {level} is invalid 😂😂😂😂😂')
                print('_____________________________')
                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))


            elif xx == 6:
                print('_____________________________')
                if len(Courseslist) != 0:
                    count3 = 0
                    student_id = int(input('Enter Student ID : '))
                    for i in Studentslist:
                        if student_id == i.Student_id:
                            count3 += 1
                            Student.add_new_course(i)
                    if count3 != 1:
                        print('This student is not exist !!\n😂😂😂')
                        count3 = 0
                    print('_____________________________')

                else:
                    print('There is no courses to add !!!')
                    print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))


            elif xx == 7:
                print('_____________________________')
                print('Welcome to ahmad program 😁😁')
                boola = False
                break
            else :
                print('_____________________________')
                print('invalid input please try again ')
                print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))


    except IndexError:
     print('invalid input !!!\nTry again')
     print('_____________________________')
    except Exception as error:
     print(f'Unexpected {error}, {type(error)}\nTry again')
     print('_____________________________')
