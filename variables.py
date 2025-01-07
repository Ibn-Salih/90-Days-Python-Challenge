# Project:
# - Create a program that takes user input for their name and age, then prints a greeting with their name and calculates the year they were born.

name = (input("Enter your name: ")) #Takes user input for their name
age = int((input("Enter your age: ")))
current_year = int((input("Enter the current year: "))) 
year_of_birth = current_year - age # calculates the year of birth of the user

print(f"Hello {name}, you were born in the year {year_of_birth}.")
