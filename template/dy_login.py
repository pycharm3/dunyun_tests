# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 9:47
# @Author  : xuyun
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,unittest

# duyun分模块化登录模块
def login(self,name='admin',pw='123456'):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(pw)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="user"]/div[3]/div/input').send_keys("000000")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
    time.sleep(2)