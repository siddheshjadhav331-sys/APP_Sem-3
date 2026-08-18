class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print("\nRoll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Marks       :", self.marks)
        print("Grade       :", self.get_grade())

class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if len(self.students) == 0:
            print("No student records found.")
        else:
            print("\n----- Student Records -----")
            for student in self.students:
                student.display()

college = College()

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")
    roll = int(input("Roll Number: "))
    name = input("Name: ")
    marks = float(input("Marks: "))

    s = Student(roll, name, marks)
    college.add_student(s)

college.display_students()

#Output
"""
Enter number of students: 1

Enter details of Student 1
Roll Number: 54
Name: Siddhesh Jadhav
Marks: 99

----- Student Records -----

Roll Number : 54
Name        : Siddhesh Jadhav
Marks       : 99.0
Grade       : A
"""