import hashlib

# Dictionary of users and hashed passwords (stored securely in production)
user_database = {
    "alice": hashlib.md5("password1".encode()).hexdigest(),
    "bob": hashlib.md5("secret123".encode()).hexdigest(),
}

# Dictionary of users and MFA codes
mfa_database = {
    "alice": "123456",
    "bob": "987654",
}

# Function to authenticate a user
def authenticate(username, password, mfa_code):
    if username not in user_database:
        print("User not found.")
        return

    stored_password = user_database[username]
    if hashlib.md5(password.encode()).hexdigest() != stored_password:
        print("Incorrect password.")
        return

    if username not in mfa_database or mfa_database[username] != mfa_code:
        print("Incorrect MFA code.")
        return

    print("Authentication successful.")

# User input
username = input("Username: ")
password = input("Password: ")
mfa_code = input("MFA code: ")

# Call the authenticate function
authenticate(username, password, mfa_code)