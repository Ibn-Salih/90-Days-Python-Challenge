# Build a simple age checker: Ask the user for their age 
# and tell them 
# if they are eligible for certain services 
# (e.g., "You are eligible to vote" or "You are too young to vote").


age = int(input("How old are you: "))

if age >= 18:
    print ("You are eligible to vote.")
elif age < 18 and age > 10:
    waiting_years = 18 - age
    print (f"You are not eligible to vote, come back in {waiting_years} years time.")
else:
    print ("Go and sleep!!!!!!!!")
