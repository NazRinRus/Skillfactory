import telebot

TOKEN = '5919391778:AAGixM5Bu55xhkX_qA6N_6W9QiRwC1nf72k'

bot = telebot.TeleBot(TOKEN)
'''
# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f"Приветствую, {message.chat.username}")


'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)