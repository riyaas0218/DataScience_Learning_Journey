
from cryptography.fernet import Fernet
from password_utilis import encrypt_password

def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as f:
        f.write(key)

    print("New Fernet key generated successfully!")

if __name__ == "__main__":
    encrypted = encrypt_password("Root")
    print("Encrypted password:")
    print(encrypted.decode())

