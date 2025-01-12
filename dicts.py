# Topics:
# - Learn about dictionaries (key-value pairs) and sets (unordered collections).
# - Dictionary methods: get(), keys(), values().
# - Project:
# - Create a program that stores user information (name, age) in a dictionary 
# and allows the user to retrieve it by providing the name.


name = input("Enter your name: ")
age = int(input("Enter your age: "))

user_info = {"name": name,"age": age}

user_name = input("Enter your name: ")

if user_name in user_info.values():
    print(f"Name: {user_info['name']}, Age: {user_info['age']}")
else:
    print("User not found. Please try again.")

