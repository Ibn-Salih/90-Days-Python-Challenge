# - Topics:
# - Learn how to evaluate password strength and detect weak passwords.
# - Project:
# - Write a Python script that checks the strength of a password by evaluating 
# - its length, use of special characters, and common patterns.


import re

# List of common passwords (add more as needed)
COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "admin", "letmein", "welcome", "123123", "123456789"
]

def check_length(password):
    """Check if the password meets minimum length requirements."""
    return len(password) >= 8

def check_character_types(password):
    """Check if the password contains uppercase, lowercase, digits, and special characters."""
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    return has_upper, has_lower, has_digit, has_special

def check_common_passwords(password):
    """Check if the password is in the list of common passwords."""
    return password.lower() in COMMON_PASSWORDS

def evaluate_password_strength(password):
    """Evaluate the strength of a password."""
    # Check length
    if not check_length(password):
        return "Weak: Password must be at least 8 characters long."
    
    # Check character types
    has_upper, has_lower, has_digit, has_special = check_character_types(password)
    if not all([has_upper, has_lower, has_digit, has_special]):
        return "Weak: Password must include uppercase, lowercase, digits, and special characters."
    
    # Check for common passwords
    if check_common_passwords(password):
        return "Weak: Password is too common."
    
    # Check for patterns (e.g., sequences, repeated characters)
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        return "Weak: Password contains repeated characters."
    if re.search(r'(123|abc|qwe)', password.lower()):  # Common sequences
        return "Weak: Password contains common sequences."
    
    # If all checks pass, the password is strong
    return "Strong: Password meets all strength requirements."

def main():
    password = input("Enter a password to evaluate: ").strip()
    result = evaluate_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()