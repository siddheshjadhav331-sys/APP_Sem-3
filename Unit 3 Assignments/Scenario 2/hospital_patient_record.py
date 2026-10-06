import csv

with open("patients.csv", "r", newline="") as file:
    patients = list(csv.DictReader(file))

print("===== All Patient Details =====")

for patient in patients:
    print(
        f"Patient ID: {patient['Patient ID']}, "
        f"Name: {patient['Name']}, "
        f"Age: {patient['Age']}, "
        f"Gender: {patient['Gender']}, "
        f"Disease: {patient['Disease']}"
    )

patient_id = input("\nEnter Patient ID to search: ")

found = False

for patient in patients:
    if patient["Patient ID"].lower() == patient_id.lower():

        print("\n===== Patient Found =====")
        print("Patient ID:", patient["Patient ID"])
        print("Name      :", patient["Name"])
        print("Age       :", patient["Age"])
        print("Gender    :", patient["Gender"])
        print("Disease   :", patient["Disease"])

        found = True
        break

if not found:
    print("\nPatient not found.")

#Output
"""
===== All Patient Details =====
Patient ID: P101, Name: Rahul Sharma, Age: 45, Gender: Male, Disease: Diabetes
Patient ID: P102, Name: Priya Patil, Age: 32, Gender: Female, Disease: Fever
Patient ID: P103, Name: Amit Joshi, Age: 56, Gender: Male, Disease: Hypertension
Patient ID: P104, Name: Neha Kulkarni, Age: 28, Gender: Female, Disease: Migraine
Patient ID: P105, Name: Rohan Deshmukh, Age: 65, Gender: Male, Disease: Asthma

Enter Patient ID to search: P103

===== Patient Found =====
Patient ID: P103
Name      : Amit Joshi
Age       : 56
Gender    : Male
Disease   : Hypertension
"""