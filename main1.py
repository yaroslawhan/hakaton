# -*- coding: utf-8 -*-

import telebot, random, time
from telebot import types
from fuzzywuzzy import fuzz
import pickle #


bot = telebot.TeleBot('2115882328:AAFxgL0uHGtc4tKqlB9_EtScnqyZeO_CLDk')
sTime = 0 #cтартовое время
text = "" #текст, который будет
text_easy_rus = ["Поздно ночью из похода воротился воевода. Он слугам велит молчать; в спальню кинулся к постеле; Дернул полог… В самом деле! Никого; пуста кровать.", 
"Пять зелёных лягушат в воду броситься спешат — испугались цапли! А меня они смешат: я же этой цапли не боюсь ни капли!", 
"Есть телевизор — подайте трибуну, так проору — разнесётся на мили! Он не окно, я в окно и не плюну — мне будто дверь в целый мир прорубили."]
text_norm_rus = ["112 год до нашей эры был годом до-юлианского римского календаря. В то время он был известен как Год консульства Друза и Цезонина и Пятый год Юандинга.", 
"Амбавади-это район, расположенный в Ахмадабаде, Индия. Основными достопримечательностями этого района являются Центральный торговый центр Ахмадабада, базар Амбавади шаак (овощной рынок) и сад Паримал.", 
"Закон об оказании помощи и подотчетности в связи с геноцидом в Ираке и Сирии 2018 года представляет собой закон о предоставлении гуманитарной помощи жертвам геноцида, совершенного Исламским государством Ирак и Левант (ИГИЛ) во время Гражданской войны в Сирии и Ираке."] #текст, который будет
text_hard_rus = ["С точки зpения банальной эpудиции каждый индивидуум, кpитически мотивиpующий абстpакцию, не может игноpиpовать кpитеpии утопического субьективизма, концептуально интеpпpетиpуя общепpинятые дефанизиpующие поляpизатоpы, поэтому консенсус, достигнутый диалектической матеpиальной классификацией всеобщих мотиваций в паpадогматических связях пpедикатов, pешает пpоблему усовеpшенствования фоpмиpующих геотpансплантационных квазипузлистатов всех кинетически коpеллиpующих аспектов.", 
"Исходя из этого, мы пpишли к выводу, что каждый пpоизвольно выбpанный пpедикативно абсоpбиpующий обьект pациональной мистической индукции можно дискpетно детеpминиpовать с аппликацией ситуационной паpадигмы коммуникативно-функционального типа пpи наличии детектоpно-аpхаического дистpибутивного обpаза в Гилбеpтовом конвеpгенционном пpостpанстве, однако пpи паpаллельном колабоpационном анализе спектpогpафичеких множеств, изомоpфно pелятивных к мультиполосным гипеpболическим паpаболоидам, интеpпpетиpующим антpопоцентpический многочлен Hео-Лагpанжа, возникает позиционный сигнификатизм гентильной теоpии психоанализа, в pезультате чего надо пpинять во внимание следующее...", 
"поскольку не только эзотеpический, но и экзистенциальный аппеpцепциониpованный энтpополог антецедентно пассивизиpованный высокоматеpиальной субстанцией, обладает пpизматической идиосинхpацией, но так как валентностный фактоp отpицателен, то и, соответственно, антагонистический дискpедитизм дегpадиpует в эксгибиционном напpавлении, поскольку, находясь в пpепубеpтатном состоянии, пpактически каждый субьект, меланхолически осознавая эмбpиональную клаустоpофобию, может экстpаполиpовать любой пpоцесс интегpации и диффеpенциации в обоих напpавлениях, отсюда следует, что в pезультате синхpонизации, огpаниченной минимально допустимой интеpполяцией обpаза, все методы конвеpгенционной концепции тpебуют пpактически тpадиционных тpансфоpмаций неоколониализма."]
text_easy_eng = ["Two roads diverged in a yellow wood, and sorry I could not travel both and be one traveler, long I stood and looked down one as far as I could to where it bent in the undergrowth.",
"A little yellow Bird above, a little yellow Flower below; the little Bird can sing the love that Bird and Blossom know; the Blossom has no song nor wing, but breathes the love he cannot sing.", 
"In the other gardens and all up the vale, from the autumn bonfires see the smoke trail! Pleasant summer over and all the summer flowers; the red fire blazes, the grey smoke towers."]
text_norm_eng = ["The events unfolding on a tapestry took place in the years 1064 to 1066. Anglo-Saxon earl Harold Godwinson is depicted receiving the English crown from Edward the Confessor, a deathly ill English monarch. An invading Norman force is then shown, which soon engages Saxon forces in a bloody battle. Ultimately king Harold is slain, and English forces flee the battlefield. The last part of the tapestry was supposedly lost and a newer piece was added in its place roughly in 1810.", 
"The tapestry is made largely of plain weave linen and embroidered with wool yarn. The woolen crewelwork is made in various shades of brown, blue and green, mainly terracotta, russet, and olive green. Later restorations have also added some brighter colours, such as orange and light yellow. Attempts at restoration of both the beginning and the end of the tapestry were made at some points, adding some missing tituli and numerals, although an ongoing debate disputes the validity of these restorations.", 
"The idea of ‘eternal return’ (or recurrence) is the idea that each event and occurrence that happens, repeats itself eternally in cycles. Rather than postulating this, Nietzsche actually ponders if it’s true. Although it’s a very popular idea that seemingly stems logically from the laws of infinite Universe as we know it, it still hasn’t been proven nor disproven, so Nietzsche marks it as ‘the most burdensome’ of his thoughts."]
text_hard_eng = ["The development of a human embryo can go awry in many different ways. One of the most common types of birth defects that afflict yet unborn children are referred to as neural tube defects (NTDs). A premise for the development of NTDs lies in an incomplete closure of a neural tube, a precursor to the human central nervous system that forms from an embryo’s nervous tissue over the course of a normal development. As a result, an opening remains in the developing spine or cranium of the fetus, which, depending on its severity, can fully disrupt the growth of the nervous system. Neural tube defects affect either the development of the brain, or spine, or both. Most of the conditions that stem from NTDs are usually untreatable, leave the person largely disabled, and have an extremely high mortality rate.", 
"A game is usually defined as a process involving two or more actors, each of them having something to gain or lose through their actions after the game is finished (or ‘solved’). Thus, the definition applies to most of the regular games (like, for example, poker), but can be broadened as necessary to cover multitudes of other situations, both real and hypothetical. The action is presumed to be taken by a ‘rational agent’ - that is, an actor that acts consistently and always chooses an action that is the most optimal in terms of loss/gain ratio according to his current position. A game can be cooperative or non-cooperative, allowing or disallowing willing alliances between the participants respectively.", 
"One of the most famous examples of finding Nash equilibrium is a thought experiment called Prisoner’s dilemma. Suppose there are two prisoners interrogated in two different prison cells. They have no way to communicate with each other, but each of them knows that the other is also interrogated. Each prisoner is sentenced to one year in prison. Each prisoner is then offered a deal: if he testifies against the other, he is set free, while the other gets a harsher, 3-year penalty. However, if both prisoners testify against each other, both of them will get a harder sentence, and both will serve 2 years in prison. Each prisoner can choose either to testify or to remain silent. What is the optimal course of action for each prisoner?"]
isTraining = False
isWorking = True
languages = ["Russian", "English"]
curr_lang = "Russian"
n = 2

