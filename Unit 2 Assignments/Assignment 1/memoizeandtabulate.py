def fib_memo(n, m):
    if n <= 1:
        return n

    if m[n] != -1:
        return m[n]

    m[n] = fib_memo(n - 1, m) + fib_memo(n - 2, m)
    return m[n]

def fib_tab(n):
    if n <= 1:
        return n

    m = [0] * (n + 1)
    m[0] = 0
    m[1] = 1

    for i in range(2, n + 1):
        m[i] = m[i - 1] + m[i - 2]

    return m[n]

n = int(input("Enter a number: "))
m = [-1] * (n + 1)

print("Memoization:", fib_memo(n, m))
print("Tabulation:", fib_tab(n))

#Output
"""
Enter a number: 10
Memoization: 55
Tabulation: 55
"""