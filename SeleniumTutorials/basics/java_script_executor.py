'''
Created on 03-Jun-2025

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
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Enter date in Date Picker 2'''
driver.execute_script('document.getElementById("txtDate").removeAttribute("readonly")')

date_picker_2 = driver.find_element(By.ID, 'txtDate')
date_picker_2.send_keys("03/06/2025")