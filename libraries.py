# - Topics:
# - Introduction to Python libraries: how to install and use them (using pip).
# - Using built-in libraries like os, sys, math.
# - Project:
# - Write a Python script that calculates the square root of a number 
# using the math library.

import math
# Get a number from the user
num = int(input("Enter a number: "))

# Calculate the square root
square_root = math.sqrt(num)

# Print the result
print(f"The square root of {num} is: {square_root}")
