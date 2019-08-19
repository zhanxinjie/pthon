#元素定位
    #find_element_by_id("kw")
    #find_element_by_name("")
    #find_element_by_class_name("")
    #find_element_by_xpath("")


from selenium import webdriver
import time

path = r""
browser = webdriver.Chrome(path)

url = ""
browser.get(url)

time.sleep(3)

browser.find_element_by_id("").send_keys()
browser.find_element_by_id("").click()

time.sleep(10)
browser.quit()


