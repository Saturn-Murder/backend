import sqlite3


def login():
    return input("Введите логин: ")


def reg():
    while True:
        favor = input("Придумайте пароль: ")
        cap = 0
        low = 0
        dig = 0
        for i in favor:
            if i.isupper() is True:
                cap += 1
        for i in favor:
            if i.islower() is True:
                low += 1
        for i in favor:
            if i.isdigit() is True:
                dig += 1
        if cap == 0:
            print("В пароле должна быть хотя бы одна заглавная буква!")
        elif low == 0:
            print("В пароле должна присутствовать хотя бы одна прописная буква!")
        elif dig == 0:
            print("В пароле должна присутствовать хотя бы одна цифра!")
        else:
            break
    return favor


def entrance():
    return input("Введите пароль: ")


con = sqlite3.connect("localhost.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                login TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)
            """)
acc = []
new = []
first = input("Добро пожаловать! Вы хотите войти или зарегистрироваться? ")
if first.lower() == "войти":
    acc.insert(0, login())
    acc.insert(1, entrance())
    for i in acc:
        try:
            cursor.execute("INSERT INTO accounts VALUES(?, ?, ?)", (None, acc[0], acc[1]))
            break
        except sqlite3.IntegrityError:
            print("Добро пожаловать!")
            cursor.execute("SELECT * FROM accounts")
            print(cursor.fetchall())
            break
elif first.lower() == "зарегистрироваться":
    new.insert(0, login())
    new.insert(1, reg())
    for i in new:
        try:
            cursor.execute("INSERT INTO accounts VALUES(?, ?, ?)", (None, new[0], new[1]))
            print("Вы успешно зарегистрировались!")
            cursor.execute("SELECT * FROM accounts")
            print(cursor.fetchall())
            break
        except sqlite3.IntegrityError:
            print("Такой аккаунт уже существует! Вам нужно войти в аккаунт!")
            break

