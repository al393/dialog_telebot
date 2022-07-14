import telebot
from telebot import types
from settings import TOKEN
from game import Game


bot = telebot.TeleBot(TOKEN)
userbot_dict = {}


@bot.message_handler(commands=["start"])
def start(m, res=False):
    global userbot_dict
    userbot_dict[m.chat.id] = Game(m.chat.id, m.chat.first_name)
    userbot = userbot_dict[m.chat.id]
    bot.send_message(m.chat.id, f"Привет {userbot.user_name},\nу нас есть новый список заданий!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Посмотреть весь список")
    item2 = types.KeyboardButton("Текущее задание")
    item3 = types.KeyboardButton("Завершить текущее")
    item4 = types.KeyboardButton("Начать заново")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)

    bot.send_message(m.chat.id, 'Выберите действие', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    userbot = userbot_dict[message.chat.id]
    text = ""
    if not userbot:
        userbot = Game(message.chat.id, message.chat.first_name)
    if message.text.strip() == "Посмотреть весь список":
        text = userbot.output_list()
    elif message.text.strip() == "Текущее задание":
        text = userbot.now_task()
    elif message.text.strip() == "Завершить текущее":
        text = userbot.now_finish()
    elif message.text.strip() == "Начать заново":
        text = userbot.reset()
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True, interval=0)
