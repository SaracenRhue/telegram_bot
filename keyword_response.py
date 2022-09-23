from telegram import Update
from telegram.ext import *
from tower_actions import *
from chat_responses import *
import yaml 

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
    messages = config['messages']


# respond to tower commands
async def keyword_response(update: Update, context: ContextTypes.DEFAULT_TYPE):

    wrap_use_tower_shell_exists = True
    async def wrap_use_tower_shell(text):
        text = text.replace('$', '')
        await random_working_text(update, context)
        use_tower_shell(text)
        await random_done_text(update, context)

    wrap_random_stash_video_exists = True
    async def wrap_random_stash_video():
        await random_working_text(update, context)
        await send_text(random_stash_video(), update, context)
        await send_text('all right, have fun :)', update, context)

    wrap_tag_hqporner_exists = False

####################################################################################################        
# if no wrap_ function excists, random_working_text() and random_done_text() will be used by default
# if you create a wrap_ function you need to set the _exists variable to True
    text = update.message.text.lower()
    for i in messages:
        if len(messages[i]['trigger']) == 3:
            if messages[i]['trigger'][0] in text and messages[i]['trigger'][1] in text or messages[i]['trigger'][2] in text:
                if 'wrap_'+messages[i]['function']+'_exists' == True:
                    await eval('wrap_'+messages[i]['function'])
                else:
                    await random_working_text(update, context)
                    eval(messages[i]['function'])
                    await random_done_text(update, context)
                return True
        elif len(messages[i]['trigger']) == 2:
            if messages[i]['trigger'][0] in text and messages[i]['trigger'][1] in text:
                if 'wrap_'+messages[i]['function']+'_exists' == True:
                    await eval('wrap_'+messages[i]['function'])
                else:
                    await random_working_text(update, context)
                    eval(messages[i]['function'])
                    await random_done_text(update, context)
                return True
        elif len(messages[i]['trigger']) == 1:
            if messages[i]['trigger'][0] in text:
                if 'wrap_'+messages[i]['function']+'_exists' == True:
                    await eval('wrap_'+messages[i]['function'])
                else:
                    await random_working_text(update, context)
                    eval(messages[i]['function'])
                    await random_done_text(update, context)
                return True