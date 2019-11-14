#!/usr/bin/env python
from random import random
import telebot
from telebot import types
import pickle
TOKEN = "1017990097:AAElNj1B7B32LI_5fwyWf6cVsH3Cdw_WVBY"
STIKER = 'CAADAgADKAAD87rOFmRQa3FFfzqAFgQ'
bot = telebot.TeleBot(TOKEN)

USERS = {
    2232323
    }

@bot.message_handler(commands = ['start', 'help'])
def command_handler(message: "Message"):
    bot.reply_to(message, "dede")

    
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=["text"])
def echo_d(message: "Message"):
    txt = message.text
    reply = ""
    if txt == "1":
        reply = str(random())
        return
    reply = str(random())
    if message.from_user.id in USERS:
        reply += f" hello again"
    bot.reply_to(message, reply)
    USERS.add(message.from_user.id)
    print(USERS)

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_sticker(message.chat.id, STIKER)

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        print(1)
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

bot.polling(timeout = 60)
