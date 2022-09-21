from telegram import Update
from telegram.ext import *
from os import system as cmd
from tower_actions import *
import yaml


# respond to tower commands
async def tower_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    text = text.replace('virtual machine', 'vm')
    if text.__contains__('vm') and text.__contains__('start') or text.__contains__('vm') and text.__contains__('stop') or text.__contains__('vm') and text.__contains__('toggle'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok I'm working on it")
        toggle_vm()
        return True
    elif text.__contains__('stash') or text.__contains__('tag') and text.__contains__('hqporner'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok I'm working on it")
        tag_hqporner()
        return True
    elif text.__contains__('$'):
        text = text.replace('$', '')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"ok I'm running {text}")
        use_shell(text)
        return True
    elif text.__contains__('porn') or text.__contains__('horny'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=random_stash_video())
        await context.bot.send_message(chat_id=update.effective_chat.id, text="All right, have fun :)")
        return True
        