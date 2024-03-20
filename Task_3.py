import sqlite3


def login():
    while True:
        log = int(input("Введите почту для регистрации: "))
        if str(log).find("@") == 0:
            print("Почта должна содержать @")
        else:
            break
    return log


con = sqlite3.connect("localhost.db")
cursor = con.cursor()
con.commit()
