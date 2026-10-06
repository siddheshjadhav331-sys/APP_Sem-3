import numpy as np
import pandas as pd

bills = np.array([1850, 3200, 2750, 4500, 2100, 3800, 1500, 5200, 2900, 3400])

mean_bill = np.mean(bills)
median_bill = np.median(bills)
maximum_bill = np.max(bills)
minimum_bill = np.min(bills)

print("===== Electricity Bill Analysis =====")
print("Electricity Bills:", bills)
print("Mean Bill    : ₹", mean_bill)
print("Median Bill  : ₹", median_bill)
print("Maximum Bill : ₹", maximum_bill)
print("Minimum Bill : ₹", minimum_bill)

data = {
    "Consumer": [
        "Rahul", "Amit", "Priya", "Sneha", "Rohan",
        "Neha", "Vikas", "Pooja", "Karan", "Anjali"
    ],
    "Units": [180, 320, 275, 450, 210, 380, 150, 520, 290, 340],
    "Bill Amount": bills
}

df = pd.DataFrame(data)

print("\n===== Electricity Bill Records =====")
print(df)

high_bills = df[df["Bill Amount"] > 3000]

print("\n===== Consumers with Bill Exceeding ₹3000 =====")
print(high_bills)

#Output
"""
===== Electricity Bill Analysis =====
Electricity Bills: [1850 3200 2750 4500 2100 3800 1500 5200 2900 3400]
Mean Bill    : ₹ 3125.0
Median Bill  : ₹ 3050.0
Maximum Bill : ₹ 5200
Minimum Bill : ₹ 1500

===== Electricity Bill Records =====
  Consumer  Units  Bill Amount
0    Rahul    180         1850
1     Amit    320         3200
2    Priya    275         2750
3    Sneha    450         4500
4    Rohan    210         2100
5     Neha    380         3800
6    Vikas    150         1500
7    Pooja    520         5200
8    Karan    290         2900
9   Anjali    340         3400

===== Consumers with Bill Exceeding ₹3000 =====
  Consumer  Units  Bill Amount
1     Amit    320         3200
3    Sneha    450         4500
5     Neha    380         3800
7    Pooja    520         5200
9   Anjali    340         3400
"""