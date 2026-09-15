import csv
import json

with open("student.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open("student.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")

#Input(student.csv)
"""
Roll_No,Name,Branch,Marks
1,Rahul,CSE,85
2,Priya,CSE,90
3,Amit,IT,92
4,Neha,CSE,80
"""

#Output(student.json)
"""
[
    {
        "Roll_No": "1",
        "Name": "Rahul",
        "Branch": "CSE",
        "Marks": "85"
    },
    {
        "Roll_No": "2",
        "Name": "Priya",
        "Branch": "CSE",
        "Marks": "90"
    },
    {
        "Roll_No": "3",
        "Name": "Amit",
        "Branch": "IT",
        "Marks": "92"
    },
    {
        "Roll_No": "4",
        "Name": "Neha",
        "Branch": "CSE",
        "Marks": "80"
    }
]
"""