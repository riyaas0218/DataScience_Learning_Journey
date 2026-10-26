from cryptography.fernet import Fernet


#class to prevent accidental print/log of password

class FakeStr(str):
    def __str__(self):
        return "password print pannathee"
    def  __repr__(self):
        return "passeord paakathee"


#Load the secret key
def load_key():
    return open("secret.key","rb").read()

#Encrypt the plain password

def encrypt_password(password):
    key = load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())

#Decrypt the password and retrunr a proteccted string


def decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)