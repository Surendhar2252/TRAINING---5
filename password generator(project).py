import random
import string

def generate_password(length=12, use_special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ""
    all_chars = letters + digits + special_chars

    if length < 3 and use_special_chars:
        raise ValueError("Password length too short to include all character types.")
    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars) if use_special_chars else random.choice(letters + digits)
    ]

    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_special_chars = input("Include special characters (yes/no)? ").strip().lower() == 'yes'
    print(f"Generated Password: {generate_password(length, use_special_chars)}")
