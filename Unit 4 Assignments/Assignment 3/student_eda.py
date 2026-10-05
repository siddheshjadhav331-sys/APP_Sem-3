import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_data.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Dataset Shape After Removing Duplicates:")
print(df.shape)

print("\nSummary Statistics:")
print(df.describe())

print("\nResult Distribution:")
print(df["Result"].value_counts())

print("\nResult Percentage:")
print(df["Result"].value_counts(normalize=True) * 100)

marks = df["Total_Marks"].to_numpy()

print("\nTotal Marks Analysis:")
print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

sns.set_style("whitegrid")

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Result")
plt.title("Student Result Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="Department")
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Total_Marks",
    hue="Result"
)
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Total Marks")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Total_Marks",
    hue="Result"
)
plt.title("Study Hours vs Total Marks")
plt.xlabel("Study Hours")
plt.ylabel("Total Marks")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Department",
    y="Total_Marks"
)
plt.title("Total Marks by Department")
plt.xlabel("Department")
plt.ylabel("Total Marks")
plt.show()

plt.figure(figsize=(10, 7))

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()

top_students = df.sort_values(
    by="Total_Marks",
    ascending=False
).head(10)

print("\nTop 10 Students:")
print(
    top_students[
        ["Student_ID", "Name", "Department", "Total_Marks", "Result"]
    ]
)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nEDA Completed Successfully!")