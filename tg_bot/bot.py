import telebot
from telebot import types
import sqlite3

con = sqlite3.connect("bot_database.db")
cursor = con.cursor()
TOKEN = '6227029117:AAH_hpycXzA1-QIXggh2COl99fcP1JAUJ70'
bot = telebot.TeleBot(TOKEN)

cursor.execute("""CREATE TABLE IF NOT EXISTS people
                (primary_id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_id INTEGER UNIQUE, 
                coins INTEGER DEFAULT 0,
                exp INTEGER DEFAULT 0,
                level INTEGER DEFAULT 0)
            """)

@bot.message_handler(commands=["start"])
def start_message(message):
    con = sqlite3.connect("bot_database.db")
    cursor = con.cursor()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_item = types.KeyboardButton("Main menu")
    markup.add(main_item)
    bot.send_message(message.chat.id, "Hello!", reply_markup=markup)
    cursor.execute("INSERT INTO people (user_id) VALUES (?)", (message.from_user.id,))
    con.commit()


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, "help me")


@bot.message_handler(commands=["ref"])
def ref_message(message):
    bot.send_message(message.chat.id, f"t.me/@Test_dovi_bot?start={message.from_user.id}")


@bot.message_handler(content_types=['text'])
def text_reply(message):
    con = sqlite3.connect("bot_database.db")
    cursor = con.cursor()
    if message.text == "Main menu":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_1 = types.KeyboardButton("Buy")
        item_2 = types.KeyboardButton("Support")
        item_3 = types.KeyboardButton("Profile")
        markup2.add(item_1, item_2, item_3)
        bot.send_message(message.chat.id, "Main  menu: \n Buy: ... \n Support: ... \n Profile: ...",
                         reply_markup=markup2)
    if message.text == "Profile":
        try:
            cursor.execute("SELECT coins,exp,level FROM people WHERE user_id = (?)", (message.from_user.id,))
            coins, exp, level = cursor.fetchone()
            bot.send_message(message.chat.id, str(f'Nickname: {message.from_user.username}\nCoins: {coins}\nExp: {exp}\nLevel: {level}'))
            con.commit()
        except sqlite3.IntegrityError:
            return



con.commit()
bot.infinity_polling()
