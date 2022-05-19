# testLogin 2022-05-17 by Pearl
# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.imooc.com/")
        self.driver.implicitly_wait(15)

    def test_login(self):
        self.driver.find_element_by_id('js-signin-btn').click()
        time.sleep(10)
        uName_tag = self.driver.find_element_by_name("email")
        uPwd_tag = self.driver.find_element_by_name("password")
        self.driver.find_element_by_class_name('xa-login').click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    # test_login('927082374@qq.com', 'Niyanzhu007.')
    unittest.main()