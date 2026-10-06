str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

m = len(str1)
n = len(str2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

max_length = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

            max_length = max(max_length, dp[i][j])

        else:
            dp[i][j] = 0

print("\nFirst String :", str1)
print("Second String:", str2)
print("Length of Longest Common Substring:", max_length)

#Output
"""
Enter first string: abcdef
Enter second string: zcdemf

First String : abcdef
Second String: zcdemf
Length of Longest Common Substring: 3
"""