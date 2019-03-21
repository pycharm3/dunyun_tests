# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 9:41
# @Author  : xuyun
import time
# 分模块话退出
def logout(self):
    driver = self.driver
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[2]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[2]/li[2]/ul/li[3]/a').click()
    time.sleep(2)

