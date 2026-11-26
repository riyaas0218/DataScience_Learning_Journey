import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root"
    )

    if connection.is_connected():
        print("MySQL connection successful!")

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")

        result = cursor.fetchone()
        print("MySQL Version:", result[0])

        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("MySQL connection failed:", error)