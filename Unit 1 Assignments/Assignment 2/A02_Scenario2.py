
#Problem Statement
"""
Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to customize and format reports. 
The system should allow users to define report templates and generate formatted reports dynamically. 
Demonstrate the implementation using a Monthly Sales Report.
"""

def format_report(func):
    def wrapper(self):
        print("=" * 50)
        print("          MONTHLY SALES REPORT")
        print("=" * 50)
        func(self)
        print("=" * 50)
    return wrapper

class SalesReport:

    def __init__(self, company, month, sales):
        self.company = company
        self.month = month
        self.sales = sales

    @classmethod
    def monthly_template(cls):
        return cls(
            "Invent Technologies",
            "July 2026",
            [25000, 18000, 30000, 22000]
        )

    def __str__(self):
        total = sum(self.sales)
        bonus = total * 0.10
        net_revenue = total + bonus

        return (
            f"Company      : {self.company}\n"
            f"Month        : {self.month}\n"
            f"Weekly Sales : {self.sales}\n"
            f"Total Sales  : ₹{total}\n"
            f"Bonus (10%)  : ₹{bonus:.2f}\n"
            f"Net Revenue  : ₹{net_revenue:.2f}"
        )

    @format_report
    def generate_report(self):
        print(self)

report = SalesReport.monthly_template()
report.generate_report()

#Output
"""
==================================================
          MONTHLY SALES REPORT
==================================================
Company      : Invent Technologies
Month        : July 2026
Weekly Sales : [25000, 18000, 30000, 22000]
Total Sales  : ₹95000
Bonus (10%)  : ₹9500.00
Net Revenue  : ₹104500.00
==================================================
"""