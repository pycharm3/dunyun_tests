# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 17:48
# @Author  : xuyun
import unittest,time,os,multiprocessing,sys
sys.path.append('\Test_DemoOne\Test')
from HTML_TestRunner import HTMLTestReportCN
from multiprocessing import Process

# 创建一个函数
def listcase():
    # 定义一个数组casedir
    casedir = []
    # 读取这个路径下文件
    listos = os.listdir("D:/test_demo/Test_DemoOne/Test/")
    # 遍历读取到的文件listos，
    for casedemo in listos:
        # 把读取到的文件/文件夹包含Thread的添加到casedir中
        # if in ThreadDemo是否在casedemo中
        if "ThreadDemo" in casedemo:
            # .appedn添加
            casedir.append(casedemo)
            # 输出casedir
    print(casedir)
    # 定义suite数组
    suite=[]
    # for循环读取casedir中的数据（即ThreadDemoOne和ThreadDemoTwo两个文件夹)
    for n in casedir:

        testunit = unittest.TestSuite()
        # 通过discover分别读取ThreadDemoOne和ThreadDemoTwo文件夹下匹配到"*_login.py"的文件
        discover=unittest.defaultTestLoader.discover(str(n),pattern='*_login.py',top_level_dir=r'D:/test_demo/Test_DemoOne/')
        # 循环读取discover
        for test_unit in discover:
            # 循环读取test_unit
            for test_case in test_unit:
                # 将所有用例文件添加到testunit测试套件中
                testunit.addTest(test_case)
                # 再将测试套件追加到suite数组中
        suite.append(testunit)
        # 返回suite,casedir两个数组的值
    return suite,casedir

# 定义runcase函数
def runcase(suite,casedir):
    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    filename = 'D:/test_demo/Test_DemoOne/manage/TestReport/' + now + 'ThreadTestDemo.html'
    fp = open(filename,'wb')

    proclist = []
    s = 0
    # for循环把suite数组中的用例执行结果写入HTMLTestRunner测试报告中
    for i in suite:
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=fp,
            title=str(casedir[s])+u'测试报告',
            description=u'用例执行情况: '
        )
    # multiprocessing.Process创建用例执行的多进程,
    proc = multiprocessing.Process(target=runcase,args=(suite,casedir))
    # 把创建的多线程追加到proclist数组中
    proclist.append(proc)
    s = s+1
    # for循环proc.start()开始进程活动，proc.join()终止进程活动
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
    # 关闭fileOpen流
    fp.close()


if __name__ == '__main__':
    runtmp = listcase()
    runcase(runtmp[0],runtmp[1])
