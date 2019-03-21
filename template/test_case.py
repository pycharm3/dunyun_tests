# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 16:10
# @Author  : xuyun
import os

caselist = os.listdir('D:/test_demo/Test_DemoOne/template')
print(caselist)
for pylist in caselist:
    s = pylist.split(".")[1]
    if s == 'py':
        os.system('python D:/test_demo/Test_DemoOne/template/%s 1>>log.txt 2>&1'%pylist)


