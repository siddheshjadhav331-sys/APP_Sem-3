import csv
import argparse

parser = argparse.ArgumentParser(
    description="Course Information System"
)

parser.add_argument(
    "filename",
    help="Name of the CSV file containing course details"
)

args = parser.parse_args()

try:
    with open(args.filename, "r", newline="") as file:
        courses = list(csv.DictReader(file))

    print("\n===== All Course Records =====")

    for course in courses:
        print(
            f"Course ID: {course['Course ID']}, "
            f"Course Name: {course['Course Name']}, "
            f"Credits: {course['Credits']}, "
            f"Department: {course['Department']}"
        )

    course_id = input("\nEnter Course ID to search: ")

    found = False

    for course in courses:
        if course["Course ID"].lower() == course_id.lower():
            print("\n===== Course Found =====")
            print("Course ID  :", course["Course ID"])
            print("Course Name:", course["Course Name"])
            print("Credits    :", course["Credits"])
            print("Department :", course["Department"])

            found = True
            break

    if not found:
        print("\nCourse not found.")

except FileNotFoundError:
    print(f"Error: File '{args.filename}' not found.")

except KeyError:
    print("Error: CSV file does not contain the required columns.")

#Output
"""
===== All Course Records =====
Course ID: CS101, Course Name: Python Programming, Credits: 4, Department: Computer Science
Course ID: CS102, Course Name: Data Structures, Credits: 4, Department: Computer Science
Course ID: CS103, Course Name: Database Management, Credits: 3, Department: Computer Science
Course ID: CS104, Course Name: Web Development, Credits: 3, Department: Information Technology
Course ID: CS105, Course Name: Machine Learning, Credits: 4, Department: Computer Science

Enter Course ID to search: CS103

===== Course Found =====
Course ID  : CS103
Course Name: Database Management
Credits    : 3
Department : Computer Science
"""