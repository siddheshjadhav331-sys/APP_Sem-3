import numpy as np

arr = np.arange(1, 11)

print("Original Array:")
print(arr)

print("\nFirst 5 elements:")
print(arr[:5])

print("\nElements from index 5 to 8:")
print(arr[5:9])

print("\nEvery alternate element:")
print(arr[::2])

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5

print("\nArray after broadcasting (adding 5):")
print(arr)

#Output
"""
Original Array:
[ 1  2  3  4  5  6  7  8  9 10]

First 5 elements:
[1 2 3 4 5]

Elements from index 5 to 8:
[6 7 8 9]

Every alternate element:
[1 3 5 7 9]

Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1

Array after broadcasting (adding 5):
[ 6  7  8  9 10 11 12 13 14 15]
"""