import telebot

TOKEN = '729880369:AAHGezH-nJDfkjVAvEOw4-3WI2EK6e3C58I' # токен вашего бота, полученный от @BotFather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id,"Я могу делать много чего интересного но это в будущем! Пока что ты можешь говорить мне 'привет' и 'пока'")

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id,
                     "Hey man! My name is Kasya.")
    user_markup = telebot.types.ReplyKeyboardMarkup(True , False)
    user_markup.row('/start' , '/stop' , '/register_user')

@bot.message_handler(content_types=["text"])
def handle_all_text(message):
    if(message.text.lower() is "привет"):
        bot.send_message(message.chat.id , "Привет ! Я бот Кася")
    elif (message.text.lower() == "пошел"):
        bot.send_message(message.chat.id, "Ты?!!")
    else:
        bot.send_message(message.chat.id , "Я не понимаю данную команду (")

bot.polling(none_stop=True, interval=0)