import sqlite3

conn = sqlite3.connect("./SQL_DDL.db")
cur = conn.cursor()

INSERT_SQL = "INSERT INTO item(code, name, price) VALUES (?, ?, ?)"

data = (
    ("A0001", "게이밍마우스", 38000),
    ("1233", "노트북", 28999),
    ("645456", "키보드", 10999),
)

cur.executemany(INSERT_SQL, data)

conn.commit()
conn.close()
