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
    return print("Ваш пароль сохранён")


def entrance():
    return print("Введите пароль: ")


con = sqlite3.connect("localhost.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                login TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)
            """)


