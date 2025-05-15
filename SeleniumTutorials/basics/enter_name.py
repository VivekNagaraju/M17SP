'''
Created on 15-May-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Enter name'''
name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("Vivek")
# name_txt_bx.click() # This is just an example syntax for clicking an web element