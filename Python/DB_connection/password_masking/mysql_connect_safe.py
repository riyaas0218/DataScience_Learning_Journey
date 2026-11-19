
import pymysql
from password_utilis import decrypt_password

# Encrypted password copied from encrypt_once.py
ENCRYPTED_PASSWORD = b"gAAAAABq33DC0aPb0tHmFhkICU8hdV9uVe1KjmqhMc9Ynzz0qqZSlWZkNNbIE9Q7vst2e9tsNx9lyBv1Oxu7n8ei0O1QPvk7XA=="


def connect_to_mysql():
    password = decrypt_password(ENCRYPTED_PASSWORD)

    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password=str.__str__(password),
            database="testdb"
        )

        print("Connected to MySQL successfully!")

        connection.close()

    except pymysql.MySQLError as error:
        print("MySQL connection failed:", error)


if __name__ == "__main__":
    connect_to_mysql()
