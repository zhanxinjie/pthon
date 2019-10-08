# -*- coding: utf-8 -*-  
""" 
Created on Fri Oct 20 20:07:36 2017 
 
@author: eastmount CSDN 杨秀璋 
"""  
  
import urllib
import urllib.request
from bs4 import BeautifulSoup  
import csv  
import codecs  
  
c = open("test.csv","w", newline='',encoding='utf-8')    #创建文件  
writer = csv.writer(c, dialect='excel')       #写入对象
writer.writerow(['产品','价格','单位','批发地','时间'])  
  
i = 1  
while i <= 1:  
    print ("爬取第" + str(i) + "页")  
    url = "http://www.gznw.gov.cn/priceInfo/getPriceInfoByAreaId.jx?areaid=22572&page=" + str(i)  
    content = urllib.request.urlopen(url).read().decode('utf8')  
    soup = BeautifulSoup(content,"html.parser")  
    print (soup.title.get_text()  )
    tt = soup.find_all("tr",class_="odd gradeX")  
    for t in tt:  
        content = t.get_text()  
        num = content.splitlines()  
        print (num[0],num[1],num[2],num[3],num[4],num[5] ) 
        #写入文件  
        templist = []  
        num[1] =  num[1]  
        num[2] =  num[2]          
        num[3] =  num[3] 
        num[4] =  num[4] 
        num[5] =  num[5]  
        templist.append(num[1])  
        templist.append(num[2])  
        templist.append(num[3])  
        templist.append(num[4])  
        templist.append(num[5])  
        #print templist  
        writer.writerow(templist)  
    i = i + 1  
  
c.close()  
