# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 17:14
# @Author  : xuyun
from time import sleep,ctime
import threading

loops = [4,2]
# 参数依次为：nloop标识，nsec睡眠时间,lock线程锁
def loop(nloop,nsec):
    # 打印输出nloop
    print('start loop',nloop,'st: ',ctime())
    # 等待nsec秒
    sleep(nsec)
    # 打印输出nloop
    print('loop',nloop,'done at:',ctime())

def main():
    print('我是main',ctime())
    threads = []
    nloops = range(len(loops))
# 创建线程
    for i in nloops:
        # threading.Thread（创建一个新的线程)
        # target=(需要线程去执行的方法名)
        # args=(线程执行方法接受的参数，该属性是一个元组)
        t = threading.Thread(target=loop,args=(i,loops[i]))
        # 添加线程到线程列表
        threads.append(t)
    # 遍历nloop线程
    for i in nloops:
        # .start(）启动线程
        threads[i].start()
# 遍历启动线程并join()结束线程
    for i in nloops:
        threads[i].join()
    # 输出线程启动结束后的当前时间
    print("all en",ctime())

if __name__ == '__main__':
    main()