from abc import ABC, abstractmethod
from datetime import datetime
import random

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} processed using Credit Card.")

class DebitCard(Payment):

    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} processed using Debit Card.")

class UPI(Payment):

    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} processed using UPI.")

class NetBanking(Payment):

    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} processed using Net Banking.")

class PaymentProcess:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):

        if amount <= 0:
            print("Invalid Payment Amount!")
            return

        print("\nProcessing Payment...")
        self.strategy.pay(amount)

        transaction_id = random.randint(100000,999999)

        print("\n----- Payment Receipt ---------------")
        print("Transaction ID :", transaction_id)
        print("Amount         : ₹{:.2f}".format(amount))
        print("Date & Time    :", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        print("Status         : SUCCESS")
        print("-------------------------------------")

def main():

    while True:

        print("\n====== PAYMENT PROCESSING SYSTEM ======")
        print("Select Payment Method")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Net Banking")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank You!")
            break

        try:
            amount = float(input("Enter payment amount (₹): "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if choice == "1":
            strategy = CreditCard()
        elif choice == "2":
            strategy = DebitCard()
        elif choice == "3":
            strategy = UPI()
        elif choice == "4":
            strategy = NetBanking()
        else:
            print("Invalid choice! Please enter a valid choice.")
            continue

        processor = PaymentProcess(strategy)
        processor.process_payment(amount)

if __name__ == "__main__":
    main()

#Output

"""
====== PAYMENT PROCESSING SYSTEM ======
Select Payment Method
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Enter your choice (1-5): 3
Enter payment amount (₹): 500

Processing Payment...
Payment of ₹500.00 processed using UPI.

----- Payment Receipt ---------------
Transaction ID : 681014
Amount         : ₹500.00
Date & Time    : 27-07-2026 17:14:01
Status         : SUCCESS
-------------------------------------
"""