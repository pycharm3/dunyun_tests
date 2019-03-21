# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 12:26
# @Author  : xuyun
import unittest,time,smtplib,os
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
filename = 'D:/test_demo/Test_DemoOne/manage/TestReport/' + writedata + 'jianshu&zhihu.html'
fp = open(filename,'wb')

runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=u'jianshu&zhihu',
    description=u'用例执行情况：'
)
# 执行测试用例
runner.run(testunit)
xmlrunner.XMLTestRunner(verbosity=2,output='测试报告').run(smoke_tests)