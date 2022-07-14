import telebot
from telebot import types
from settings import TOKEN, work_list
import datetime

bot = telebot.TeleBot(TOKEN)
my_list = work_list.copy()
tek_n = 1


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f"Привет {m.chat.first_name},\nу нас есть новое задание!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Посмотреть весь список")
    item2 = types.KeyboardButton("Текущее дело")
    item3 = types.KeyboardButton("Завершить текущее")
    item4 = types.KeyboardButton("Начать заново")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)

    bot.send_message(m.chat.id, 'Выберите действие', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Посмотреть весь список":
        all_var(message.chat.id, my_list)
    elif message.text.strip() == "Текущее дело":
        tekuch(message.chat.id)
    elif message.text.strip() == "Завершить текущее":
        zaversh(message.chat.id)
    elif message.text.strip() == "Начать заново":
        zanovo(message.chat.id)


def all_var(id, d):
    global tek_n
    l = []
    for i in my_list:
        if i < tek_n:
            l.append(str(i)+") "+my_list[i]+" (готово)")
        else:
            l.append(str(i)+") "+my_list[i])

    text = "\n".join(l)
    bot.send_message(id, text)


def tekuch(id):
    global tek_n
    if tek_n in my_list:
        text = f"Делаем №{tek_n} : {my_list[tek_n]}"
    else:
        text = "Текущих дел нет"
    bot.send_message(id, text)


def zaversh(id):
    global tek_n
    if tek_n < len(my_list)+1:
        bot.send_message(id, f"Вы завершили дело № {tek_n}")
        now = datetime.datetime.now()
        my_list[tek_n] += f""" {now.strftime("%d-%m-%Y %H:%M")}"""
        tek_n += 1
    if tek_n >= len(my_list)+1:
        text = "Вы справились со всеми заданиями!"
    else:
        text = f"Переходим к следующему )"
    bot.send_message(id, text)


def zanovo(id):
    global tek_n, my_list
    tek_n = 1
    bot.send_message(id, "Начинаем сначала")
    my_list = work_list.copy()


bot.polling(none_stop=True, interval=0)
