
with open("input.txt", "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))

first_two_lines = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines copied to output.txt")

#input.txt
"""
Python is a powerful programming language.
It is widely used for web development.
Python supports file handling.
It is easy to learn and understand.
"""

#output.txt
"""
Python is a powerful programming language.
It is widely used for web development.
"""

#Output
"""
Number of lines: 4
First two lines copied to output.txt
"""