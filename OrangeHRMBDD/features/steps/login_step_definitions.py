'''
Created on 14-Jun-2025

@author: admin
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Chrome browser is launched')
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options)
    context.driver.implicitly_wait(10)       


@when(u'User navigates to OrangeHRM Login page')
def navigate_to_orangehrm_login_page(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@when(u'User enters username')
def enter_username(context):
    username_bx = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    username_bx.send_keys("Admin")

@when(u'User enters password')
def enter_password(context):
    password_bx = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    password_bx.send_keys("admin123")


@when(u'User clicks on login button')
def click_on_login_button(context):
    login_btn = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    login_btn.click()        


@then(u'User should able to see dashboard/index in current page url')
def validate_dashboard_url(context):
    expected_url_member = "dashboard/index"
    actual_url = context.driver.current_url
    
    # context.assertIn(expected_url_member, actual_url, "Login failed")
    
    assert expected_url_member in actual_url, "Login failed"


@then(u'User should able to see auth/login in current page url')
def validate_login_page_url(context):
    expected_url_portion = "auth/login"
    actual_url = context.driver.current_url
    
    # context.assertIn(expected_url_portion, actual_url, "Navigation to OrangeHRM login page is failed")
    
    assert expected_url_portion in actual_url, "Navigation to OrangeHRM login page is failed"