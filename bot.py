from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("7184779982:AAG-uDGut-KTNd4lL7xRgi_cRWn4qQL6HmQ")

# @bot.message_handler(commands=["start", "help"])
# def start(message: Message):
#     chat_id = message.chat.id
#     full_name = message.from_user.full_name
#     bot.send_message(chat_id, f"Assalomu alaykum {full_name} help")
#
#     print(message)
#     print(id)



@bot.message_handler(content_types=["text"])
def start(message: Message):
    chat_id = message.chat.id
    bot.copy_message(chat_id, chat_id, message.message_id)

bot.polling()
