# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 15:35
# @Author  : xuyun
'''
dunyun登录10.0.0.9
'''
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
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("1234567")
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

        # driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[5]/a').click()
        # b1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[5]/a').text
        # b = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div').text
        # print("\n")
        # print(b1)
        # print(b)
        #
        # driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a').click()
        # A1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a').text
        # A = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div').text
        # print("\n")
        # print(A1)
        # print(A)


        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[3]/a').click()
        c1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[3]/a').text
        c = driver.find_element_by_xpath('//*[@id="treeMenu"]').text
        print("\n")
        print(c1)
        print(c)

        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a').click()
        d1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a').text
        d = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div').text
        print("\n")
        print(d1)
        print(d)

        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').click()
        e1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').text
        e = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div').text
        print("\n")
        print(e1)
        print(e)


if __name__ == "__main__":
    unittest.main()