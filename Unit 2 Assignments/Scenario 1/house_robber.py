n = int(input("Enter the number of houses: "))

houses = []

for i in range(n):
    amount = int(input(f"Enter amount in house {i + 1}: "))
    houses.append(amount)

if n == 0:
    maximum_amount = 0

elif n == 1:
    maximum_amount = houses[0]

else:
    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    maximum_amount = dp[n - 1]

print("\nHouse Amounts:", houses)
print("Maximum possible amount:", maximum_amount)

#Output
"""
Enter the number of houses: 6
Enter amount in house 1: 100
Enter amount in house 2: 200
Enter amount in house 3: 300
Enter amount in house 4: 100
Enter amount in house 5: 400
Enter amount in house 6: 200

House Amounts: [100, 200, 300, 100, 400, 200]
Maximum possible amount: 900
"""