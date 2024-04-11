import telebot
import sqlite3
from telebot import types



bot = telebot.TeleBot('7079792810:AAE7N2lW5wRPOhLOWPE40sK72pUO2Rz3-d8')
con = sqlite3.connect('bot_database.db')
cursor = con.cursor()
status = ''
value = ''
tg_id = None
tg_name = None

cursor.execute("""CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               user_id INTEGER UNIQUE,
               name TEXT NOT NULL,
               mark INTEGER NOT NULL)
            """)

con.commit()
cursor.close()
con.close()


@bot.message_handler(commands=['start'])
def start(message):
    global tg_id, tg_name, status
    tg_id = message.from_user.id
    tg_name = message.from_user.username
    if tg_name == 'Dovi_t':
        status = 'admin'
    else:
        status = 'user'
    bot.send_message(message.chat.id, "Hello")
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_item = types.KeyboardButton("Ебашь!")
    markup2.add(main_item)
    item1 = types.InlineKeyboardButton("0", callback_data="0")
    item2 = types.InlineKeyboardButton("1", callback_data="1")
    item3 = types.InlineKeyboardButton("2", callback_data="2")
    item4 = types.InlineKeyboardButton("3", callback_data="3")
    item5 = types.InlineKeyboardButton("4", callback_data="4")
    item6 = types.InlineKeyboardButton("5", callback_data="5")
    markup.add(item1, item2, item3, item4, item5, item6)
    if status == 'user':
        bot.send_message(message.chat.id, "Оцените качество обслуживания:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Здравствуйте! Хотите посмотреть статистику?", reply_markup=markup2)
        bot.register_next_step_handler(message, per)


def per(message):
    if message.text == "Ебашь!":
        con = sqlite3.connect("bot_database.db")
        cursor = con.cursor()
        cursor.execute("SELECT (name, mark) FROM users")
        name, total = cursor.fetchall()
        bot.send_message(message.chat.id, f'{name}, {total}')
        con.commit()
        cursor.close()
        con.close()



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global value, tg_id, tg_name
    if call.data == "0":
        value = call.data
    elif call.data == "1":
        value = call.data
    elif call.data == "2":
        value = call.data
    elif call.data == "3":
        value = call.data
    elif call.data == "4":
        value = call.data
    elif call.data == "5":
        value = call.data
    con = sqlite3.connect('bot_database.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO users (user_id, name, mark) VALUES (?, ?, ?)", (tg_id, tg_name, value))
    con.commit()
    cursor.close()
    con.close()
    bot.send_message(call.message.chat.id, "Ваша оценка сохранена!")
    


bot.polling(none_stop=True)

