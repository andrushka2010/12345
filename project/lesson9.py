import sqlite3 as sq

cars = [
    ('Audi', 52636),
    ('Mercedes', 18911),
    ('Opel', 73811),
    ('BMW', 92811),
    ('Skoda', 21123),
    ('Volvo', 12000),
]

with sq.connect('saper2.db') as con:
    cur = con.cursor() #cursor

    cur.execute('DROP TABLE IF EXISTS cars')
    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER 
    )""")

    for car in cars:
        cur.execute("INSERT INTO cars VALUES(NULL, ?,?)", car)