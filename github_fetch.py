# - Topics:
# - Learn how to send requests and handle JSON responses from APIs.
# - Authentication methods for APIs (e.g., using API keys).
# - Project:
# - Write a program that interacts with the GitHub API 
# to fetch user data (like profile information).

import requests, json

def get_user_profile():
    username = input("Enter GitHub username: ")
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"User Id: {user_data['id']}")
        print(f"Name: {user_data['name']}")
        print(f"Bio: {user_data['bio']}")
        print(f"URl: {user_data['url']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Location: {user_data['location']}")
    else:
        print (f"Error: {response.status_code} User not found")

    

# get_user_profile()
user_info = get_user_profile()
print(user_info)






