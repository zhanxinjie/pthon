#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 14:36
# @Author  : Xuegod Teacher For
# @File    : 01_bibao_test.py
# @Software: PyCharm
def outer(num):
    def inner(num_in):
        print('inner,num_in is %d'%num_in)
        return num+num_in
    return inner

# outer()()
a = outer(20)
# print(a)
print(a(200))


#闭包 就是在吧签到函数，在外部进行执行