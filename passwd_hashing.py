# - Topics:
# - Introduction to hashing with the hashlib library.
# - Hashing algorithms: MD5, SHA1, SHA256.
# - Project:
# - Write a Python script that hashes a user’s password
# - and compares it to a known hash.

import hashlib, secrets, string


# Define the length of the salt (e.g., 16 bytes)
# salt = secrets.token_bytes(16)
# print(salt)  # Raw bytes

def user_password(): # Takes user passwd and salt
    password = input("Enter your password:")
    salt = string.ascii_letters + string.digits + password
    salting = (secrets.choice(salt) for i in range(7))
    salted_password_1 = password + str(salting)
    return salted_password_1,salting



def new_password(salting):
    second_passwd = input('Enter password: ')
    salted_password_2 = second_passwd + str(salting)
    return salted_password_2

def generate_hash(salted_password_1, salted_password_2):
    passwd_hasher_1 = hashlib.blake2b(salted_password_1.encode()).hexdigest()
    passwd_hasher_2 = hashlib.blake2b(salted_password_2.encode()).hexdigest()
    
    if passwd_hasher_1 == passwd_hasher_2:
        print("Passwords match successfull")
    else:
        print("Password do not match")

    print(f"Password_1 hash: {passwd_hasher_1}")
    print(f"Password_2 hash: {passwd_hasher_2}")


if __name__ == "__main__":
    print("Comparing Hash Values")
    print("_"*20)
    salted_password_1, salting = user_password()
    salted_password_2 = new_password(salting)
    generate_hash(salted_password_1, salted_password_2)
