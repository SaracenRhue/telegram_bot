from telegram import Update
from telegram.ext import *
import datetime
import random
import yaml

current_time = datetime.datetime.now()
response = ''

# respond normal messages
async def chat_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text.__contains__('hi') or text.__contains__('hello') or text.__contains__('hey'):
        response = 'Hello'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

########################################################################################

with open('chat.yml', 'r') as file:
    chat = yaml.safe_load(file)


# send text
async def send_text(message, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# send random working text
async def random_working_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    working = chat['working']
    msg = working[random.randint(0, len(working) - 1)]
    await send_text(msg, update, context)


# send random done text
async def random_done_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    done = chat['done']
    msg = done[random.randint(0, len(done) - 1)]
    await send_text(msg, update, context)