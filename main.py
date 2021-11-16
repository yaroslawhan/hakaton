import telebot, random
from telebot import types
from fuzzywuzzy import fuzz
import time


bot = telebot.TeleBot('2115882328:AAFxgL0uHGtc4tKqlB9_EtScnqyZeO_CLDk')
sTime = 0 #cтартовое время
text = "" #текст, который будет
isTraining = False
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
        ratio = fuzz.ratio(message.text, text)

        errorsText = ""
        if(ratio == 100):
            errorsText = "ошибок нет✔️"
        else:
            errorsText = "совпадение: " + str(ratio) + "% ❌"

        rTime = round(time.time() - sTime, 1) #результат времемени
        charsPerSecond = round(len(message.text)/rTime, 1)

        timeText = "Символы в секунду: " + str(charsPerSecond)
        if charsPerSecond >= 1.5:
            timeText += " ✔"
        else:
            timeText += " ❌"

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