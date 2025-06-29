# File: MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

# Replace these with your MySQL credentials
DB_HOST = "localhost"
DB_PORT = "3306"
DB_USER = "root"
DB_PASSWORD = "890532488"

DB_NAME = "alx_book_store"

def create_database():
    try:
        # Connect to MySQL server (not to any specific database yet)
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Try to create the database
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print("Error: Could not connect to the MySQL server.")
        print(f"Reason: {err}")

if __name__ == "__main__":
    create_database()
