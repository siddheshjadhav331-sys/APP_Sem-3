class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def get_category(self):
        if self.treatment_cost >= 50000:
            return "Special"
        else:
            return "General"

    def display(self):
        print("\nPatient ID      :", self.patient_id)
        print("Name            :", self.name)
        print("Treatment Cost  :", self.treatment_cost)
        print("Category        :", self.get_category())

class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        if len(self.patients) == 0:
            print("No patient records found.")
        else:
            print("\n----- Patient Records -----")
            for patient in self.patients:
                patient.display()

hospital = Hospital()

n = int(input("Enter number of patients: "))

for i in range(n):
    print(f"\nEnter details of Patient {i + 1}")
    pid = int(input("Patient ID: "))
    name = input("Name: ")
    cost = float(input("Treatment Cost: "))

    p = Patient(pid, name, cost)
    hospital.add_patient(p)

hospital.display_patients()

#Output
"""
Enter number of patients: 1

Enter details of Patient 1
Patient ID: 142
Name: Rajesh
Treatment Cost: 15000 

----- Patient Records -----

Patient ID      : 142
Name            : Rajesh
Treatment Cost  : 15000.0
Category        : General
"""