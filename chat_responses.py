from telegram import Update
from telegram.ext import *
import datetime

current_time = datetime.datetime.now()
response = ''

# respond normal messages
async def chat_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text.__contains__('hi') or text.__contains__('hello') or text.__contains__('hey'):
        response = 'Hello'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
