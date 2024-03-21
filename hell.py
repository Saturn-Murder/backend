import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()

base.execute(
    'CREATE TABLE IF NOT EXISTS users '
    '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
    ' login TEXT NOT NULL UNIQUE,'
    ' password TEXT NOT NULL)')
base.commit()

users = [['jonny123', '123456']]

for user in users:
    try:
        cur.execute('INSERT INTO users VALUES(?, ?, ?)', (None, user[0], user[1]))
    except sqlite3.IntegrityError as err:
        print(f"Database error: {err}")

base.commit()
