
#Problem Statement
"""
Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to customize and format reports.
The system should allow users to define report templates and generate formatted reports dynamically. 
Demonstrate the implementation using an Employee Report.
"""

def report_formatter(func):
    def wrapper(self):
        print("=" * 40)
        print("       EMPLOYEE REPORT")
        print("=" * 40)
        func(self)
        print("=" * 40)
    return wrapper

class Report:

    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    @classmethod
    def default_template(cls):
        return cls(
            "Rahul Sharma",
            "EMP101",
            "IT Department",
            50000
        )

    def __str__(self):
        return (
            f"Employee Name : {self.name}\n"
            f"Employee ID   : {self.emp_id}\n"
            f"Department    : {self.department}\n"
            f"Salary        : ₹{self.salary}"
        )
    
    @report_formatter
    def generate_report(self):
        print(self)

employee = Report.default_template()
employee.generate_report()

#Output
"""
========================================
       EMPLOYEE REPORT
========================================
Employee Name : Rahul Sharma
Employee ID   : EMP101
Department    : IT Department
Salary        : ₹50000
========================================
"""