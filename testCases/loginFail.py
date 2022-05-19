# testLogin 2022-05-17 by Pearl
# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class LoginFailTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.imooc.com/")
        self.driver.implicitly_wait(15)
    # 用户名、密码为空
    def test_login_null(self):
        self.driver.find_element_by_id('js-signin-btn').click()
        self.driver.find_element_by_class_name('xa-login').click()
        time.sleep(5)
        result = self.driver.find_element_by_css_selector('p.errorHint').text
        respect_result = u'请输入正确的邮箱或手机号'
        self.assertEqual(result, respect_result)
    # 密码为空
    def test_login_nPwd(self):
        self.driver.find_element_by_id('js-signin-btn').click()
        self.driver.find_element_by_name("email").send_keys('12345678@qq.com')
        self.driver.find_element_by_class_name('xa-login').click()
        time.sleep(5)
        result = self.driver.find_element_by_xpath("//form[@id='signup-form']/div[2]/p").text
        respect_result = u'请输入6-20位密码，区分大小写，不能使用空格！'
        self.assertEqual(result, respect_result)
    # 密码错误
    def test_login_fPwd(self):
        self.driver.find_element_by_id('js-signin-btn').click()
        self.driver.find_element_by_name("email").send_keys('12345678@qq.com')
        time.sleep(5)
        self.driver.find_element_by_name("password").send_keys('12345678@qq.com')
        time.sleep(5)
        self.driver.find_element_by_class_name('xa-login').click()
        time.sleep(5)
        result = self.driver.find_element_by_class_name('rlf-tip-error').text
        respect_result = u'请求超时'
        print('result' + result)
        print('respect_result' + respect_result)
        self.assertEqual(result, respect_result)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()