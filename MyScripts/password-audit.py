# List of passwords to be verified
passwords = [
    "password123!",
    "senha123!",
    "securePassword123!",
    "MinhaSenhaSuperSegura123#",
    "12345",
    "qwerty",
    "abc123",
    "abc123def#@!",
]

# Function to check if a password meets the minimum length requirement
def has_minimum_length(password, min_length=8):
    """Check if the password has the minimum length required."""
    return len(password) >= min_length

# Function to check if a password contains only numbers
def is_numeric(password):
    """Check if the password contains only numbers."""
    return password.isnumeric()

# Function to check if a password contains only letters
def is_alphabetic(password):
    """Check if the password contains only letters."""
    return password.isalpha()

# Function to check if a password contains both letters and numbers
def has_letters_and_numbers(password):
    """Check if the password contains both letters and numbers."""
    return any(char.isalpha() for char in password) and any(char.isdigit() for char in password)

# Function to verify the strength of a password
def verify_password_strength(password):
    """Verify the strength of the given password."""
    if not has_letters_and_numbers(password):
        return "weak (must contain both letters and numbers)"
    if not has_minimum_length(password):
        return "weak (minimum length is 8 characters)"
    return "strong"

# Verify the strength of each password in the list
for password in passwords:
    strength = verify_password_strength(password)
    print(f"The password '{password}' is considered {strength}.")
