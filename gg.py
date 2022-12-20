import telebot
import random

from env import TOKEN

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start', 'hi'])
def start_func(message):
    msg = bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer_check)

def answer_check(msg):
    if msg.text == 'Да':
        bot.send_message(msg.chat.id, 'У тебя есть 3 попытки угадать число от 1 до 10')
        random_num = random.randint(1,10)
        popytka = 3
        start_game(msg, random_num, popytka)


    else:
        bot.send_message(msg.chat.id, 'Ну и иди нахуй >:(')

def start_game(msg, random_num, popytka):
    msg = bot.send_message(msg.chat.id, 'Введи число от 1 до 10: ')
    bot.register_next_step_handler(msg, check_func, random_num, popytka-1)

def check_func(msg, random_num, popytka):
    if msg.text == str(random_num):
        bot.send_message(msg.chat.id, 'Вы победили!')
    elif popytka == 0:
        bot.send_message(msg.chat.id, f'Вы проиграли! Число было - {random_num}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй еще раз, у тебя осталось {popytka} попыток')
        start_game(msg, random_num, popytka)
#     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJKBGOhPVmbKKYqXNfA7-hhYdvuzKZSAAKMGAACfebRS4ZKKHgWKbruLAQ')
#     bot.send_photo(message.chat.id, 'https://i.pinimg.com/564x/4f/a9/65/4fa965953eca58e83539070ba49bc800.jpg')

# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text)



bot.polling()