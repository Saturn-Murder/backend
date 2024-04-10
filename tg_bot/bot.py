import telebot
import sqlite3
from telebot import types



bot = telebot.TeleBot('7079792810:AAE7N2lW5wRPOhLOWPE40sK72pUO2Rz3-d8')
con = sqlite3.connect('bot_database.db')
cursor = con.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               user_id INTEGER UNIQUE,
               name TEXT NOT NULL,
               status varchar(50))
            """)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("0", callback_data="0")
    item2 = types.InlineKeyboardButton("1", callback_data="1")
    item3 = types.InlineKeyboardButton("2", callback_data="2")
    item4 = types.InlineKeyboardButton("3", callback_data="3")
    item5 = types.InlineKeyboardButton("4", callback_data="4")
    item6 = types.InlineKeyboardButton("5", callback_data="5")
    markup.add(item1, item2, item3, item4, item5, item6)
    con = sqlite3.connect('bot_database.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO users (user_id, name, status) VALUES (?, ?, ?)", (message.from_user.id, message.from_user.username, 'user'))
    con.commit()
    cursor.execute("SELECT status FROM users WHERE user_id = (?)", (message.from_user.id,))
    status = cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()
    if status == "user":
        bot.send_message(message.chat.id, f'Привет {message.from_user.username}. Пожалуйста, оцените качество обслуживания:', reply_markup=markup)
    else:
        return
    

bot.polling(none_stop=True)

