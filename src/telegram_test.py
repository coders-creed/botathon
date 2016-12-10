# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-12-10 19:19:12
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-11 00:07:17

import logging

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram.ext import InlineQueryHandler

from telegram import InlineQueryResultArticle, InputTextMessageContent

from info.fetch_info import *
from data_helpers import *

def initialize_bot():
	new_port = Portfolio([], 100000)
	create_companies()
	new_port.add_position(Position(Company.companies[0], 1000, 200))
	new_port.add_position(Position(Company.companies[1], 2000, 100))
	return

initialize_bot()



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

API = '321593047:AAHu3OSD71i8II0exHJGFTkVIxwOtvEGJlo'

updater = Updater(token=API)
dispatcher = updater.dispatcher

def start(bot, update):
	print "Userid: %d" %(update.message.chat_id)
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
	print args
	text_caps = ' '.join(args).upper()
	bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def inline_caps(bot, update):
	query = update.inline_query.query

	if not query:
		return
	
	results = [
		InlineQueryResultArticle(
			id=query.upper(),
			title='Caps',
			input_message_content=InputTextMessageContent(query.upper())
			)
		]
	bot.answerInlineQuery(update.inline_query.id, results)

# command handlers
start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps, pass_args=True)
info_handler = CommandHandler('info', send_info_handler, pass_args=True)
# inline handlers
inline_caps_handler = InlineQueryHandler(inline_caps)

# message handlers
echo_handler = MessageHandler(Filters.text, echo)

# add handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(info_handler)

print "Starting bot"
updater.start_polling()
updater.idle()




