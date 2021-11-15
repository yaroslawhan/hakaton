import telebot, random
from telebot import types
import time

bot = telebot.TeleBot('2115882328:AAFxgL0uHGtc4tKqlB9_EtScnqyZeO_CLDk')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start" or message.text == "Привет" or message.text == "привет":
        messages = ['Вас приветствует лучший в мире бот для тренировки печати!', 'Hello, World!', 'Здравствуйте!', 'Привет, человек по ту сторону экрана.', 'С Наступающим Новым Годом!']
        i = random.randrange(0, 4)
        keyboard = types.InlineKeyboardMarkup()
        #key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        #keyboard.add(key_settings);
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        bot.send_message(message.from_user.id, "{} Пожалуйста, выберите действие.".format(messages[i]), reply_markup = keyboard)
        

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "go":
        texts = ['Мой первый друг, мой друг бесценный!']
        letters = ['6']
        bot.send_message(call.message.chat.id, 'Напечатайте данный текст как можно быстрее:')
        time.sleep(1)
        bot.send_message(call.message.chat.id, texts)
        bot.send_message(call.message.chat.id, 'Времени осталось: 5 секунд')
        time.sleep(5)
        bot.send_message(call.message.chat.id, 'Время вышло!')
        #bot.send_message(message.from_user.id, 'Слов напечатано: {} из {}.'.format(len(message.text.split()), letters))
        #if texts == message.text:
            #bot.send_message(call.message.chat.id, 'Всё верно!')

bot.polling(none_stop=True, interval=0)