from telegram import Update
from telegram.ext import *
from os import system as cmd


# respond to tower commands
async def tower_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    text = text.replace('virtual machine', 'vm')
    if text.__contains__('vm') and text.__contains__('start') or text.__contains__('vm') and text.__contains__('stop') or text.__contains__('vm') and text.__contains__('toggle'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok I'm working on it")
        cmd('python3 ./tower/toggle_vm.py')
        