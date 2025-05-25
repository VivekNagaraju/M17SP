'''
Created on 25-May-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Creating an object from ActionChains class'''
actions = ActionChains(driver)

'''4. Scrolling'''
actions.scroll_by_amount(0, 1000).perform()

'''5. Mouse hover'''
point_me = driver.find_element(By.XPATH, '//*[@id="HTML3"]/div[1]/div/button')
actions.move_to_element(point_me).perform()

time.sleep(10)

'''6. Double click'''
copy_text_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
actions.double_click(copy_text_btn).perform()

'''7. Drag and drop'''
actions.scroll_by_amount(0, 500).perform()
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
actions.drag_and_drop(source, target).perform()

'''8. Slider'''
slider_right_box = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')
actions.drag_and_drop_by_offset(slider_right_box, 50, 0).perform()

'''9. Context click/ Right click'''
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
right_click_me_btn = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
actions.context_click(right_click_me_btn).perform()
