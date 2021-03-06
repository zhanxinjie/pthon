# encoding:utf-8
import requests             # 使用requests得到网页源码
import re                   # 使用正则匹配想要的数据
import json
from xlwt import Workbook
import xlrd
import time
import csv

import threading
import pprint

import xlsxwriter as wx


class spider:
    def __init__(self,sid,name):
      
        self.id = sid        #天猫宝贝ID
        self.headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"https://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }                #请求头herders 'User-Agent':请求方式
                             #  'referer':从哪个链接跳转进来的
 
        self.name=name

    def openurl(self,url):
         
        self.request = requests.get(url,headers = self.headers)
        #建立连接
        #url：起始的地址，也就是访问的第一个页面
        #headers：请求头，告诉服务器是谁来了。
        #requests.get：一个方法能获取all_url的页面内容并且返回内容。

        if self.request.ok:
            return self.request.text
        
    def matchs(self):

        tmall_exp = r"Setup\(([\s\S]+?)\);"### 匹配 商品数据的正则
        detail = r"src=\"(https://img\S+?[jpgifn]+?)\""  ###匹配 商品详情图的正则
        
        html = self.openurl("https://detail.tmall.com/item.htm?id=%s"%self.id)
##        print(html)
        data = re.findall(tmall_exp,html)
        data = json.loads(data[0])
        
##        print(data)
        self.itemDO_info = data['itemDO']
##        print("商品详情信息：%s"%self.itemDO_info)
##        print("网址ID:%s："%self.id + self.itemDO_info['title'])

        main_img = data['propertyPics'] ## 这里包括了主图和颜色图的地址
        color_data = data['valItemInfo'] ['skuList']  ### 这里获得商品的颜色信息列表   包括颜色编码        颜色名称,商品skuID  
##        print("主图和颜色图的地址：%s"%main_img)
##        print("商品的颜色信息列表：%s"%color_data)
        
        pvs_all = re.findall('"pvs":"(.*?)"',self.request.text)
        
##        pvs_info = pvs_all[0]+";"+pvs_all[1]+";"+pvs_all[2]
        
        self.pvs_info = str(pvs_all).replace("'", '').replace(", ", ';').replace("[", '').replace("]", '')
##        print( self.pvs_info )

        skuMap = data['valItemInfo']['skuMap']
##        print( skuMap )

        detail_html = self.openurl("http:"+data['api']["httpsDescUrl"])
        self.detail_info = str(detail_html).replace("var desc='", '').replace("';", '')
##        print( self.detail_info )
         
        detail_image = re.findall(detail,detail_html)
##        pprint.pprint("商品页面所有图片地址：%s"%detail_html)
##        pprint.pprint("商品详情图片地址：%s"%detail_image)

        self.newdata={"MAIN":main_img['default'],"DETAIL":detail_image,"id":self.id,}   
##        pprint.pprint( self.newdata )


        psvs = []
        self.newdata['COLOR']=[]
        
        for v in range(len(color_data)):
            if ";"in color_data[v]["pvs"]:
                psv = color_data[v]['pvs'][color_data[v]['pvs'].find(";")+1:]
            else:
                psv = color_data[v]['pvs']
            if psv in psvs:
                continue
            psvs.append(psv)
            
            
            self.newdata['COLOR'].append({color_data[v]["names"]:main_img[";"+psv+";"]})
            
