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

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

mycursor = mydb.cursor()

# Placeholder to prevent injection
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
