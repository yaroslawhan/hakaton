import telebot;
bot = telebot.TeleBot('2115882328:AAFxgL0uHGtc4tKqlB9_EtScnqyZeO_CLDk');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "")

bot.polling(none_stop=True, interval=0)