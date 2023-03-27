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
    def add_newccourse(self):

        studentid = int(input('Enter Student ID : '))
        for i in Studentslist:
            if studentid == i.Student_id:
                courseid = int(input('Enter Course ID : '))

                for x in Courseslist:
                    if courseid == x.course_id:
                        if self.Student_level == x.course_level:
                            self.Student_courses.append({"course name": x.course_name, "course id": x.course_id})
                            print(f'Added course {x.course_name} to student {i.Student_name} was done 👍👍')
                        else:
                            print('Course level not match with Student level !!\n😂😂😂')
                    elif self.Student_level != x.course_level:
                        print('This course is not exist !!\n😂😂😂')


            else:
                print('This student is not exist !!\n😂😂😂')

    def report(self):
        print(f'Student Name : {self.Student_name} ')
        print(f'Student ID : {self.Student_id} ')
        print(f'Student Level : {self.Student_level} ')
        print(f'Student Courses : ')
        count = 1
        for i in self.Student_courses:
            print(f'{count}- Course name : {i["course name"]} course id : {i["course id"]}')
            count += 1


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
                    print(f'Student {name} added with ID : {std.Student_id} as successfully 👍')
                else:
                    print(f'This level {level} is invalid 😂😂😂😂😂')
                print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')
                xx = int(input('choice : '))


            elif xx == 2:
                print('_____________________________')
                studentid1 = int(input('Enter Student ID : '))
                for i in Studentslist:
                    if studentid1 == i.Student_id:
                        Studentslist.remove(i)
                        print(F'Student {i.Student_name} was removed 😢😢')
                    else:
                        print(f'There is no student with this ID 😒😒 ')
                print('_____________________________')

                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))

            elif xx == 3:
                print('_____________________________')
                studentid1 = int(input('Enter Student ID : '))
                for i in Studentslist:
                    if studentid1 == i.Student_id:
                        name = input('Enter New Name : ')
                        level = input('Select New Level from (A-B-C) : ').capitalize()
                        if level in ['A', 'B', 'C']:
                            i.Student_name = name
                            i.Student_level = level
                        print(F'Details of Student {i.Student_id} was updated 👌👌 ')
                    else:
                        print(f'There is no student with this ID 😒😒 ')
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
                    print(f'Course {name} added with ID : {course.course_id} as successfully 👍')
                else:
                    print(f'This level {level} is invalid 😂😂😂😂😂')
                print('_____________________________')
                print(
                    '1. Add New Student\n2. Remove Student\n3. Edit Student\n4. Display all students\n5. Create new Course\n6. Add Course to student\n7. Exit')

                xx = int(input('choice : '))


            elif xx == 6:
                print('_____________________________')
                if len(Courseslist) != 0:
                    for i in Studentslist:
                        Student.add_newccourse(i)
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

    except IndexError:
        print('invalid input !!!\nTry again')
        print('_____________________________')
    except Exception as error:
        print(f'Unexpected {error}, {type(error)}\nTry again')
