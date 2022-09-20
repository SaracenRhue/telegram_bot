from telegram import Update
from telegram.ext import *
from os import system as cmd

#respond to slash commands

# respond to /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
