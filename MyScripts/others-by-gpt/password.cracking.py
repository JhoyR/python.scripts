import hashlib

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def dictionary_attack(username, hashed_password, dictionary):
    for word in dictionary:
        if hashed_password == hash_password(word, username):
            return word
    return None

# Exemplo de uso:
username = "john_doe"
hashed_password = "5a36a992aed1e7a5572b9c2ccff6e5d357e94c3af3a2570d30e67e7d67ecf7b1"
common_passwords = ["password", "123456", "qwerty"]

cracked_password = dictionary_attack(username, hashed_password, common_passwords)
if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found in dictionary.")
