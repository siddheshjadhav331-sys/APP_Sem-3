import numpy as np
import pandas as pd

prices = np.array([45, 120, 80, 250, 60, 150, 90, 300, 75, 110])

mean_price = np.mean(prices)
median_price = np.median(prices)
maximum_price = np.max(prices)
minimum_price = np.min(prices)

print("===== Grocery Price Analysis =====")
print("Product Prices:", prices)
print("Mean Price   :", mean_price)
print("Median Price :", median_price)
print("Maximum Price:", maximum_price)
print("Minimum Price:", minimum_price)

data = {
    "Product": [
        "Rice",
        "Wheat",
        "Sugar",
        "Oil",
        "Milk",
        "Biscuits",
        "Tea",
        "Coffee",
        "Salt",
        "Soap"
    ],
    "Price": [45, 120, 80, 250, 60, 150, 90, 300, 75, 110],
    "Quantity": [25, 8, 15, 6, 20, 5, 12, 7, 30, 9]
}

df = pd.DataFrame(data)

print("\n===== Grocery Inventory =====")
print(df)

low_stock = df[df["Quantity"] < 10]

print("\n===== Low Stock Items (Quantity < 10) =====")
print(low_stock)

#Output
"""
===== Grocery Price Analysis =====
Product Prices: [ 45 120  80 250  60 150  90 300  75 110]
Mean Price   : 128.0
Median Price : 100.0
Maximum Price: 300
Minimum Price: 45

===== Grocery Inventory =====
    Product  Price  Quantity
0      Rice     45        25
1     Wheat    120         8
2     Sugar     80        15
3       Oil    250         6
4      Milk     60        20
5  Biscuits    150         5
6       Tea     90        12
7    Coffee    300         7
8      Salt     75        30
9      Soap    110         9

===== Low Stock Items (Quantity < 10) =====
    Product  Price  Quantity
1     Wheat    120         8
3       Oil    250         6
5  Biscuits    150         5
7    Coffee    300         7
9      Soap    110         9
"""