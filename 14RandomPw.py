# Password Random Generator

import random, string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = uppercase + lowercase + digits + special_chars
    password += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password)

    return ''.join(password)

try:
    leght = int(input("Masukkan panjang password: "))
    password = generate_password(leght)
    print("Generated Password:", password)

except ValueError as e:
    print(e)