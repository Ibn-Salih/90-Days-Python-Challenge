# Topics:
# - Learn how to use try, except, and finally for error handling.
# - Handling specific exceptions like ValueError, FileNotFoundError.
# - Project:
# - Create a program that takes user input for a number and 
# catches errors if the user inputs something invalid (non-integer).

print("Calculate your intrest")
print("_"*20)

try:
    principal = int(input("Enter a principal amount: "))
    rate = float(input("Enter a rate of intrest: "))
    time = int(input("Enter a time frame in year: "))
except ValueError as e:
    print("Enter an integer value")

simple_intrest = (principal * rate * time) / 100
print(f"Your intrest amount is GHS{simple_intrest}0")





