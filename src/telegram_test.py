# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-12-10 19:19:12
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-10 20:17:10

import logging

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

API = '321593047:AAHu3OSD71i8II0exHJGFTkVIxwOtvEGJlo'

updater = Updater(token=API)
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

print "Starting bot"
updater.start_polling()




