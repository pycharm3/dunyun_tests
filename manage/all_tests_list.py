# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 14:06
# @Author  : xuyun
import sys
sys.path.append("/template")
from template import zhihu_login,jianshu_login

def caselist():
    alltestnames = [
        zhihu_login.ZhihuLogin,
        jianshu_login.JSlogin,
    ]
    print("success read case list")
    return alltestnames
