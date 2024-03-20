import sqlite3


def login():
    return input("Введите логин: ")
    


def password():
    while True:
        favor = input("Введите пароль: ")
        if len(favor) < 6:
            print("Пароль слишком маленький, хотя бы 6 символов")
        else:
            break
    return favor


con = sqlite3.connect("localhost.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS reg
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                login TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)
            """)

users = [login(), password()]
for i in users:
    try:
        cursor.execute("INSERT INTO reg VALUES(?, ?, ?)", (None, users[0], users[1]))
        break
    except sqlite3.IntegrityError:
        print("Такой аккаунт уже существует!") 
        break

con.commit()

