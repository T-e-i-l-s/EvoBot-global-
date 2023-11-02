from datetime import datetime
import time

#библиотеки для telegram
import telebot
bot = telebot.TeleBot('5294354029:AAGRbw7nWPnmz4D1KwKQaNKf5dmrc3I71qU')

#nms = ['Гусман бей','Райнур абый','Аккмалутдинов','Бариев','Воробьев','Галаутдинов','Гашигулин','Димухаметов','Загидулин','Закиров','Замалеев','Ильин','Исмагилов',
#         'Леухин','Лукьянов','Мифтахов','МустафинК','МустафинС','Мухаметгалиев','ПимурзинРусл',
#         'ПимурзинРуст','Сахабутдинов','Фаизов','Фазлиев','Хамидулин','Шамсиев','Юсупов']
ind6A = []
ind7A = []



#клавы
main = telebot.types.ReplyKeyboardMarkup()
main.add('Домашнее задание')
main.add('Новости')
main.add('Дежурство')
main.add('Расписание')
main.add('Изменить класс')

dz7 = telebot.types.ReplyKeyboardMarkup()
dz7.add('Биология')
dz7.add('Турецкий(рус)')
dz7.add('Турецкий(тат)')
dz7.add('География')
dz7.add('ИЗО')
dz7.add('Английский(сред)')
dz7.add('Английский(сил)')
dz7.add('История')
dz7.add('Лит-ра')
dz7.add('Алгебра')
dz7.add('Геометрия')
dz7.add('Музыка')
dz7.add('Общество')
dz7.add('Род.лит(рус)')
dz7.add('Родной(рус)')
dz7.add('Род.лит(тат)')
dz7.add('Родной(тат)')
dz7.add('Рус.яз')
dz7.add('Технология')
dz7.add('Физ-культура')
dz7.add('Физика')
dz7.add('Информатика')
dz7.add('MENU')


dz6 = telebot.types.ReplyKeyboardMarkup()
dz6.add('Биология')
dz6.add('Турецкий(рус)')
dz6.add('Турецкий(тат)')
dz6.add('География')
dz6.add('ИЗО')
dz6.add('Английский(сред)')
dz6.add('Английский(сил)')
dz6.add('История')
dz6.add('Лит-ра')
dz6.add('Математика')
dz6.add('Музыка')
dz6.add('Общество')
dz6.add('Род.лит(рус)')
dz6.add('Родной(рус)')
dz6.add('Род.лит(тат)')
dz6.add('Родной(тат)')
dz6.add('Рус.яз')
dz6.add('Технология')
dz6.add('Физ-культура')
dz6.add('MENU')



week = telebot.types.ReplyKeyboardMarkup()
week.add('ПН','ВТ','СР')
week.add('ЧТ','ПТ','СБ')
week.add('MENU')

classes = telebot.types.ReplyKeyboardMarkup()
classes.add('6A')
classes.add('7A')


#подключение firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


#обновление информации
def update():
    global timetable7a
    global news7a
    global hw7a
    global tgid7a
    global dez7a

    global timetable6a
    global news6a
    global hw6a
    global tgid6a
    global dez6a

    db7 = db.collection('Evo1')
    docs7 = db7.stream()

    for doc in docs7:
        if doc.id == "timetable":
            timetable7a = doc.to_dict()
        elif doc.id == "news":
            news7a = doc.to_dict()
        elif doc.id == "hw":
            hw7a = doc.to_dict()
        elif doc.id == "dez":
            dez7a = doc.to_dict()


    db6 = db.collection('Evo6a')
    docs6 = db6.stream()

    for doc in docs6:
        if doc.id == "timetable":
            timetable6a = doc.to_dict()
        elif doc.id == "news":
            news6a = doc.to_dict()
        elif doc.id == "hw":
            hw6a = doc.to_dict()
        elif doc.id == "dez":
            dez6a = doc.to_dict()

    #ind[0]=  tgid["n0"]
    #ind[1] =  tgid["n1"]
    #ind[2] =  tgid["n2"]
    #ind[3] =  tgid["n3"]
    #ind[4] =  tgid["n4"]
    #ind[5] =  tgid["n5"]
    #ind[6] =  tgid["n6"]
    #ind[7] =  tgid["n7"]
    #ind[8] =  tgid["n8"]
    #ind[9] =  tgid["n9"]
    #ind[10] =  tgid["n10"]
    #ind[11] =  tgid["n11"]
    #ind[12] =  tgid["n12"]
    #ind[13] =  tgid["n13"]
    #ind[14] =  tgid["n14"]
    #ind[15] =  tgid["n15"]
    #ind[16] =  tgid["n16"]
    #ind[17] =  tgid["n17"]
    #ind[18] =  tgid["n18"]
    #ind[19] =  tgid["n19"]
    #ind[20] =  tgid["n20"]
    #ind[21] =  tgid["n21"]
    #ind[22] =  tgid["n22"]
    #ind[23] =  tgid["n23"]
    #ind[24] =  tgid["n24"]
    #ind[25] =  tgid["n25"]
    #ind[26] =  tgid["n26"]
    #ind[27] =  tgid["n27"]


