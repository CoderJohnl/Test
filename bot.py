from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("7184779982:AAG-uDGut-KTNd4lL7xRgi_cRWn4qQL6HmQ")
@bot.message_handler(func=lambda message: True if message.text else False)
def text_handler(message: Message):
    chat_id = -1002136578167
    bot.send_message(chat_id, message.text)

# Rasm uchun handler
@bot.message_handler(content_types=["photo"])
def photo_handler(message: Message):
    chat_id = -1002136578167
    bot.send_photo(chat_id, message.photo[-1].file_id)
@bot.message_handler(content_types=["video"])
def video_handler(message: Message):
    chat_id = -1002136578167
    bot.send_video(chat_id, message.video.file_id)
@bot.message_handler(content_types=["animation"])
def animation_handler(message: Message):
    chat_id = -1002136578167
    bot.send_animation(chat_id, message.animation.file_id)

bot.polling()
