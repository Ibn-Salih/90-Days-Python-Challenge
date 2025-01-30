# Topics:
# - Learn how brute force attacks work.
# - Introduction to itertools for generating combinations.
# - Project:
# - Write a script that attempts to brute-force a password 
# -using a wordlist and hashes it with hashlib.

import hashlib, itertools, string

hsah_algo = {
    32: "md5",
    40: "sha1",
    56: "sha224",
    64: "sha256",
    96: "sha384",
    128: "sha512"
}

# Get the target password hash from the user
target = input("Enter password hash: ").strip()

# Get the hash length
hash_length = len(target)

# Get the possible algorithm based on the hash length
possible_algo = hsah_algo.get(hash_length)
if not possible_algo:
    print("Unsupported hash length")
    exit()

# Set the charset and maximum length for the brute force attack
charset = string.ascii_letters + string.digits
max_length = 4

# Loop through the charset to guess the password
for length in range(1, max_length + 1):
    for candidate in itertools.product(charset, repeat=length) :
        # Join the candidate characters to form a single string
        guess = "".join(candidate)
        # Loop through the possible algorithms to hash the guess
        for algo in possible_algo:
            # Create a hasher object with the algorithm
            hasher = hashlib.new(algo)
            # Update the hasher with the guess
            hasher.update(guess.encode())
            # Check if the hashed guess matches the target
            if hasher.hexdigest() == target:
                print(f"Password found: {guess} | Algorithm: {algo}")
                # Exit the program if a match is found
                exit()
# Print a message if no match is found
print("No match found")

 


