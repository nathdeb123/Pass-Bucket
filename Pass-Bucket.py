import secrets, string

def gen_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}<>?"
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length (default 10): ") or 10)
    count = int(input("How many passwords to generate? (default 1): ") or 1)

    for i in range(count):
        print(f"Password {i+1}:", gen_password(length))
