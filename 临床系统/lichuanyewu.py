'''
Created on 2018年11月06日

@author: zxj
'''
# coding=utf-8
import unittest ## 引入unittest模组
from selenium import webdriver  ## 引入WebDriver的包，才能使用 webdriver API 进行自动化脚本开发
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def browser(browser='chrome'):
# '''
# open browser "firefox"、"chrome"、"ie"、"phantomjs"
# usage:
# driver = browser("chorme")
# '''
  try:
      if browser == "firefox":
          driver = webdriver.Firefox()
          return driver
      elif browser == "chrome":
          driver = webdriver.Chrome()
          return driver
      elif browser == "ie":
          driver = webdriver.Ie()
          return driver
      elif browser == "phantomjs":
          driver = webdriver,PhantomJS()
          return driver
      else: 
          #print("Not found browser!You can enter 'firefox' , 'chrome' , 'ie' or 'phantomjs'")
          print("没有找到浏览器！你可以选择火狐，谷歌，ie浏览器或者phantomjs")
  except Exception as msg:
          print("打开浏览器出错:%s" % msg)

class Web_OSCE_Tests(unittest.TestCase):
    
    ## 使用'@'修饰符，注明该方法是类的方法
    ## setUpClass方法是在执行测试之前需要先调用的方法
    ## 是开始测试前的初始化工作
    @classmethod
    def setUpClass(self):
        # 默认启动Chrome
        self.driver = browser()
        time.sleep(2)
##        self.driver.maximize_window()
##        print("打开浏览器:%s" % self.driver.name)
        print(" -- set up finished -- ")
        print()

        url = "http://47.107.82.25"
        # 导航到临床业务系统的主页
        self.driver.get(url)
        print(self.driver.title)
        
    def test_01_admin_login(self):
        username = self.driver.find_element_by_id("username")
        userpass = self.driver.find_element_by_id("password")
        loginbtn = self.driver.find_element_by_id("loginbtn")

        username.clear()
        userpass.clear()
        time.sleep(3)

        username.send_keys("admin")#输入帐号
        userpass.send_keys("jfr2019")#输入密码
        time.sleep(2)
        loginbtn.click()#点击登录按钮
        time.sleep(2)
        print("登录成功")
        print("-- test 01 finished -- ")
        print()

    def test_02_add(self,url):
        self.driver.get("http://47.107.82.25/backstage/index.jsp/")
        self.driver.find_element_by_link_text('后台管理').click()
        time.sleep(10)
        
        self.driver.get("http://47.107.82.25/Subject.action/")
        time.sleep(10)
        self.driver.find_element_by_link_text('新增').click()
        time.sleep(10)
##        self.driver.find_element_by_id("menu_base_info").click()
##        self.driver.find_element_by_link_text('课程类型').click()
##        username = self.driver.find_element_by_id("username")


    @classmethod
    def tearDownClass(self):
        #close the browser window
        js = 'javascript:logout(17005)'
        self.driver.execute_script(js)

        self.driver.quit()## 关闭浏览器
        pass
        print('-- tear down finished -- ')
        print()

if __name__ == '__main__':
    ## 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)

