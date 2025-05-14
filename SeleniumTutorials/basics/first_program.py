'''
Created on 11-May-2025

@author: admin


'''
from selenium import webdriver
# from selenium.webdriver import Chrome, Edge


'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.get('https://selenium.dev/')