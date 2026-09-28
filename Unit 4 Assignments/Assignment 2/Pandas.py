import pandas as pd
import numpy as np

np.random.seed(42)
numbers = np.random.randint(1, 101, 10)

series = pd.Series(numbers)

print("Original Series:")
print(series)

print("\nIndexing:")
print("Element at index 0:", series[0])
print("Elements from index 2 to 5:")
print(series[2:6])

print("\nFiltering:")
print("Numbers greater than 50:")
print(series[series > 50])

print("\nStatistical Operations:")
print("Mean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())

#Output
"""
Original Series:
0     52
1     93
2     15
3     72
4     61
5     21
6     83
7     87
8     75
9     75
dtype: int64

Indexing:
Element at index 0: 52
Elements from index 2 to 5:
2    15
3    72
4    61
5    21
dtype: int64

Filtering:
Numbers greater than 50:
0    52
1    93
3    72
4    61
6    83
7    87
8    75
9    75
dtype: int64

Statistical Operations:
Mean: 63.4
Median: 73.5
Minimum: 15
Maximum: 93
"""