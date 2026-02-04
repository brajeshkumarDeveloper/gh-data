import os
import mysql.connector
from mysql.connector import Error

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

if not all([host, user, password, database]):
    raise SystemExit(
        "Missing required env vars: "
        "DB_HOST, DB_USER, DB_PASSWORD, DB_NAME"
    )

conn = None
cursor = None
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    for row in cursor:       # iterate rows safely
        print(row)
except Error as e:
    print("DB error:", e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
