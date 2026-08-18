
print("1. WRITE OPERATION")

file = open("sample.txt", "w")
file.write("Hello, this is a Python file.\n")
file.write("This is an example of file handling.")
file.close()

print("Data written successfully.")

print("\n2. READ OPERATION")

file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()

print("\n3. READLINE() OPERATION")

file = open("sample.txt", "r")
line = file.readline()
print(line)
file.close()

print("4. READLINES() OPERATION")

file = open("sample.txt", "r")
lines = file.readlines()
print(lines)
file.close()

print("\n5. READ FILE LINE BY LINE")

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()

print("\n6. APPEND OPERATION")

file = open("sample.txt", "a")
file.write("\nThis line is added using append.")
file.close()

print("Data appended successfully.")

print("\n7. WRITE OPERATION")

file = open("newfile.txt", "w")
file.write("This is another file.")
file.close()

print("Data written to newfile.txt successfully.")

print("\nAll file handling operations completed.")

#Output
"""
1. WRITE OPERATION
Data written successfully.

2. READ OPERATION
Hello, this is a Python file.
This is an example of file handling.

3. READLINE() OPERATION
Hello, this is a Python file.

4. READLINES() OPERATION
['Hello, this is a Python file.\n', 'This is an example of file handling.']

5. READ FILE LINE BY LINE
Hello, this is a Python file.
This is an example of file handling.

6. APPEND OPERATION
Data appended successfully.

7. WRITE OPERATION
Data written to newfile.txt successfully.

All file handling operations completed.
"""