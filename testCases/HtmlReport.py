# coding:utf-8
import unittest
import HTMLTestRunner
from time import strftime, localtime, time
from loginSuccess import *
from loginFail import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# suite = unittest.TestSuite()
suite1 = unittest.TestLoader().loadTestsFromTestCase(LoginSuccessTestCase)
suite2 = unittest.TestLoader().loadTestsFromTestCase(LoginFailTestCase)
suite = unittest.TestSuite([suite1, suite2])

# 把测试用例添加到测试容器中
now = strftime("%Y-%m-%M-%H_%M_%S", localtime())
# 获取当前时间
filename = now + "test.html"
# 文件名

fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title="测试报告",
    description="测试报告的详情")

runner.run(suite)
