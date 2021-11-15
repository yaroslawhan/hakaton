import telebot, random
from telebot import types
import time
import math

bot = telebot.TeleBot('2115882328:AAFxgL0uHGtc4tKqlB9_EtScnqyZeO_CLDk')
sTime = 0 #cтартовое время
text = "" #текст, который будет
isTraining = False
sPerChar = 0.6 #секунды за символы
isWorking = True


@bot.message_handler(content_types=['text'])
def start(message):
    global isTraining
    global text
    global isWorking

    #начало
    if (message.text == "/start" or message.text == "Привет" or message.text == "привет") and isTraining == False:
        messages = ['Вас приветствует лучший в мире бот для тренировки печати!', 'Hello, World!', 'Здравствуйте!', 'Привет, человек по ту сторону экрана.', 'С Наступающим Новым Годом!']
        i = random.randrange(0, 4)
        keyboard = types.InlineKeyboardMarkup()
        #key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        #keyboard.add(key_settings);
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        bot.send_message(message.from_user.id, "{} Пожалуйста, выберите действие.".format(messages[i]), reply_markup = keyboard)

    if(message.text == "/quit"):
        print(123)
        bot.stop_bot()

    #если выводен текста
    if (isTraining):
        isTraining = False

        #проверка на ошибки
        errors = 0
        l = 0

        if len(message.text) < len(text):
            l = len(message.text)
            errors = len(text) - len(message.text)

        else:
            l = len(text)
            errors += len(message.text) - len(text)

        for i in range(0, l):
            if (text[i] != message.text[i]):    
                errors+=1

        errorsText = ""
        if(errors == 0):
            errorsText = "ошибок нет✔️"
        else:
            errorsText = "ошибок: " + str(errors) + "❌"

        rTime = time.time() - sTime #результат времемени
        dTime = len(text) * sPerChar #желательное время

        timeText = "Время: " + str(math.floor(rTime))
        if(rTime <= dTime):
            timeText += "с ✔️"
        else:
            timeText += "с ❌"

        bot.send_message(message.chat.id, timeText + ", " + errorsText)
        

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global isTraining
    global sTime
    global text

    if call.data == "go":
        text = 'Мой первый друг, мой друг бесценный!'

        sTime = time.time()
        isTraining = True

        bot.send_message(call.message.chat.id, 'Напечатайте данный текст как можно быстрее:')
        bot.send_message(call.message.chat.id, text)

        #bot.send_message(message.from_user.id, 'Слов напечатано: {} из {}.'.format(len(message.text.split()), letters))
        #if texts == message.text:
            #bot.send_message(call.message.chat.id, 'Всё верно!')

bot.polling(none_stop=isWorking, interval=0)