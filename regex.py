# - Topics:
# - Introduction to the re library.
# - Basic regex syntax: \d, \w, \s, +, *, ?.
# - Project:
# - Build a program that validates email addresses using regular expressions.

import re

email = input("Please enter your email address:")

#validate user input by comparing it to the pattern specified
pattern = r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"

def validate_email():
    if re.match(pattern, email):
        return True
    else:
        return False
    
validator = validate_email()

if validator is True:
    print ("Email validation successful")
else:
    print("Invalid email")