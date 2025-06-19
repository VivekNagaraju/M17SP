from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_btn_locator = (By.TAG_NAME, "button")
        
    def enter_username(self, username):
        self.enter_text(self.username_locator, username)
    
    def enter_password(self, password):
        self.enter_text(self.password_locator, password)
    
    def click_login(self):
        self.click_element(self.login_btn_locator)
