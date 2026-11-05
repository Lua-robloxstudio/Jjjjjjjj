import telebot
from config import token

bot = telebot.TeleBot(token)

from logic import generate_image

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Генерирую картинки")



@bot.message_handler(func=lambda message: True)
def send_message(message):
    data = generate_image(message.text)
    if data == "Не удалось нарисовать шедевр":
        bot.send_message(message.chat.id, data)
    else:
        with open(data, "rb") as photo:
            bot.send_photo(message.chat.id, photo)


bot.infinity_polling()