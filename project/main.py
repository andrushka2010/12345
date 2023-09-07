import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor() #cursor

    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

    cur.execute('DROP TABLE IF EXISTS games')
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
         user_id TEXT NOT NULL,
         score INTEGER,
         time INTEGER
         )""")

