import requests
import telebot
from base import Database


token = 'p1124233516:AAGM_htHVW95qXsQzb0C8e3zE1TGsi2u6nI'
bot = telebot.TeleBot(token)
GROUP_ID = '63904903'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ct = "Привет! Я слежу за сайтами Mystream для оповещении о падении.\nКоманда для вывода всех команд нажмите /help"
    bot.send_message(message.chat.id, ct)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    ct = "Доступные команды:" \
         "\n/list - выводит все отслеживаемые сайты" \
         "\n/check - бот проходит по всем сайтам независимо от таймера" \
         "\n/add - добавляет страницу" \
         "\n/remove - удаляет страницу"
    bot.send_message(message.chat.id, ct)

@bot.message_handler(commands=['check'])
def check(message):
    sites = Database.all(())
    ct = f'Отслеживаю сайты\n{sites}'
    bot.send_message(message.chat.id, ct)



#
# @bot.message_handler(commands=['site'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f'Слежу за сайтами: {page}')
#
#
# def tg(message):
#     ms = bot.send_message(message, message.text)
#     return ms




# bot.polling(none_stop=True, interval=0)