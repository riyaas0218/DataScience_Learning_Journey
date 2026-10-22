import pymysql


connection= pymysql.connect(
    host='localhost',
    user='root',
    password='Root',
    database='testdb',
    cursorclass=pymysql.cursors.DictCursor

)
try:
    with connection.cursor() as cursor:

        # Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees1 (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                department VARCHAR(100)
            )
        """)

        # Insert records
        insert_query = """
            INSERT INTO employees1 (name, department)
            VALUES (%s, %s)
        """

        values = [
            ("John", "IT"),
            ("Riyas", "DS"),
            ("Ajim", "Support"),
            ("Asiga", "HR")
        ]

        cursor.executemany(insert_query, values)
        connection.commit()

        # Retrieve records
        cursor.execute("SELECT * FROM employees1")
        result = cursor.fetchall()

        # for row in result:
            # print(row)
        with open("employees1_output.txt","w") as file:
            for row in result:
                file.write(f"{row}\n")

finally:
    connection.close()