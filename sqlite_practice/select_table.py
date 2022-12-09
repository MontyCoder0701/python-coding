import sqlite3

conn = sqlite3.connect("SQL_DDL.db")
cur = conn.cursor()

SELECT_SQL = "SELECT * FROM item LIMIT 2;"

cur.execute(SELECT_SQL)
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
