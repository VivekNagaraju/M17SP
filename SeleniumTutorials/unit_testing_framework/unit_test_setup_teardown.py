'''
Created on 08-Jun-2025

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class OrangeHRMLoginTest(unittest.TestCase):


    def setUp(self):
        '''1. Launching the chrome browser'''
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options)
        self.driver.implicitly_wait(10)
        
        '''2. Navigating to OrangeHRM Login page'''
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    def tearDown(self):
        self.driver.quit()


    def test_navigation_to_login_page(self):
        '''3. Validate whether navigation is successful'''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login123"
        expected_url_portion = "auth/login"
        actual_url = self.driver.current_url
        
        # self.assertEqual(actual_url, expected_url, "Navigation to OrangeHRM login page is failed")
        self.assertIn(expected_url_portion, actual_url, "Navigation to OrangeHRM login page is failed")
    
    
    def test_orangehrm_login(self):
        '''3. enter user name '''
        username_bx = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username_bx.send_keys("Admin")
         
         
        '''4. Enter password'''
        
        password_bx = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password_bx.send_keys("admin123")
        
        '''5. Click on login btn'''
        
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_btn.click()
        
        '''6. Validate whether login is successful'''
        expected_url_member = "dashboard/index"
        actual_url = self.driver.current_url
        
        self.assertIn(expected_url_member, actual_url, "Login failed")
    


if __name__ == "__main__":
    import sys;sys.argv = ['', 'OrangeHRMLoginTest.test_navigation_to_login_page']
    unittest.main()
