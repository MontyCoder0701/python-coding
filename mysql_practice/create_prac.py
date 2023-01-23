import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database="mydatabase"
)

mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

# mycursor.execute(
#     "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

mycursor.execute(
    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
