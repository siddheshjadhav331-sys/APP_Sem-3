import threading
import time

def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

def print_alphabets():
    for ch in 'ABCDE':
        print("Alphabet:", ch)
        time.sleep(1)

def print_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=print_squares)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed successfully!")

#Output
"""
Number: 1
Alphabet: A
Square of 1 = 1
Number: 2
Alphabet: B
Square of 2 = 4
Number: 3
Square of 3 = 9
Alphabet: C
Number: 4
Square of 4 = 16
Alphabet: D
Number: 5
Square of 5 = 25
Alphabet: E
All tasks completed successfully!
"""