##        pprint.pprint(self.newdata)
        print(psvs)
        return self.newdata

    
        
    def download(self):
        if len(self.newdata)>0:
            for x in range(len(self.newdata['MAIN'])):
          
                threading.Thread(target=self.download_main,args=(self.newdata['MAIN'][x],x)).start()
                 
            for x in self.newdata['COLOR']:
             
                threading.Thread(target=self.download_color,args=(x,)).start()
            for x in range(len(self.newdata['DETAIL'])):
                 
                threading.Thread(target=self.download_detail,args=(self.newdata['DETAIL'][x],x)).start()
        return
 
 
    def download_main(self,url,index):
        try:
            img = requests.get("http:"+url,stream=True,headers = self.headers,timeout=10)
 
        except:
            print(sys.exc_info())
            return
        if img.ok:
            if not os.path.exists(self.name+"/main"):
                try:
                    os.makedirs(self.name+"/main")
                except:
                    pass
            imgs = open(self.name+"/main/%s.jpg"%index,"wb")
            imgs.write(img.content)
            imgs.close()
             
    def download_color(self,url):
          
        try:
            img = requests.get("http:"+url[list(url.keys())[0]][0],stream=True,headers = self.headers,timeout=10)
 
        except:
            print(sys.exc_info())
            return
        if img.ok:
            if not os.path.exists(self.name+"/color"):
                try:
                    os.makedirs(self.name+"/color")
                except:
                    pass
            if "/"in list(url.keys())[0]:
                color = list(url.keys())[0].replace("/","_")
            elif "\\" in list(url.keys())[0]:
                color = list(url.keys())[0].replace("\\","_")
            else:
                color = list(url.keys())[0]
            imgs = open(self.name+"/color/%s.jpg"%color,"wb")
            imgs.write(img.content)
            imgs.close()
 
 
    def download_detail(self,url,index):
 
        try:
            img = requests.get(url,stream=True,headers = self.headers,timeout=10)
 
        except:
            print(sys.exc_info())
            return
        if img.ok:
            if not os.path.exists(self.name+"/detail"):
                try:
                    os.makedirs(self.name+"/detail")
                except:
                    pass
             
            imgs = open(self.name+"/detail/%s.jpg"%index,"wb")
            imgs.write(img.content)
 
            imgs.close()
             


     

    def writeexcel(self,path):
             """
             将数据插入Excel   
             """
             dealcontent = [("version 1.00",""),
                     
                 ("title","cid","seller_cids","stuff_status","location_state",
                  
                  "location_city","item_type","price","auction_increment","num",
                  
                  "valid_thru","freight_payer","post_fee","ems_fee","express_fee",
                  
                  "has_invoice","has_warranty","approve_status","has_showcase","list_time",
                  
                  "description","cateProps","postage_id","has_discount","modified",
                  
                  "upload_fail_msg","picture_status","auction_point","picture","video",
                  
                  "skuProps","inputPids","inputValues","outer_id","propAlias",
                  
                  "auto_fill","num_id","local_cid","navigation_type","user_name",
                  
                  "syncStatus","is_lighting_consigment","is_xinpin","foodparame","features",
                  
                  "buyareatype","global_stock_type","global_stock_country","sub_stock_type","item_size",
                  
                  "item_weight","sell_promise","custom_design_flag","wireless_desc","barcode",
                  
                  "sku_barcode","newprepay","subtitle"),
                     
                 ("宝贝名称","宝贝类目","店铺类目","新旧程度","省",
                  
                  "城市","出售方式","宝贝价格","加价幅度","宝贝数量",
                  
                  "有效期","运费承担","平邮","EMS","快递",
                  
                  "发票","保修","放入仓库","橱窗推荐","开始时间",
                  
                  "宝贝描述","宝贝属性","邮费模版ID","会员打折","修改时间",
                  
                  "上传状态","图片状态","返点比例","新图片","视频",
                  
                  "销售属性组合","用户输入ID串","用户输入名-值对","商家编码","销售属性别名",
                  
                  "代充类型","数字ID","本地ID","宝贝分类","账户名称",
                  
                  "宝贝状态","闪电发货","新品","食品专项","尺码库",
                  
                  "采购地","库存类型","国家地区","库存计数","物流体积",
                  
                  "物流重量","退换货承诺","定制工具","无线详情","商品条形码",
                  
                  "sku 条形码","7天退货","宝贝卖点"),


                  (self.itemDO_info['title'],self.itemDO_info['categoryId'],"",self.itemDO_info['feature'],self.itemDO_info['prov'],#宝贝名称
                   
                   "深圳","1",self.itemDO_info['reservePrice'],"0",self.itemDO_info['quantity'],#城市
                   
                   "7","1","","","0",#有效期
                   
                   "0","0","1",self.itemDO_info['showCompanyPurchase'],"",#发票
                   
                   self.detail_info,self.pvs_info,"1364214590","0","",#宝贝描述
                   
                   "200","","0","","",#上传状态 a7c4f22c62f2b4ba43fb8a3d10e10311:1:0:|;
                   
                   "32.00:65292::1627207:21962;19.00:65292::1627207:21966;20.70:65292::1627207:28320;","","","","别名",#销售属性组合
                   
                   "0","","0","","",#代充类型"
                   
                   "1","0","0","","",#宝贝状态
                   
                   "0","-1","","1","",#采购地

                   "0","0","","","",#物流重量

                   "","1",""#sku 条形码
                     )
                     ]         
             
             self.workbook = wx.Workbook(path)
             nor = self.workbook.add_format({'font_size':11,'font_name': '宋体'})
##             top = self.workbook.add_format({'border':1,'align':'center','bg_color':'white','font_size':11,'font_name': '微软雅黑'})
##             red = self.workbook.add_format({'font_color':'white','border':1,'align':'center','bg_color':'800000','font_size':11,'font_name': '微软雅黑','bold':True})
##             image = self.workbook.add_format({'border':1,'align':'center','bg_color':'white','font_size':11,'font_name': '微软雅黑'})
             formatt=nor
##             formatt.set_align('vcenter') #设置单元格垂直对齐
             self.worksheet = self.workbook.add_worksheet('csv'+str(sid))        #创建一个工作表对象
             width=len(dealcontent[0])
             self.worksheet.set_column(0,width,22)            #设定列的宽度为22像素
  
             for i in range(0,len(dealcontent)):
##                     if i==0:
##                             formatt=red
##                     else:
##                             formatt=top
                     for j in range(0,len(dealcontent[i])):
                             if i!=0 and j==len(dealcontent[i])-1:
                                     if dealcontent[i][j]=='':
                                              self.worksheet.write(i,j,' ',formatt)
                                     else:
                                             try:
                                                      self.worksheet.write(i,j,dealcontent[i][j])
                                             except:
                                                      self.worksheet.write(i,j,' ',formatt)
                                                      
                             else:
                                     if dealcontent[i][j]:
                                              self.worksheet.write(i,j,dealcontent[i][j],formatt)
                                     else:
                                              self.worksheet.write(i,j,' ',formatt)
             print("下载完成，共下载1个，成功下载1个，下载失败0个")
             self.workbook.close()



if __name__ == '__main__':

##    sid = input("[+] 输入天猫宝贝ID：")
    
    sid = 528766269341 ## 这里输入天猫宝贝ID

    taobao = spider(sid,"宝贝详情/T")

    shop_row = taobao.matchs()
    
    taobao.writeexcel("csv%s.xlsx"%(sid))
       
##    taobao.download()
    