results = [] #

def save(obj): #
    my_pickled_object = pickle.dumps(obj)
    print(my_pickled_object)

class Result: #
    def __init__(self, id_, name_, score_):
        self.id = id_
        self.name = name_
        self.score = score_
        self.ratio = 100 #совпадение
        self.cps = 0 #символы в секунду

def tryToAddToTable(id, name, score): #
    global results
    result = Result(id, name, score)

    if len(results) < 10 or results[9].score < score:
        for i in results:
            if i.id == id and score > i.score:
                results.remove(i)

        results.append(result)
        sortResults()

def sortResults(): #
    global results

    results = sorted(results, key=lambda x: x.score, reverse=True)

    for i in range(0, len(results)):
        print(results[i].name + " " + str(results[i].score))

    save(results)

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
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);
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

        keyboard = types.InlineKeyboardMarkup()
        key_go= types.InlineKeyboardButton(text='Продолжить тренировку', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);

        bot.send_message(message.chat.id, timeText + ", " + errorsText, reply_markup = keyboard)

        name = message.from_user.first_name
        lastName = message.from_user.last_name

        if lastName != None:
            name += " " + lastName

        tryToAddToTable(message.chat.id, name, charsPerSecond * (ratio/100))
        

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
    global n

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

        if curr_lang == "English":
            if n == 2:
                text_num = random.randrange(0, len(text_norm_eng))
                text = text_norm_eng[text_num]
            elif n == 1:
                text_num = random.randrange(0, len(text_easy_eng))
                text = text_easy_eng[text_num]
            else:
                text_num = random.randrange(0, len(text_hard_eng))
                text = text_hard_eng[text_num]

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
        key_ch_n = types.InlineKeyboardButton(text='Сменить сложность тестов', callback_data='ch_n');
        keyboard.add(key_ch_n)

        bot.send_message(call.message.chat.id, 'Язык тестов - {}'.format(curr_lang))
        bot.send_message(call.message.chat.id, 'Сложность тестов - {}'.format(n), reply_markup = keyboard)

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
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);

        bot.send_message(call.message.chat.id, 'Язык тестов заменён на: {}'.format(curr_lang), reply_markup = keyboard)

    if call.data == "rus":
        curr_lang = languages[0]

        keyboard = types.InlineKeyboardMarkup()
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);

        bot.send_message(call.message.chat.id, 'Язык тестов заменён на: {}'.format(curr_lang), reply_markup = keyboard)

    if call.data == "ch_n":
        keyboard = types.InlineKeyboardMarkup()
        key_easy = types.InlineKeyboardButton(text='Легко', callback_data='easy');
        keyboard.add(key_easy)
        key_norm = types.InlineKeyboardButton(text='Нормально', callback_data='norm');
        keyboard.add(key_norm)
        key_hard = types.InlineKeyboardButton(text='Сложно', callback_data='hard');
        keyboard.add(key_hard)

        bot.send_message(call.message.chat.id, 'Доступные уровни сложности:', reply_markup = keyboard)

    if call.data == "easy":
        n = 1

        keyboard = types.InlineKeyboardMarkup()
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);

        bot.send_message(call.message.chat.id, 'Сложность тестов заменена на: {}'.format(str(n)), reply_markup = keyboard)

    if call.data == "norm":
        n = 2

        keyboard = types.InlineKeyboardMarkup()
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);

        bot.send_message(call.message.chat.id, 'Сложность тестов заменена на: {}'.format(str(n)), reply_markup = keyboard)

    if call.data == "hard":
        n = 3

        keyboard = types.InlineKeyboardMarkup()
        key_go= types.InlineKeyboardButton(text='Начать тренировку!', callback_data='go')
        keyboard.add(key_go)
        key_settings = types.InlineKeyboardButton(text='Настройки', callback_data='settings');
        keyboard.add(key_settings);

        bot.send_message(call.message.chat.id, 'Сложность тестов заменена на: {}'.format(str(n)), reply_markup = keyboard)

bot.polling(none_stop=isWorking, interval=0)