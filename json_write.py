#Topics:
#  Learn how to parse and create JSON data using Python’s json library.
#  Understanding JSON format and how it is used in APIs.
#  Project:
#  Create a script that reads a JSON file and 
# prints out specific values based on user input.

import json

user_info = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

with open("data.json", "w") as file:
    json.dump(user_info, file)

with open("data.json", "r") as file:
    data = json.load(file)

user_name = input("Enter the name of the person: ")

if user_name ==  data["name"]:
    print("User info found\n")
    print("----------------------------\n")
    print(f"Name: {data["name"]}\n")
    print(f"Age: {data["age"]}\n")
    print(f"City: {data["city"]}\n")
else:
    print("User info not found")