#!/usr/bin/python3.5
#coding:utf8
 
 
import xlsxwriter as wx
import re           # 使用正则 匹配想要的数据
import cgi
import requests     # 使用requests得到网页源码
import os
import time
import urllib
 
 
page=1
downsuccess = 0
downfaild = 0
shop = [("店铺名称","商品","商品售价￥","商品购买数","产地","商品详情地址","商品展示图")]
 
shop2 = [("店铺名称","商品","商品售价￥","商品购买数","产地","商品详情地址","商品展示图")]
#用于生成EXCEL
detailpage = ""
#keyword="公仔"
 
keyword = input("[+] 输入搜索关键词：")
page = input("[+] 输入查找页数:")
 
url="https://s.taobao.com/search?q=%s"%(keyword)
now = time.strftime("%Y%m%d_%H%M%S")
imglocalpath=[("商品图示")] 
 
def getPicIMG(url,path,imgname):
    """
    下载商品展示图片
 
    """
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    try:
        imgdir = path+"/"+imgname.replace(".jpeg","")    
        os.mkdir(imgdir)
        imgdata = requests.get(url).content
        print("[*]下载图片：%s" % imgname)
        f = open(imgdir+"/"+imgname,"wb")
        f.write(imgdata)
        f.close()
        imglocalpath.append([imgdir+"/"+imgname])
        global downsuccess
        downsuccess += 1
    except:
        print("[!]啊哦出错了")
        global downfaild
        downfaild += 1
        pass
 
def getHTML(url,s):
    """
    获取HTML源代码
    """
    try:
        if s == 0:
            responText = requests.get(url) #第一页
        else:
            responText = requests.get(url+"&s=%s"%(str(44*s))) #其他页
        return responText
    except:
        return '"nice":"error"'
 
def get(url):
    """
    Http Get方法
    """
    try:
        respon = requestss.get(url)
        return respon
    except:
        return 1
 
 
def Regx(Text):
    """
    提取商品信息
     
    """
    #Text = str(Text)
    print(type(Text))
    Titleregx = re.findall('"raw_title":"(.*?)"',Text)
    PiceRegx = re.findall('"view_price":"([\d+.]*)"',Text)
    item_loc = re.findall('"item_loc":"(.*?)"',Text)
    nice = re.findall('"nick":"(.*?)"',Text)
    purl = re.findall('"pic_url":"(.*?)"',Text)
    detail = re.findall('"detail_url":"(.*?)"',Text)
    sales = re.findall('"view_sales":"(\d+.*?)"',Text)
    #shop.append([Titleregx.findall(Text),PiceRegx])
    for i in range(Titleregx.__len__()):
        imgurl = "https:"+purl[i]
        shop.append((nice[i],Titleregx[i],PiceRegx[i],sales[i],item_loc[i],"https:"+detail[i].replace("\\u003d","=").replace("\\u0026","&"),imgurl)) 
        shop2.append((nice[i],Titleregx[i],PiceRegx[i],sales[i],item_loc[i],"https:"+detail[i].replace("\\u003d","=").replace("\\u0026","&"),"./公仔"+now+"/"+Titleregx[i]+"/"+Titleregx[i]+".jpeg")) 
 
 
def writeexcel(path,dealcontent):
         """
         将数据插入Excel   
         """
         
         workbook = wx.Workbook(path)
         top = workbook.add_format({'border':1,'align':'center','bg_color':'white','font_size':11,'font_name': '微软雅黑'})
         red = workbook.add_format({'font_color':'white','border':1,'align':'center','bg_color':'800000','font_size':11,'font_name': '微软雅黑','bold':True})
         image = workbook.add_format({'border':1,'align':'center','bg_color':'white','font_size':11,'font_name': '微软雅黑'})
         formatt=top
         formatt.set_align('vcenter') #设置单元格垂直对齐
         worksheet = workbook.add_worksheet("Mr.RaoJL-商品爬虫-”"+keyword+"“详情表单")        #创建一个工作表对象
         width=len(dealcontent[0])
         worksheet.set_column(0,width,38.5)            #设定列的宽度为22像素
         for i in range(0,len(dealcontent)):
                 if i==0:
                         formatt=red
                 else:
                         formatt=top
                 for j in range(0,len(dealcontent[i])):
                         if i!=0 and j==len(dealcontent[i])-1:
                                 if dealcontent[i][j]=='':
                                         worksheet.write(i,j,' ',formatt)
                                 else:
                                         try:
                                                 worksheet.insert_image(i,j,dealcontent[i][j])
                                         except:
                                                 worksheet.write(i,j,' ',formatt)
                                                  
                         else:
                                 if dealcontent[i][j]:
                                         worksheet.write(i,j,dealcontent[i][j].replace(' ',''),formatt)
                                 else:
                                         worksheet.write(i,j,'无',formatt)
         workbook.close()
 
if __name__ == "__main__":
    HTML=""
    #keyword = input("[+] 输入搜索关键词：")
    #page = input("[+] 输入查找页数:")
    for i in range(0,int(page)):
        HTML+=getHTML(url,i).text
    Regx(HTML)
    detailtxt=open("detail_url.txt","w")
    nav = "{:8}\t{:18}\t{:4}\t{:16}\t{:32}\t{:32}\t{:32}"
    print(nav.format("店铺名","商品","价格","购买量","产地","商品图片","商品详情"))
    for i in shop:
        imgurl = i[6]
        imgname = i[1]
        path = keyword+now
        detailu = i[5]
        #print(nav.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        detailtxt.write("%s" % (detailu+"\n"))
        getPicIMG(imgurl,path,imgname+".jpeg")
    #print(len(shop))
    detailtxt.close()
    writeexcel("%s%s.xlsx"%(keyword,now),shop)
    print("[*]下载成功：%s" % str(downsuccess))
    print("[!]下载失败：%s" % str(downfaild))