update()

#def updateind():
#    doc_ref = db.collection('Evo1').document('tgid')
#
#    i = 1
#    for i in range(28):
#        string = "n" + str(i)
#        doc_ref.update({string: ind[i]})



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте!👋', reply_markup=main)
    if (message.chat.id not in ind6A) or (message.chat.id not in ind7A):
        bot.send_message(message.chat.id,"Для использования меня нам нужно занать ваш класс,пожалуйста,выберите его.",reply_markup=classes)

@bot.message_handler(commands=['update'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ожидайте')
    update()
    bot.send_message(message.chat.id, 'Выполенно')




@bot.message_handler(commands=["event" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/event ', '')
    wrt_ref = db.collection('Evo6a').document('news')
    wrt_ref.update({'event': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["new1" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/new1 ', '')
    wrt_ref = db.collection('Evo6a').document('news')
    wrt_ref.update({'new1': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["new2" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/new2 ', '')
    wrt_ref = db.collection('Evo6a').document('news')
    wrt_ref.update({'new2': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["new3" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/new3 ', '')
    wrt_ref = db.collection('Evo6a').document('news')
    wrt_ref.update({'new3': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["new4" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/new4 ', '')
    wrt_ref = db.collection('Evo6a').document('news')
    wrt_ref.update({'new4': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["new5" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/new5 ', '')
    wrt_ref = db.collection('Evo6a').document('news')
    wrt_ref.update({'new5': txt})
    bot.send_message(message.chat.id, "Записано")


@bot.message_handler(commands=["mon" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/mon ', '')
    wrt_ref = db.collection('Evo6a').document('dez')
    wrt_ref.update({'mon': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["tue" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/tue ', '')
    wrt_ref = db.collection('Evo6a').document('dez')
    wrt_ref.update({'tue': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["wed" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/wed ', '')
    wrt_ref = db.collection('Evo6a').document('dez')
    wrt_ref.update({'wed': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["thu" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/thu ', '')
    wrt_ref = db.collection('Evo6a').document('dez')
    wrt_ref.update({'thu': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["fri" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/fri ', '')
    wrt_ref = db.collection('Evo6a').document('dez')
    wrt_ref.update({'fri': txt})
    bot.send_message(message.chat.id, "Записано")

@bot.message_handler(commands=["sat" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/sat ', '')
    wrt_ref = db.collection('Evo6a').document('dez')
    wrt_ref.update({'sat': txt})
    bot.send_message(message.chat.id, "Записано")


@bot.message_handler(commands=["bio" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/bio ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'bio': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["tur1"])
def start_message(message):
    txt = message.text
    txt = txt.replace('/tur1 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'tur1': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["tur2"])
def start_message(message):
    txt = message.text
    txt = txt.replace('/tur2 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'tur2': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["geo" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/geo ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'geo': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["art" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/art ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'art': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["eng1"])
def start_message(message):
    txt = message.text
    txt = txt.replace('/eng1 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'eng1': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["eng2"])
def start_message(message):
    txt = message.text
    txt = txt.replace('/eng2 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'eng2': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["his" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/his ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'his': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["lit" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/lit ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'lit': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["math"])
def start_message(message):
    txt = message.text
    txt = txt.replace('/math ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'math': txt})
    bot.send_message(message.chat.id, "Записано")


@bot.message_handler(commands=["mus" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/mus ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'mus': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["obs" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/obs ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'obs': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["rl1" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/rl1 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'rl1': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["rl2" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/rl2 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'rl2': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["r1"  ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/r1 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'r1': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["r2"  ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/r2 ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'r2': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["rus" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/rus ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'rus': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["tec" ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/tec ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'tec': txt})
    bot.send_message(message.chat.id, "Записано")



@bot.message_handler(commands=["pe"  ])
def start_message(message):
    txt = message.text
    txt = txt.replace('/pe ', '')
    wrt_ref = db.collection('Evo6a').document('hw')
    wrt_ref.update({'pe': txt})
    bot.send_message(message.chat.id, "Записано")


@bot.message_handler(commands=["class"  ])
def start_message(message):
    if message.chat.id in ind7A:
        ind7A.pop(ind7A.index(message.chat.id))
        bot.send_message(message.chat.id, "Выберите свой класс заново.", reply_markup=classes)
    elif message.chat.id in ind6A:
        ind6A.pop(ind6A.index(message.chat.id))
        bot.send_message(message.chat.id, "Выберите свой класс заново.", reply_markup=classes)
    else:
        bot.send_message(message.chat.id, "Выберите свой класс.",reply_markup=classes)



@bot.message_handler(content_types=['text'])
def ans(message):
    global timetable7a
    global news7a
    global hw7a
    global dez7a
    global timetable6a
    global news6a
    global hw6a
    global dez6a
    global timetable
    global news
    global hw
    global dez

    timetable = timetable6a
    news = news6a
    hw = hw6a
    dez = dez6a

    if message.text == 'Изменить класс':
        if message.chat.id in ind7A:
            ind7A.pop(ind7A.index(message.chat.id))
            bot.send_message(message.chat.id, "Выберите свой класс заново.", reply_markup=classes)
        elif message.chat.id in ind6A:
            ind6A.pop(ind6A.index(message.chat.id))
            bot.send_message(message.chat.id, "Выберите свой класс заново.", reply_markup=classes)
        else:
            bot.send_message(message.chat.id, "Выберите свой класс.", reply_markup=classes)


    if ((message.chat.id not in ind6A) and (message.chat.id not in ind7A)) and (message.text != '7A' and message.text != '6A') and message.text != 'Изменить класс':
        bot.send_message(message.chat.id,"Мне нужно занать ваш класс,пожалуйста,выберите его.",reply_markup=classes)

    if message.text == '6A':
        ind6A.append(message.chat.id)

        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        #updateind()

    elif message.text == '7A':
        ind7A.append(message.chat.id)
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        #updateind()

    else:

        if message.chat.id in ind7A:
            timetable=timetable7a
            news=news7a
            hw=hw7a
            dez=dez7a
        elif message.chat.id in ind6A:
            timetable=timetable6a
            news=news6a
            hw=hw6a
            dez=dez6a

        if message.chat.id in ind7A or message.chat.id in ind6A:

            if message.text == 'MENU':
                bot.send_message(message.chat.id, "Выполняю", reply_markup=main)


            if message.text == 'Домашнее задание':
                if message.chat.id in ind7A:
                    bot.send_message(message.chat.id, "Выберите урок:", reply_markup=dz7)
                elif message.chat.id in ind6A:
                    bot.send_message(message.chat.id, "Выберите урок:", reply_markup=dz6)
            elif message.text == 'Новости':
                bot.send_message(message.chat.id, "Событие: " + news["event"])
                bot.send_message(message.chat.id, "Новости:")
                bot.send_message(message.chat.id, "1. " + news["new1"])
                bot.send_message(message.chat.id, "2. " + news["new2"])
                bot.send_message(message.chat.id, "3. " + news["new3"])
                bot.send_message(message.chat.id, "4. " + news["new4"])
                bot.send_message(message.chat.id, "5. " + news["new5"])
            elif message.text == 'Дежурство':
                bot.send_message(message.chat.id, "Дежурные на этой неделе:")
                bot.send_message(message.chat.id, "ПН." + dez["mon"])
                bot.send_message(message.chat.id, "ВТ." + dez["tue"])
                bot.send_message(message.chat.id, "СР." + dez["wed"])
                bot.send_message(message.chat.id, "ЧТ." + dez["thu"])
                bot.send_message(message.chat.id, "ПТ." + dez["fri"])
                bot.send_message(message.chat.id, "CБ." + dez["sat"])
            elif message.text == 'Расписание':
                bot.send_message(message.chat.id,"Выберите день",reply_markup=week)


            if message.text == 'ПН':
                bot.send_message(message.chat.id, "1. " + timetable["m1"])
                bot.send_message(message.chat.id, "2. " + timetable["m2"])
                bot.send_message(message.chat.id, "3. " + timetable["m3"])
                bot.send_message(message.chat.id, "4. " + timetable["m4"])
                bot.send_message(message.chat.id, "5. " + timetable["m5"])
                bot.send_message(message.chat.id, "6. " + timetable["m6"])
                bot.send_message(message.chat.id, "7. " + timetable["m7"])
                bot.send_message(message.chat.id, "8. " + timetable["m8"])
                bot.send_message(message.chat.id, "9. " + timetable["m9"])
            elif message.text == 'ВТ':
                bot.send_message(message.chat.id, "1. " + timetable["tu1"])
                bot.send_message(message.chat.id, "2. " + timetable["tu2"])
                bot.send_message(message.chat.id, "3. " + timetable["tu3"])
                bot.send_message(message.chat.id, "4. " + timetable["tu4"])
                bot.send_message(message.chat.id, "5. " + timetable["tu5"])
                bot.send_message(message.chat.id, "6. " + timetable["tu6"])
                bot.send_message(message.chat.id, "7. " + timetable["tu7"])
                bot.send_message(message.chat.id, "8. " + timetable["tu8"])
                bot.send_message(message.chat.id, "9. " + timetable["tu9"])
            elif message.text == 'СР':
                bot.send_message(message.chat.id, "1. " + timetable["w1"])
                bot.send_message(message.chat.id, "2. " + timetable["w2"])
                bot.send_message(message.chat.id, "3. " + timetable["w3"])
                bot.send_message(message.chat.id, "4. " + timetable["w4"])
                bot.send_message(message.chat.id, "5. " + timetable["w5"])
                bot.send_message(message.chat.id, "6. " + timetable["w6"])
                bot.send_message(message.chat.id, "7. " + timetable["w7"])
                bot.send_message(message.chat.id, "8. " + timetable["w8"])
                bot.send_message(message.chat.id, "9. " + timetable["w9"])
            elif message.text == 'ЧТ':
                bot.send_message(message.chat.id, "1. " + timetable["th1"])
                bot.send_message(message.chat.id, "2. " + timetable["th2"])
                bot.send_message(message.chat.id, "3. " + timetable["th3"])
                bot.send_message(message.chat.id, "4. " + timetable["th4"])
                bot.send_message(message.chat.id, "5. " + timetable["th5"])
                bot.send_message(message.chat.id, "6. " + timetable["th6"])
                bot.send_message(message.chat.id, "7. " + timetable["th7"])
                bot.send_message(message.chat.id, "8. " + timetable["th8"])
                bot.send_message(message.chat.id, "9. " + timetable["th9"])
            elif message.text == 'ПТ':
                bot.send_message(message.chat.id, "1. " + timetable["f1"])
                bot.send_message(message.chat.id, "2. " + timetable["f2"])
                bot.send_message(message.chat.id, "3. " + timetable["f3"])
                bot.send_message(message.chat.id, "4. " + timetable["f4"])
                bot.send_message(message.chat.id, "5. " + timetable["f5"])
                bot.send_message(message.chat.id, "6. " + timetable["f6"])
                bot.send_message(message.chat.id, "7. " + timetable["f7"])
                bot.send_message(message.chat.id, "8. " + timetable["f8"])
                bot.send_message(message.chat.id, "9. " + timetable["f9"])
            elif message.text == 'СБ':
                bot.send_message(message.chat.id, "1. " + timetable["s1"])
                bot.send_message(message.chat.id, "2. " + timetable["s2"])
                bot.send_message(message.chat.id, "3. " + timetable["s3"])
                bot.send_message(message.chat.id, "4. " + timetable["s4"])
                bot.send_message(message.chat.id, "5. " + timetable["s5"])
                bot.send_message(message.chat.id, "6. " + timetable["s6"])
                bot.send_message(message.chat.id, "7. " + timetable["s7"])
                bot.send_message(message.chat.id, "8. " + timetable["s8"])
                bot.send_message(message.chat.id, "9. " + timetable["s9"])





            if message.text == 'Биология':              bot.send_message(message.chat.id, 'По биологии задали: '                + hw["bio"      ])
            elif message.text == 'Турецкий(рус)':       bot.send_message(message.chat.id, 'По турецкому задали: '               + hw["tur1"      ])
            elif message.text == 'Турецкий(тат)':       bot.send_message(message.chat.id, 'По турецкому задали: '               + hw["tur2"      ])
            elif message.text == 'География':           bot.send_message(message.chat.id, 'По географии задали: '               + hw["geo"      ])
            elif message.text == 'ИЗО':                 bot.send_message(message.chat.id, 'По ИЗО задали: '                     + hw["art"      ])
            elif message.text == 'Английский(сред)':    bot.send_message(message.chat.id, 'По английскому(ср.группы) задали: '  + hw["eng1"      ])
            elif message.text == 'Английский(сил)':     bot.send_message(message.chat.id, 'По английскому(сил.группы) задали: ' + hw["eng2"      ])
            elif message.text == 'История':             bot.send_message(message.chat.id, 'По истории задали: '                 + hw["his"      ])
            elif message.text == 'Лит-ра':              bot.send_message(message.chat.id, 'По лит-ре задали: '                  + hw["lit"      ])
            elif message.text == 'Геометрия':           bot.send_message(message.chat.id, 'По алгебре задали: '                 + hw["geom"      ])
            elif message.text == 'Алгебра':             bot.send_message(message.chat.id, 'По геометрии задали: '               + hw["alge"      ])
            elif message.text == 'Математика':               bot.send_message(message.chat.id, 'По математике задали: '         + hw["math"      ])
            elif message.text == 'Музыка':              bot.send_message(message.chat.id, 'По музыке задали: '                  + hw["mus"      ])
            elif message.text == 'Общество':            bot.send_message(message.chat.id, 'По обществу задали: '                + hw["obs"      ])
            elif message.text == 'Род.лит(рус)':        bot.send_message(message.chat.id, 'По род.лит(рус) задали: '            + hw["rl1"      ])
            elif message.text == 'Родной(рус)':         bot.send_message(message.chat.id, 'По родной(рус) задали: '             + hw["rl2"      ])
            elif message.text == 'Род.лит(тат)':        bot.send_message(message.chat.id, 'По род.лит(тат) задали: '            + hw["r1"      ])
            elif message.text == 'Родной(тат)':         bot.send_message(message.chat.id, 'По родной(тат) задали: '             + hw["r2"      ])
            elif message.text == 'Рус.яз':              bot.send_message(message.chat.id, 'По рус.яз задали: '                  + hw["rus"      ])
            elif message.text == 'Технология':          bot.send_message(message.chat.id, 'По технологии задали: '              + hw["tec"      ])
            elif message.text == 'Физ-культура':        bot.send_message(message.chat.id, 'По физ-культуре задали: '            + hw["pe"      ])
            elif message.text == 'Физика':              bot.send_message(message.chat.id, 'По физике задали: '                  + hw["physic"      ])
            elif message.text == 'Информатика':         bot.send_message(message.chat.id, 'По информатике задали: '             + hw["info"      ])





while True:
        try:
            print("polling")
            bot.polling()
        except:
            print("stop polling")
            bot.stop_polling()
            time.sleep(15);

