# -*- coding: utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
from dateutil.parser import parse
from BeautifulReport import BeautifulReport


class Test(unittest.TestCase):
    # 定义一个保存截图函数
    def save_img(self, img_name):
        self.browser.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath("E:\\pthon\\pthon\\test\\urllib\\img"), img_name))

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1920, 1080)
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间：", self.starttime)
        self.browser.get("https://www.baidu.com/")
        time.sleep(3)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        time.sleep(3)
        self.browser.quit()
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("总时长：", totaltime, "秒")

    # 测试用例1：必须以test_开头
    @BeautifulReport.add_test_img('打开登录页面', '输入账号密码', '登录')
    def test_01(self):
        u"""登录"""
        self.browser.find_element_by_xpath("//*[@id=\"u1\"]/a[7]").click()
        # 需要进行截图的时候，直接调用截图函数就ok，下同
        self.save_img('打开登录页面')
        self.browser.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__footerULoginBtn\"]").click()
        # self.browser.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        self.browser.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("userName")
        time.sleep(1)
        self.browser.find_element_by_id("TANGRAM__PSP_10__password").send_keys("password")
        time.sleep(1)
        self.save_img('输入账号密码')
        self.browser.find_element_by_id("TANGRAM__PSP_10__submit").click()
        time.sleep(1)
        self.save_img('登录')

    # 测试用例2：也是必须以test_开头
    @BeautifulReport.add_test_img('测试用例2')
    def test_02(self):
        u"""测试用例2"""
        self.save_img('测试用例2')
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()