import logging
from telegram import Update
from telegram.ext import *
from os import system as cmd
from slash_cmds import *
from tower_cmds import *
from chat_responses import *

TOKEN = '5741907853:AAH4pPGe8khEWgMiGgs1Xy0pBKMuB7unzzE'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


application = ApplicationBuilder().token(TOKEN).build()

# handle slash commands
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)


# main bot function
async def bot_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await tower_response(update, context)
   await chat_response(update, context)




application.add_handler(MessageHandler(filters.TEXT, bot_response))
application.run_polling()