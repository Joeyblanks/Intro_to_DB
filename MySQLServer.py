import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',      # Change to your MySQL username if different
        password='passwd'       # Change to your MySQL password if set
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
    except NameError:
        pass

