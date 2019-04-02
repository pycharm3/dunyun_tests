# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 14:06
# @Author  : xuyun
import sys
sys.path.append("/template")
from template import zhihu_login,jianshu_login,dunyun_login

def caselist():
    alltestnames = [
        zhihu_login.ZhihuLogin,
        jianshu_login.JSlogin,
        dunyun_login.dunyun,
    ]
    print("success read case list")
    return alltestnames
