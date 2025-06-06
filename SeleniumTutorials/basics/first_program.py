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

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Validate the navigation is successfull'''
current_page_title=driver.title
print(current_page_title)

expected_page_title="Automation Testing Practice123"

if current_page_title == expected_page_title:
    print("Test is Passed!")
else:
    print("Test Failed!!")
