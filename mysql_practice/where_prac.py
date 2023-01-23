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

# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

sql = "SELECT * FROM customers WHERE address = %s"  # Prevent injection by using placeholder
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
