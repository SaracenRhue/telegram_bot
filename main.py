import logging
from telegram import Update
from telegram.ext import *
from os import system as cmd
from tower_response import *
from chat_responses import *
import yaml

with open('data.yml', 'r') as file:
    auth = yaml.safe_load(file)
    TOKEN = auth['token']


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok I'm working on it")
    

# handle slash commands
application.add_handler(CommandHandler('start', start))


# main bot function
async def bot_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await tower_response(update, context):
        return True
    else:
        await chat_response(update, context)

    




application.add_handler(MessageHandler(filters.TEXT, bot_response))
application.run_polling()