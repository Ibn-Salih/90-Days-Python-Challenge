# - Topics:
# - Learn basic encryption concepts using the cryptography library.
# - Symmetric vs. asymmetric encryption.
# - Project:
# - Create a simple encryption/decryption tool
# - using the cryptography library (e.g., AES encryption).

from cryptography.fernet import Fernet

# Generate a key
def key_generator():
    key = Fernet.generate_key()
    cypher_suite = Fernet(key)
    return key, cypher_suite


# Encrypt a message 
def encrypt_message(message, cypher_suite):
    encrypted_message = cypher_suite.encrypt(message.encode())
    print(f"Encrypted message: {encrypted_message}")
    return encrypted_message

def decrypt_message(message, cypher_suite):
    response = input("Do you want to decrypt the message? (yes/no): ")
    if response.lower() == "yes":
        decrypted_message = cypher_suite.decrypt(message).decode()
        print(f"Decrypted message: {decrypted_message}")
        return decrypted_message
    else:
        print("Message not decrypted Goodbye!!.")


if __name__ == "__main__":
    message = input("Enter message to encrypt: ")
    key, cypher_suite = key_generator()
    encrypted_message = encrypt_message(message, cypher_suite)
    decrypted_message = decrypt_message(encrypted_message, cypher_suite)

