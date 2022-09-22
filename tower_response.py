from telegram import Update
from telegram.ext import *
from tower_actions import *
from chat_responses import *


# respond to tower commands
async def tower_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    text = text.replace('virtual machine', 'vm')
    if text.__contains__('vm') and text.__contains__('start') or text.__contains__('vm') and text.__contains__('stop') or text.__contains__('vm') and text.__contains__('toggle'):
        await random_working_text(update, context)
        toggle_vm()
        await random_done_text(update, context)
        return True

    elif text.__contains__('stash') or text.__contains__('tag') and text.__contains__('hqporner'):
        await random_working_text(update, context)
        tag_hqporner()
        await random_done_text(update, context)
        return True

    elif text.startswith('$'):
        text = text.replace('$', '')
        await send_text(f"ok I'm running {text} on the server", update, context)
        use_tower_shell(text)
        await random_done_text(update, context)
        return True

    elif text.__contains__('porn') or text.__contains__('horny'):
        await random_working_text(update, context)
        await send_text(random_stash_video(), update, context)
        await send_text('all right, have fun :)', update, context)
        return True

        