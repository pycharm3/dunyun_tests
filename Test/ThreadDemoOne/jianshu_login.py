# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 11:56
# @Author  : xuyun

from selenium import webdriver
import time,unittest


class JSlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.jianshu.com/sign_in"
        self.driver.maximize_window()

    def testlogin(self):
        u"""简书登录"""
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        driver.find_element_by_xpath('//*[@id="session_email_or_mobile_number"]').send_keys('18158144399')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="session_password"]').send_keys('Xadmin123')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="sign-in-form-submit-btn"]').submit()
        print(driver.current_url)

if __name__ == "__main__":
   unittest.main()
