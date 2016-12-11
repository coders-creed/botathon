# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-12-10 19:19:12
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-11 13:45:56

import logging

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram.ext import CallbackQueryHandler

from telegram import InlineQueryResultArticle, InputTextMessageContent

from info.fetch_info import *
from actions.trade import *
from data_helpers import *

from info import sector

def initialize_bot():
	new_port = Portfolio([], 108761231899)
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

# command handlers
start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps, pass_args=True)
info_handler = CommandHandler('info', send_info_handler, pass_args=True)
buy_handler = CommandHandler('buy', buy_shares, pass_args=True)
sector_handler = CommandHandler('sector', sector.sector_main, pass_args=True)

def button(bot, update):
    query = update.callback_query
    action, arg = query.data.split('-')


    print action, arg

    if action == 'BUY':
	    # bot.editMessageText(text="Selected option: %s" % query.data,
	    #                     chat_id=query.message.chat_id,
	    #                     message_id=query.message.message_id)
	    if arg == 'Y': complete_buy()
	# elif action == 'SELL':
	#     if arg == 'Y': complete_sell()

# message handlers
echo_handler = MessageHandler(Filters.text, echo)

# add handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(buy_handler)
dispatcher.add_handler(sector_handler)
dispatcher.add_handler(CallbackQueryHandler(button))

print "Starting bot"
updater.start_polling()
updater.idle()




