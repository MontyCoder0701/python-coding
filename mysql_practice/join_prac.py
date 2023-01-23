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
# sql = "DROP TABLE IF EXISTS users"
# mycursor.execute(sql)

# mycursor.execute(
#     "CREATE TABLE users (name VARCHAR(255), fav INT)")
# mycursor.execute(
#     "ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#     ('John', 154),
#     ('Peter', 154),
#     ('Amy', 155),
# ]
# mycursor.executemany(sql, val)
# mycursor.execute(
#     "INSERT INTO users (name, fav) VALUES('Hannah', NULL);")
# mycursor.execute(
#     "INSERT INTO users (name, fav) VALUES('Michael', NULL);")
# mydb.commit()

# mycursor.execute(
#     "CREATE TABLE products (id INT, name VARCHAR(255))") # Return only when there is match
# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [
#     (154, 'Chocolate Heaven'),
#     (155, 'Tasty Lemons'),
#     (156, 'Vanilla Dreams'),
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

# sql = "SELECT \ # Return all users
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# sql = "SELECT \ # Return all products
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
