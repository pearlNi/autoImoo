# testLogin 2022-05-17 by Pearl
# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LoginSuccessTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.imooc.com/")
        self.driver.implicitly_wait(15)
        self.expect_result = u'我的课程'

    def test_login(self):
        self.driver.find_element_by_id('js-signin-btn').click()
        time.sleep(10)
        uName_tag = self.driver.find_element_by_name("email")
        uPwd_tag = self.driver.find_element_by_name("password")
        uName_tag.click()
        uName_tag.send_keys('12345678@qq.com')
        time.sleep(5)
        uPwd_tag.click()
        uPwd_tag.send_keys('xxx')
        time.sleep(5)
        self.driver.find_element_by_class_name('xa-login').click()
        time.sleep(10)

        result = self.driver.find_element_by_xpath("//div[@id='login-area']/ul/li[4]/a/span").text
        # print('expect_result' + self.expect_result)
        # print('result' + result)
    #   断言
        self.assertEqual(result, self.expect_result)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()