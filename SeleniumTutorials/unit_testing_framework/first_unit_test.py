'''
Created on 07-Jun-2025

@author: admin
'''
import unittest
from selenium import webdriver

class OrangeHRMLoginTest(unittest.TestCase):


    def test_navigation_to_login_page(self):
        '''1. Launching the chrome browser'''
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        
        '''2. Navigating to OrangeHRM Login page'''
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
        '''3. Validate whether navigation is successful'''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login123"
        expected_url_portion = "auth/login"
        actual_url = driver.current_url
        
        # self.assertEqual(actual_url, expected_url, "Navigation to OrangeHRM login page is failed")
        self.assertIn(expected_url_portion, actual_url, "Navigation to OrangeHRM login page is failed")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()