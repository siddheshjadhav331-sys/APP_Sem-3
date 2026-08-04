def lcs(X, Y):
    a = len(X)
    b = len(Y)
    dp = [[0 for i in range(b + 1)] for j in range(a + 1)]

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i,j = a,b
    lcs_string = ""

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string = X[i - 1] + lcs_string
            i = i - 1
            j = j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i = i - 1
        else:
            j = j - 1

    return dp[a][b], lcs_string

seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

length,subsequence = lcs(seq1,seq2)

print("Longest Common Subsequence:", subsequence)
print("Length of LCS:", length)

#Output
"""
Enter first sequence: ACXYZM
Enter second sequence: ABCXYZ
Longest Common Subsequence: ACXYZ
Length of LCS: 5
"""