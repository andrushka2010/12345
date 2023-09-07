import sqlite3 as sq

with sq.connect('saper2.db') as con:
    cur = con.cursor() #cursor

    cur.execute('DROP TABLE IF EXISTS students')
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
    users_id INTEGER,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER
    )""")

    cur.execute('DROP TABLE IF EXISTS marks')
    cur.execute("""CREATE TABLE IF NOT EXISTS marks (
         id TEXT NOT NULL,
         subject INTEGER,
         mark INTEGER
         )""")
