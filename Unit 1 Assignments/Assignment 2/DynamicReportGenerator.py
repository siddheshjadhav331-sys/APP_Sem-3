
def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("         STUDENT REPORT")
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper

class Report:
    college = "MIT ADT University"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")

student1 = Report("Siddhesh",54,92)
student1.display_report()
print()

Report.change_college("Sardar Patel Institute of Technology")

student2 = Report("Nikhil",30,38)
student2.display_report()

#Output
"""
========================================
         STUDENT REPORT
========================================
College : MIT ADT University
Name : Siddhesh
Roll No : 54
Marks : 92
Result : PASS
========================================

========================================
         STUDENT REPORT
========================================
College : Sardar Patel Institute of Technology
Name : Nikhil
Roll No : 30
Marks : 38
Result : FAIL
========================================
"""