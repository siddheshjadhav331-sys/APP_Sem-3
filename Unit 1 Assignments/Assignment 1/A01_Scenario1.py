
#Problem Statement
"""
Write a program to create a simplified Student Course Registration System using object-oriented programming principles in Python. 
The system should manage students and courses, allowing basic operations such as:

1)Adding new courses
2)Registering students
3)Enrolling students in courses
4)Dropping courses
5)Viewing enrolled students and course details
"""

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print("Already enrolled in this course.")

    def display_courses(self):
        print(f"\nCourses enrolled by {self.name}:")
        if self.courses:
            for course in self.courses:
                print(course.course_name)
        else:
            print("No courses enrolled.")

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class RegistrationSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def display_students(self):
        print("\nRegistered Students:")
        for student in self.students:
            print(f"{student.student_id} - {student.name}")

    def display_courses(self):
        print("\nAvailable Courses:")
        for course in self.courses:
            print(f"{course.course_id} - {course.course_name}")

system = RegistrationSystem()

course1 = Course(101, "DBMS")
course2 = Course(102, "DSA")

system.add_course(course1)
system.add_course(course2)

student1 = Student(1, "Rahul")
student2 = Student(2, "Nikhil")

system.add_student(student1)
system.add_student(student2)

student1.enroll_course(course1)
student1.enroll_course(course2)
student2.enroll_course(course1)

system.display_students()
system.display_courses()

student1.display_courses()
student2.display_courses()

#Output
"""
Rahul enrolled in DBMS
Rahul enrolled in DSA
Nikhil enrolled in DBMS

Registered Students:
1 - Rahul
2 - Nikhil

Available Courses:
101 - DBMS
102 - DSA

Courses enrolled by Rahul:
DBMS
DSA

Courses enrolled by Nikhil:
DBMS
"""