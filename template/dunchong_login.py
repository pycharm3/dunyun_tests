# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 15:35
# @Author  : xuyun

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,unittest

class loginuser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.0.0.9/login"
        self.driver.get(self.base_url)
    def testlogin(self):
        driver = self.driver
        print('4555')
        driver.get("https://10.0.0.9/login")
        driver.maximize_window()
        # 登录
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("MadeinChina2020")
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys("Xadmin123")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="user"]/div[3]/div/input').send_keys("000000")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        # 添加智能等待
        WebDriverWait(driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None)
        cookie = driver.get_cookies()
        print(cookie)
        print(driver.current_url)
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()