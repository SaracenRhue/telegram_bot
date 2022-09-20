from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from os import system as cmd

TOWER = 'http://192.168.178.132'

driver = webdriver.Firefox()
driver.get(TOWER)
sleep(1)

# login
username = driver.find_elements(by=By.TAG_NAME, value='input')[0]
username.send_keys('root')
password = driver.find_elements(by=By.TAG_NAME, value='input')[1]
password.send_keys('Bazinga!73')
driver.find_elements(by=By.TAG_NAME, value='button')[0].click()
#switch to virtual machines
driver.get(TOWER+'/VMs')
sleep(1)
vm_icon = driver.find_elements(by=By.TAG_NAME, value='img')[3]
vm_icon.click()
sleep(1)
toggle_icon = driver.find_elements(by=By.TAG_NAME, value='li')[6]
toggle_icon.click()

driver.close()
cmd('fkill firefox')