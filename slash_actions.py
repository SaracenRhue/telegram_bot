from telegram import Update
from telegram.ext import *
from os import system as cmd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from chat_responses import *
import yaml


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok I'm working on it")


## toggle gaming vm
async def toggle_vm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await random_working_text(update, context)
    TOWER = 'http://192.168.178.132'

    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        USER = data['toweruser']
        PASS = data['towerpassword']

    driver = webdriver.Firefox()
    driver.get(TOWER)
    sleep(1)

    # login
    driver.find_elements(by=By.TAG_NAME, value='input')[0].send_keys(USER)
    driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(PASS)
    driver.find_elements(by=By.TAG_NAME, value='button')[0].click()
    #switch to virtual machines
    driver.get(TOWER+'/VMs')
    sleep(1)
    # open vm dropdown
    vm_icon = driver.find_elements(by=By.TAG_NAME, value='img')[3]
    vm_icon.click()
    sleep(1)
    # toggle vm
    toggle_icon = driver.find_elements(by=By.TAG_NAME, value='li')[6]
    toggle_icon.click()
    # close browser
    driver.close()
    cmd('pkill firefox')
    await random_working_text(update, context)


# /vsc command
# reinstall code-server 
async def reinst_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await random_working_text(update, context)
    TOWER = 'http://192.168.178.132'
    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        USER = data['toweruser']
        PASS = data['towerpassword']
    driver = webdriver.Firefox()
    driver.get(TOWER)
    # login
    driver.find_elements(by=By.TAG_NAME, value='input')[0].send_keys(USER)
    driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(PASS)
    driver.find_elements(by=By.TAG_NAME, value='button')[0].click()
    #switch to terminal
    driver.get(TOWER+'/logterminal/code-server/')
    sleep(1)
    terminal = driver.find_element(by=By.TAG_NAME, value='textarea')
    terminal.send_keys('bash -c "$(curl -fsSL https://raw.githubusercontent.com/SaracenRhue/unraidScripts/main/codeserver.sh)"')
    terminal.send_keys('\n')
    await random_done_text(update, context)
