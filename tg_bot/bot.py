import telebot
from telebot import types
import sqlite3


bot = telebot.TeleBot('6417408484:AAENEqwykRLTar_lCauXZMuTOI5BkglQ6yk')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                   name varchar(50), 
                   pass varchar(50), 
                   coins INTEGER DEFAULT 0, 
                   exp INTEGER DEFAULT 0, 
                   level INTEGER DEFAULT 0)
                """)
    con.commit()
    cursor.close()
    con.close()
    bot.send_message(message.chat.id, "Здравствуйте! Для регистрации назовите своё имя:")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Введите пароль:")
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password,))
    con.commit()
    cursor.close()
    con.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_item = types.KeyboardButton("Главное меню")
    markup.add(main_item)
    bot.send_message(message.chat.id, "Вы успешно зарегистрировались!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_reply(message):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    if message.text == "Главное меню":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Создатели')
        item2 = types.KeyboardButton('Поддержка')
        item3 = types.KeyboardButton('Профиль')
        markup2.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Создатели: ...\nПоддержка: ...\nПрофиль: ...", reply_markup=markup2)
    if message.text == "Профиль":
        cursor.execute("SELECT * FROM users WHERE name = (?)", (name,))
        users = cursor.fetchall()
        info = ''
        for el in users:
            info += f'Имя: {el[1]}\nПароль: {el[2]}\nМонеты: {el[3]}\nОпыт: {el[4]}\nУровень: {el[5]}'
        bot.send_message(message.chat.id, info)



bot.polling(none_stop=True)
