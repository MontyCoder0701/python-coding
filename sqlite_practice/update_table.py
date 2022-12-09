import sqlite3

conn = sqlite3.connect("./SQL_DDL.db")
cur = conn.cursor()

UPDATE_SQL = "UPDATE item set price = 65000 WHERE code = 'A0001'"

cur.execute(UPDATE_SQL)

conn.commit()

conn.close()
