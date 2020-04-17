# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])

def welcome(message):
	bot.send_message(message.user.id, 'ghb')

@bot.message_handler(commands=['getid'])

def command_getid(message):
    cid = message.chat.id
    bot.send_message(cid, str(message.chat.id) + " " + message.from_user.username)



bot.polling(none_stop=True)


