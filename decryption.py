# - Topics:
# - Understand how weak encryption algorithms can be cracked (e.g., brute-force AES).
# - Project:
# - Write a script that attempts to break weak encryption algorithms 
# - by trying different key combinations.


from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

# Sample ciphertext and IV (replace with your target data)
# To generate: Encrypt "Secret Message" with password "123"
iv = b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10'
ciphertext = b'\x9d\x83\xa4\x1e\xb5\xa0\xc6\x8a\x7f\x12\x45\x6c\x38\xd1\xf9\xdb'

def brute_force_aes(wordlist):
    for password in wordlist:
        # Derive key from password (weak method: SHA256 of password)
        key = hashlib.sha256(password.encode()).digest()
        
        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
            
            # Check for valid plaintext (ASCII printable characters)
            if decrypted.isascii() and decrypted.decode().isprintable():
                print(f"Success! Password: '{password}' | Decrypted: {decrypted.decode()}")
                return
        except (ValueError, UnicodeDecodeError):
            continue
    
    print("No valid decryption found.")

# Limited wordlist for demonstration (add more entries)
wordlist = ["123", "password", "admin", "letmein", "test"]
brute_force_aes(wordlist)