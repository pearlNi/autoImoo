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
        # 登录前的cookie
        cookie1 = self.driver.get_cookies()
        print('11111111111111', cookie1)

    def test_login(self):
        self.driver.find_element_by_id('js-signin-btn').click()
        time.sleep(10)
        uName_tag = self.driver.find_element_by_name("email")
        uPwd_tag = self.driver.find_element_by_name("password")
        uName_tag.click()
        uName_tag.send_keys('927082374@qq.com')
        time.sleep(5)
        uPwd_tag.click()
        uPwd_tag.send_keys('Niyanzhu007/')
        time.sleep(5)
        self.driver.find_element_by_class_name('xa-login').click()
        time.sleep(10)
        # 获取登录后的cookie 方便跳过验证码
        cookie2 = self.driver.get_cookies()
        print('**********22222', cookie2)
        result = self.driver.find_element_by_xpath("//div[@id='login-area']/ul/li[4]/a/span").text
    #   断言
        self.assertEqual(result, self.expect_result)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()