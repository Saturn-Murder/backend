import sqlite3


def password():
    while True:
        favor = int(input("Введите пароль: "))
        if len(str(favor)) < 6:
            print("Пароль слишком маленький, хотя бы 6 символов")
        else:
            break
    return favor


con = sqlite3.connect("localhost.db")
cursor = con.cursor()
cursor.execute("INSERT INTO password (password) VALUES (?)", (password(),))
con.commit()
print("Ваш пароль сохранён =)")
