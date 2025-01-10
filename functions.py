# Write a function that takes a number as input
#  and returns the factorial of that number.

def factorial(n): # where n can be any positive integer
    if n == 0: 
        return 1
    else:
        return n * factorial(n-1)


num = int(input("Enter a number: "))
result =(factorial(num))
print(f"The factorial of {num} is: {result}")