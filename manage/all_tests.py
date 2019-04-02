# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 12:26
# @Author  : xuyun
import sys
print(sys.path)
sys.path.append('D:\\test_demo\\Test_DemoOne\\manage')
sys.path.append('D:\\test_demo\\Test_DemoOne')
sys.path.append('D:\\Django_project\\Test_DemoOne\\Scripts\\python35.zip')
sys.path.append('D:\\virtualenvwrapper\\HttpRunner\\DLLs')
sys.path.append('D:\\virtualenvwrapper\\HttpRunner\\lib')
sys.path.append('D:\\virtualenvwrapper\\HttpRunner\\Scripts')
sys.path.append('c:\\users\\administrator\\appdata\\local\\programs\\python\\python35\\Lib')
sys.path.append('c:\\users\\administrator\\appdata\\local\\programs\\python\\python35\\DLLs')
sys.path.append('D:\\virtualenvwrapper\\HttpRunner')
sys.path.append('D:\\virtualenvwrapper\\HttpRunner\\lib\\site-packages')
sys.path.append('D:\\pycharm2018\\PyCharm 2018.1.4\\helpers\\pycharm_matplotlib_backend')
sys.path.append('D:\\virtualenvwrapper\\HttpRunner\\lib\\ntpath.py')

import unittest,time,smtplib,os,xmlrunner
from HTML_TestRunner import HTMLTestReportCN
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from template import jianshu_login,zhihu_login
from manage import all_tests_list
from email.header import Header

# 将用例组装数组
alltestnames = all_tests_list.caselist()
# 创建测试套件
testunit = unittest.TestSuite()
# 循环读取数组中的用例
for test in alltestnames:
    testunit.addTest(unittest.makeSuite(test))
# 定义测试报告命名规则
writedata = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 定义测试报告存放路径
# filename = 'D:/test_demo/Test_DemoOne/manage/TestReport/' + writedata + 'jianshu&zhihu.html'
# jenkins项目工作空间，例如：F:\jenkins\workspace\test\TestReport
filename = 'F:/jenkins/workspace/test/TestReport/' + 'jianshu&zhihu.html'
fp = open(filename,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=u'jianshu&zhihu',
    description=u'用例执行情况：'
)
# 执行测试用例
runner.run(testunit)
# xmlrunner.XMLTestRunner(verbosity=2,output='TestReport').run(testunit)