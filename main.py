import telebot

bot = telebot.TeleBot("7805702387:AAFR8ZFKAepB-XKeQODSzpR5ENxi0uxpMak")

data = {"أنوار المعرفة والأمة المنقذة…. أمتنا توحد العالم":"https://quranok.com/wp-content/uploads/2023/03/%D8%A8%D9%8A%D9%86_%D8%B9%D9%8A%D8%B3%D9%89_%D9%88%D9%85%D8%AD%D9%85%D8%AF_%D8%B5%D9%84%D9%89_%D8%A7%D9%84%D9%84%D9%87_%D8%B9%D9%84%D9%8A%D9%87%D9%85%D8%A7_%D9%88%D8%B3%D9%84%D9%85.mp3",
        "صلة الأرحام الإنسانية دعوة الأنبياء عامة":"https://quranok.com/wp-content/uploads/2023/02/%D8%AD%D8%B1%D9%85%D8%A9_%D8%A7%D9%84%D8%AF%D9%85%D8%A7%D8%A1_%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85_%D8%A7%D9%84%D9%85%D8%AC%D9%8A%D8%AF%D9%8A.mp3",
        "العظمة النبوية في القيادة الدعوية":"https://quranok.com/wp-content/uploads/2023/01/%D8%B1%D8%A7%D8%A8%D8%B9_%D8%A7%D9%84%D8%A5%D8%B3%D9%84%D8%A7%D9%85_%D9%88%D8%A8%D8%B1%D9%85%D8%AC%D8%A9_%D8%A7%D9%84%D8%AA%D9%84%D8%B7%D9%81_%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85_%D8%A7%D9%84%D9%85%D8%AC%D9%8A%D8%AF%D9%8A.mp3",
        "محاولات تعطيل إنارة الحياة":"https://quranok.com/wp-content/uploads/2023/01/%D8%B3%D8%A7%D8%AD%D8%B1_%D9%82%D8%B1%D9%8A%D8%B4_%D9%88%D8%B3%D8%A7%D8%AD%D8%B1%D8%AA%D9%87_%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85_%D8%A7%D9%84%D9%85%D8%AC%D9%8A%D8%AF%D9%8A.mp3",
        "صفات العظمة":"https://quranok.com/wp-content/uploads/2023/01/%D9%88%D8%A7%D9%84%D9%84%D9%87-%D9%84%D8%A7-%D9%8A%D8%AE%D8%B2%D9%8A%D9%83-%D8%A7%D9%84%D9%84%D9%87-%D8%A3%D8%A8%D8%AF%D8%A7-%D8%A3.-%D8%AF.-%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85-%D8%A7%D9%84%D9%85%D8%AC%D9%8A%D8%AF%D9%8A.mp3",
        "الفرار إلى الله القهار":"https://quranok.com/wp-content/uploads/2022/12/%D9%85%D9%86%D8%B2%D9%84%D8%A9_%D8%A7%D9%84%D9%81%D8%B1%D8%A7%D8%B1_%D8%A5%D9%84%D9%89_%D8%A7%D9%84%D9%84%D9%87_%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85_%D8%A7%D9%84%D9%85%D8%AC%D9%8A%D8%AF%D9%8A.mp3",
        "قوانين بناء الحياة":"https://quranok.com/wp-content/uploads/2022/12/%D9%84%D9%88_%D9%86%D8%B4%D8%A7%D8%A1_%D8%A3%D8%B5%D8%A8%D9%86%D8%A7%D9%87%D9%85_%D8%A8%D8%A8%D8%B9%D8%B6_%D8%B0%D9%86%D9%88%D8%A8%D9%87%D9%85_%D8%B9%D8%A8%D8%AF_%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85_%D8%A7%D9%84%D9%85%D8%AC%D9%8A%D8%AF%D9%8A_.mp3"
        }

@bot.message_handler(commands=['start'])
def start(message):
    #global current_option
    #current_option = ""
    #lessons = list(data.keys())
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    for item in data.keys():
        button = telebot.types.KeyboardButton(item)
        markup.add(button)
    #button1 = telebot.types.KeyboardButton(lessons[0])
    #markup.add(button1)
    #button2 = telebot.types.KeyboardButton(lessons[1])
    #markup.add(button2)
    #button3 = telebot.types.KeyboardButton(lessons[2])
    #markup.add(button3)
    #button4 = telebot.types.KeyboardButton(lessons[3])
    #markup.add(button4)
    #button5 = telebot.types.KeyboardButton(lessons[4])
    #markup.add(button5)
    #button6 = telebot.types.KeyboardButton(lessons[5])
    #markup.add(button6)
    bot.reply_to(message, "اختر خطبة:", reply_markup = markup)

@bot.message_handler(func=lambda message: True)
def search(message):
    for item in data.keys():
        if message.text == item:
            bot.send_audio(message.chat.id, data[item])
bot.polling()