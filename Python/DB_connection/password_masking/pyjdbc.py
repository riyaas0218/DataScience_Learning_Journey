import pymysql

def connect_to_mysql():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Root",
        database="testdb"
    )

    print("Connected to MySQL successfully!")
    conn.close()

if __name__ == "__main__":
    connect_to_mysql()