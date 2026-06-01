import string

def check_password_strength(password):
    # Requirement: Length Verification (Minimum 8 characters)
    length_criteria = len(password) >= 8
    
    # Requirement: Check for digits
    has_digit = any(char.isdigit() for char in password)
    
    # Requirement: Check for uppercase letters
    has_upper = any(char.isupper() for char in password)
    
    # Requirement: Check for symbols (punctuation)
    has_symbol = any(char in string.punctuation for char in password)

    # Logic to determine strength
    score = sum([length_criteria, has_digit, has_upper, has_symbol])

    if score <= 1:
        return "Weak"
    elif score == 2 or score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"

# User Input and Output
user_password = input("Enter a password to check its strength: ")
strength = check_password_strength(user_password)

print(f"Password Strength: {strength}")
