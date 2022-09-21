from telegram import Update
from telegram.ext import *
from stash import *

async def send_text(output ,update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=output)