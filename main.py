# -*- coding: utf-8 -*-

import telebot, random, time
from telebot import types
from fuzzywuzzy import fuzz


bot = telebot.TeleBot('2115882328:AAFxgL0uHGtc4tKqlB9_EtScnqyZeO_CLDk')
sTime = 0 #cтартовое время
text = "" #текст, который будет
text_easy_rus = []
text_norm_rus = ["112 год до нашей эры был годом до-юлианского римского календаря. В то время он был известен как Год консульства Друза и Цезонина и Пятый год Юандинга.", "Амбавади-это район, расположенный в Ахмадабаде, Индия. Основными достопримечательностями этого района являются Центральный торговый центр Ахмадабада, базар Амбавади шаак (овощной рынок) и сад Паримал.", "Закон об оказании помощи и подотчетности в связи с геноцидом в Ираке и Сирии 2018 года представляет собой закон о предоставлении гуманитарной помощи жертвам геноцида, совершенного Исламским государством Ирак и Левант (ИГИЛ) во время Гражданской войны в Сирии и Ираке."] #текст, который будет
text_hard_rus = []
isTraining = False
isWorking = True
languages = ["Russian", "English"]
curr_lang = "Russian"
n = 2

@bot.message_handler(content_types=['text'])
def start(message):
    global isTraining
    global text
    global isWorking
    global text_easy_rus
    global text_norm_rus
    global text_hard_rus

    #начало
    if (message.text == "/start" or message.text == "Привет" or message.text == "привет") and isTraining == False:
        messages = ['Вас приветствует лучший в мире бот для тренировки печати!', 'Hello, World!', 'Здравствуйте!', 'Привет, человек по ту сторону экрана.', 'С Наступающим Новым Годом!']
        i = random.randrange(0, 4)
        keyboard = types.InlineKeyboardMarkup()
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);
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
    global curr_lang
    global languages
    global text_easy_rus
    global text_norm_rus
    global text_hard_rus

    if call.data == "go":
        if curr_lang == "Russian":
            if n == 2:
                text_num = random.randrange(0, len(text_norm_rus))
                text = text_norm_rus[text_num]
            elif n == 1:
                text_num = random.randrange(0, len(text_easy_rus))
                text = text_easy_rus[text_num]
            else:
                text_num = random.randrange(0, len(text_hard_rus))
                text = text_hard_rus[text_num]

        sTime = time.time()
        isTraining = True

        bot.send_message(call.message.chat.id, 'Напечатайте данный текст как можно быстрее:')
        bot.send_message(call.message.chat.id, text)

        #bot.send_message(message.from_user.id, 'Слов напечатано: {} из {}.'.format(len(message.text.split()), letters))
        #if texts == message.text:
            #bot.send_message(call.message.chat.id, 'Всё верно!')

    if call.data == "settings":
        bot.send_message(call.message.chat.id, 'Настройки:')

        keyboard = types.InlineKeyboardMarkup()
        key_ch_lang = types.InlineKeyboardButton(text='Сменить язык тестов', callback_data='ch_lang');
        keyboard.add(key_ch_lang)

        bot.send_message(call.message.chat.id, 'Язык тестов - {}'.format(curr_lang), reply_markup = keyboard)
    if call.data == "ch_lang":
        keyboard = types.InlineKeyboardMarkup()
        key_eng = types.InlineKeyboardButton(text='English', callback_data='eng');
        keyboard.add(key_eng)
        key_rus = types.InlineKeyboardButton(text='Russian', callback_data='rus');
        keyboard.add(key_rus)

        bot.send_message(call.message.chat.id, 'Доступные языки:', reply_markup = keyboard)
        
    if call.data == "eng":
        curr_lang = languages[1]

        keyboard = types.InlineKeyboardMarkup()
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)

        bot.send_message(call.message.chat.id, 'Язык тестов заменён на: {}'.format(curr_lang), reply_markup = keyboard)

    if call.data == "rus":
        curr_lang = languages[0]

        keyboard = types.InlineKeyboardMarkup()
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)

        bot.send_message(call.message.chat.id, 'Язык тестов заменён на: {}'.format(curr_lang), reply_markup = keyboard)

bot.polling(none_stop=isWorking, interval=0)