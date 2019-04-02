# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 9:26
# @Author  : xuyun
'''
dunyun登录退出
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,unittest
from HTML_TestRunner import HTMLTestRunner_jpg
from template import dunchong_login
from template import dy_login,dy_logout



class dunyun(unittest.TestCase):
    # setUp初始化
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.0.0.9/login"
        self.verificationErrors = []

    def test_login(self):
        u"""敦云login&&logout"""
        driver =self.driver
        driver.get(self.base_url)
        # 调用登录模块
        dy_login.login(self)
        # 调用退出模块
        dy_logout.logout(self)

if __name__ == "__main__":
    unittest.main()
