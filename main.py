import logging
from telegram import Update
from telegram.ext import *
from tower_response import *
from chat_responses import *
from slash_actions import *
import yaml

with open('data.yml', 'r') as file:
    auth = yaml.safe_load(file)
    TOKEN = auth['token']


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token(TOKEN).build()
    
# main bot function
async def bot_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await tower_response(update, context):
        return True
    else:
        await chat_response(update, context)



# handle slash commands
# generate handler for each command from config.yml (slash)
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
    slash = config['slash']
    for i in slash:
        trigger = slash[i]['trigger']
        function = eval(slash[i]['function']) # convert string to function name
        application.add_handler(CommandHandler(trigger, function))

# handle normal messages
application.add_handler(MessageHandler(filters.TEXT, bot_response))
# start the bot
application.run_polling()