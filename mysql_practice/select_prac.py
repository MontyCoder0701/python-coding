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

# mycursor.execute("SELECT * FROM customers")
mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()
myresult = mycursor.fetchone()

for x in myresult:
    print(x)
