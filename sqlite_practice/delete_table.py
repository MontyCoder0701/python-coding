import sqlite3

conn = sqlite3.connect("./SQL_DDL.db")
cur = conn.cursor()

DELETE_SQL = "DELETE FROM item WHERE code = '1233'"

cur.execute(DELETE_SQL)

conn.commit()

conn.close()
