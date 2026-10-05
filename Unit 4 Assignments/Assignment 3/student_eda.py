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

#Output
"""
First 5 Records:
  Student_ID       Name  Gender  ... External_Marks  Total_Marks  Result
0     STU001  Student_1  Female  ...             83          139    Pass
1     STU002  Student_2  Female  ...             68          154    Pass
2     STU003  Student_3    Male  ...             82          140    Pass
3     STU004  Student_4  Female  ...             66          128    Pass
4     STU005  Student_5    Male  ...             81          166    Pass

[5 rows x 11 columns]

Dataset Shape:
(101, 11)

Column Names:
Index(['Student_ID', 'Name', 'Gender', 'Department', 'Attendance',
       'Study_Hours', 'Assignment_Score', 'Internal_Marks', 'External_Marks',
       'Total_Marks', 'Result'],
      dtype='object')

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 101 entries, 0 to 100
Data columns (total 11 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Student_ID        101 non-null    object 
 1   Name              101 non-null    object 
 2   Gender            101 non-null    object 
 3   Department        101 non-null    object 
 4   Attendance        98 non-null     float64
 5   Study_Hours      99 non-null     float64
 6   Assignment_Score  99 non-null     float64
 7   Internal_Marks    101 non-null    int64  
 8   External_Marks    101 non-null    int64  
 9   Total_Marks       101 non-null    int64  
10   Result            101 non-null    object 
dtypes: float64(3), int64(3), object(5)
memory usage: 8.8+ KB

Missing Values:
Student_ID          0
Name                0
Gender              0
Department          0
Attendance          3
Study_Hours         2
Assignment_Score    2
Internal_Marks      0
External_Marks      0
Total_Marks         0
Result              0
dtype: int64

Missing Values After Cleaning:
Student_ID          0
Name                0
Gender              0
Department          0
Attendance          0
Study_Hours         0
Assignment_Score    0
Internal_Marks      0
External_Marks      0
Total_Marks         0
Result              0
dtype: int64

Number of Duplicate Rows:
1

Dataset Shape After Removing Duplicates:
(100, 11)

Summary Statistics:
       Attendance  Study_Hours  ...  External_Marks  Total_Marks
count  100.000000   100.000000  ...       100.00000   100.000000
mean    76.242500     4.555000  ...        65.51000   128.420000
std     12.289914     2.055511  ...        18.76516    24.314098
min     55.700000     1.100000  ...        35.00000    77.000000
25%     64.525000     2.900000  ...        48.00000   109.750000
50%     76.450000     4.600000  ...        68.00000   128.000000
75%     87.425000     6.600000  ...        81.25000   143.250000
max     99.000000     7.900000  ...        95.00000   187.000000

[8 rows x 6 columns]

Result Distribution:
Result
Pass    100
Name: count, dtype: int64

Result Percentage:
Result
Pass    100.0
Name: proportion, dtype: float64

Total Marks Analysis:
Mean Marks: 128.42
Median Marks: 128.0
Standard Deviation: 24.192221890516795
Maximum Marks: 187
Minimum Marks: 77

Top 10 Students:
   Student_ID        Name Department  Total_Marks Result
27     STU028  Student_28       ENTC          187   Pass
55     STU056  Student_56       CSE          183   Pass
41     STU042  Student_42         IT          181   Pass
60     STU061  Student_61       CSE          179   Pass
25     STU026  Student_26         IT          177   Pass
98     STU099  Student_99         IT          176   Pass
75     STU076  Student_76         IT          173   Pass
59     STU060  Student_60         CSE          166   Pass
4      STU005  Student_5       ENTC          166   Pass
88     STU089  Student_89         CSE          163   Pass

Final Dataset Shape:
(100, 11)

EDA Completed Successfully!
"""