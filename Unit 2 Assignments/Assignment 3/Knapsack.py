def Knapsack_Bottom_Up(weights, values, capacity):

    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]
    
    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:

                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_items.append(i)

            w = w - weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items, dp

def Knapsack_Top_Down(weights, values, capacity):

    n = len(weights)

    memo = [[-1 for _ in range(capacity + 1)]
            for _ in range(n + 1)]

    def solve(i, w):

        if i == 0 or w == 0:
            return 0

        if memo[i][w] != -1:
            return memo[i][w]

        if weights[i - 1] > w:

            memo[i][w] = solve(i - 1, w)

        else:

            include = values[i - 1] + solve(
                i - 1,
                w - weights[i - 1]
            )

            exclude = solve(i - 1, w)

            memo[i][w] = max(include, exclude)

        return memo[i][w]

    maximum_value = solve(n, capacity)

    selected_items = []
    w = capacity

    for i in range(n, 0, -1):

        if solve(i, w) != solve(i - 1, w):

            selected_items.append(i)

            w = w - weights[i - 1]

    selected_items.reverse()
    return maximum_value, selected_items

weights = [2, 3, 5, 7]
values = [10, 15, 20, 25]
capacity = 5

print("0/1 KNAPSACK PROBLEM")
print("--------------------")

print("\nItems:")

for i in range(len(weights)):

    print(
        f"Item {i + 1}: Weight = {weights[i]}, "
        f"Value = {values[i]}"
    )

print("\nKnapsack Capacity:", capacity)

value1, items1, dp_table = Knapsack_Bottom_Up(
    weights,
    values,
    capacity
)

print("\n--- Bottom-Up Approach ---")
print("Maximum Value:", value1)
print("Selected Items:", items1)

print("\nDP Table:")

for row in dp_table:
    print(row)

value2, items2 = Knapsack_Top_Down(
    weights,
    values,
    capacity
)

print("\n--- Top-Down Approach ---")
print("Maximum Value:", value2)
print("Selected Items:", items2)

#Output
"""
0/1 KNAPSACK PROBLEM
--------------------

Items:
Item 1: Weight = 2, Value = 10
Item 2: Weight = 3, Value = 15
Item 3: Weight = 5, Value = 20
Item 4: Weight = 7, Value = 25

Knapsack Capacity: 5

--- Bottom-Up Approach ---
Maximum Value: 25
Selected Items: [1, 2]

DP Table:
[0, 0, 0, 0, 0, 0]
[0, 0, 10, 10, 10, 10]
[0, 0, 10, 15, 15, 25]
[0, 0, 10, 15, 15, 25]
[0, 0, 10, 15, 15, 25]

--- Top-Down Approach ---
Maximum Value: 25
Selected Items: [1, 2]
"""