from selenium import webdriver #导入驱动，就是刚刚你下载那个浏览器驱动（你电脑要有浏览器哦）
wd=webdriver.Chrome()                                               #实例化
wd.get('https://www.baidu.com/')                                 #在浏览器中输入百度网址
wd.find_element_by_xpath('//*[@id="kw"]').send_keys("博客园")     #在百度中输入“博客园”
wd.find_element_by_xpath('//*[@id="su"]').click()                  #点击“百度一下”按钮