import re

text = input("Enter a text: ")

emails = re.findall(r'\w+@\w+\.\w+', text)

if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email addresses found.")

#Output
"""
Enter a text: Contact us at abc@gmail.com or xyz@yahoo.com.
Email addresses found:
abc@gmail.com
xyz@yahoo.com
"""