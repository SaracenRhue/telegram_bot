from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from os import system as cmd
import yaml

TOWER = 'http://192.168.178.132'

with open('auth.yml', 'r') as file:
    auth = yaml.safe_load(file)
    USER = auth['toweruser']
    PASS = auth['password']

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