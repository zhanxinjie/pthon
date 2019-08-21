#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 14:56
# @Author  : Xuegod Teacher For
# @File    : 02_dec_test.py
# @Software: PyCharm

def outer(func):# func == func1
    def inner():
        func() # func() == func1()
        print('I come from china')
    return inner

 #func1 = outer(func1)
@outer # func1 = outer(func1)
def func1():
    print('this is xuegod1')
#
# def func2():
#     print('this is xuegod2')

# func1 = outer(func1)
# # print(f1)
# func1()

func1()