# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 19:26
# @Author  : xuyun
from selenium import webdriver
import unittest,time

class ZhihuLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = ("https://www.zhihu.com/signup?next=%2F")
        self.driver.maximize_window()
    def testlogin(self):
        u"""知乎登录"""
        driver = self.driver
        driver.get(self.base_url)
        # iframe = driver.find_element_by_xpath('//*[@id="frameforlogin"]')
        # driver.switch_to.frame(iframe)
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys("18158144399")
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys("Xadmin123")
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()
        print(driver.current_url)
        time.sleep(5)

if __name__ == "__main__":
    unittest.main(verbosity=2)

        # try:
        #     browser.find_element_by_id("kwsss").send_keys("selenium")
        #     browser.find_element_by_id("su").click()
        # except:
        #     browser.get_screenshot_as_file(u"D://test_demo//error.png")
        #     browser.quit()