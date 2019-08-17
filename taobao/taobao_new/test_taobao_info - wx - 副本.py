import requests

import re
import json
from xlwt import Workbook
import xlrd
import time

import xlsxwriter as wx


class spider:
    def __init__(self,sid,name):
      
        self.id = sid
        self.headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"https://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
 
        self.name=name

##        self.book = Workbook()
##        self.sheet = self.book.add_sheet('csv'+str(sid))
##        #第一行数据
##        self.sheet.write(0,0,'version 1.00')
##        #第二行数据      
##        self.sheet.write(1,0,'title')        
##        self.sheet.write(1,1,'cid')
##        self.sheet.write(1,2,'seller_cids')
##        self.sheet.write(1,3,'stuff_status')
##        self.sheet.write(1,4,'location_state')
##        self.sheet.write(1,5,'location_city')
##        self.sheet.write(1,6,'item_type')
##        self.sheet.write(1,7,'price')
##        self.sheet.write(1,8,'auction_increment')
##        self.sheet.write(1,9,'num')
##        
##        self.sheet.write(1,10,'valid_thru')
##        self.sheet.write(1,11,'freight_payer')
##        self.sheet.write(1,12,'post_fee')
##        self.sheet.write(1,13,'ems_fee')
##        self.sheet.write(1,14,'express_fee')
##        self.sheet.write(1,15,'has_invoice')
##        self.sheet.write(1,16,'has_warranty')
##        self.sheet.write(1,17,'approve_status')
##        self.sheet.write(1,18,'has_showcase')
##        self.sheet.write(1,19,'list_time')
##        
##        self.sheet.write(1,20,'description')
##        self.sheet.write(1,21,'cateProps')
##        self.sheet.write(1,22,'postage_id')
##        self.sheet.write(1,23,'has_discount')
##        self.sheet.write(1,24,'modified')
##        self.sheet.write(1,25,'has_invoice')
##        self.sheet.write(1,26,'picture_status')
##        self.sheet.write(1,27,'auction_point')
##        self.sheet.write(1,28,'picture')
##        self.sheet.write(1,29,'video')
##        
##        self.sheet.write(1,30,'skuProps')
##        self.sheet.write(1,31,'inputPids')
##        self.sheet.write(1,32,'inputValues')
##        self.sheet.write(1,33,'outer_id')
##        self.sheet.write(1,34,'propAlias')
##        self.sheet.write(1,35,'auto_fill')
##        self.sheet.write(1,36,'num_id')
##        self.sheet.write(1,37,'local_cid')
##        self.sheet.write(1,38,' navigation_type')
##        self.sheet.write(1,39,'user_name')
##        
##        self.sheet.write(1,40,'syncStatus')
##        self.sheet.write(1,41,'is_lighting_consigment')
##        self.sheet.write(1,42,'is_xinpin')
##        self.sheet.write(1,43,'foodparame')
##        self.sheet.write(1,44,'features')
##        self.sheet.write(1,45,'item_size')
##        self.sheet.write(1,46,'item_weight')
##        self.sheet.write(1,47,'wireless_desc')
##        self.sheet.write(1,48,'subtitle')
##        self.sheet.write(1,49,'input_custom_cpv')
##        
##        #第三行数据
##        self.sheet.write(2,0,'宝贝名称')        
##        self.sheet.write(2,1,'宝贝类目')
##        self.sheet.write(2,2,'店铺类目')
##        self.sheet.write(2,3,'新旧程度')
##        self.sheet.write(2,4,'省')
##        self.sheet.write(2,5,'城市')
##        self.sheet.write(2,6,'出售方式')
##        self.sheet.write(2,7,'宝贝价格')
##        self.sheet.write(2,8,'加价幅度')
##        self.sheet.write(2,9,'宝贝数量')
##        
##        self.sheet.write(2,10,'有效期')
##        self.sheet.write(2,11,'运费承担')
##        self.sheet.write(2,12,'平邮')
##        self.sheet.write(2,13,'EMS')
##        self.sheet.write(2,14,'快递')
##        self.sheet.write(2,15,'发票')
##        self.sheet.write(2,16,'保修')
##        self.sheet.write(2,17,'放入仓库')
##        self.sheet.write(2,18,'橱窗推荐')
##        self.sheet.write(2,19,'开始时间')
##					
##     
##        self.sheet.write(2,20,'宝贝描述')
##        self.sheet.write(2,21,'宝贝属性')
##        self.sheet.write(2,22,'邮费模版ID')
##        self.sheet.write(2,23,'会员打折')
##        self.sheet.write(2,24,'修改时间')
##        self.sheet.write(2,25,'上传状态')
##        self.sheet.write(2,26,'图片状态')
##        self.sheet.write(2,27,'返点比例')
##        self.sheet.write(2,28,'新图片')
##        self.sheet.write(2,29,'视频')
##        
##        self.sheet.write(2,30,'销售属性组合')
##        self.sheet.write(2,31,'用户输入ID串')
##        self.sheet.write(2,32,'用户输入名-值对')
##        self.sheet.write(2,33,'商家编码')
##        self.sheet.write(2,34,'销售属性别名')
##        self.sheet.write(2,35,'代充类型')
##        self.sheet.write(2,36,'数字ID')
##        self.sheet.write(2,37,'本地ID')
##        self.sheet.write(2,38,'宝贝分类')
##        self.sheet.write(2,39,'账户名称')
##        
##        self.sheet.write(2,40,'宝贝状态')
##        self.sheet.write(2,41,'闪电发货')
##        self.sheet.write(2,42,'新品')
##        self.sheet.write(2,43,'食品专项')
##        self.sheet.write(2,44,'尺码库')
##        self.sheet.write(2,45,'物流体积')
##        self.sheet.write(2,46,'物流重量')
##        self.sheet.write(2,47,'无线详情')
##        self.sheet.write(2,48,'宝贝卖点')
##        self.sheet.write(2,49,'自定义属性值')
##        
##        self.book.save('csv' + str(sid) + '.csv')

    def openurl(self,url):
         
        self.request = requests.get(url,headers = self.headers)        
        if self.request.ok:
            return self.request.text
        
    def matchs(self):

        tmall_exp = r"Setup\(([\s\S]+?)\);"### 匹配商品数据的正则
        detail= r"src=\"(https://img\S+?[jpgifn]+?)\""  ###匹配 商品详情图的正则
        html = self.openurl("https://detail.tmall.com/item.htm?id=%s"%self.id)
##        print(html)
        data = re.findall(tmall_exp,html)
        data = json.loads(data[0])
##        print(data)
        itemDO_info = data['itemDO']
        print("商品详情信息：%s"%itemDO_info)
        
##        self.sheet.write(3,0,itemDO_info['title'])
##        self.sheet.write(3,1,itemDO_info['categoryId'])
##        
##        self.sheet.write(3,3,itemDO_info['feature'])
##        self.sheet.write(3,4,itemDO_info['prov'])
####        self.sheet.write(3,5,itemDO_info[''])
##        self.sheet.write(3,7,itemDO_info['reservePrice'])
##        print(itemDO_info['title'])
##                
##        self.book.save('csv' + str(sid) + '.csv')
        
        main_img = data['propertyPics'] ## 这里包括了主图和颜色图的地址
        color_data =data['valItemInfo'] ['skuList']  ### 这里获得商品的颜色信息列表   包括颜色编码  颜色名称,商品skuID

##        print("主图和颜色图的地址：%s"%main_img)
##        print("商品的颜色信息列表：%s"%color_data)
        detail_html = self.openurl("http:"+data['api']["httpsDescUrl"])
        detail_image = re.findall(detail,detail_html)
##        print("商品页面所有图片地址：%s"%detail_html)
##        print("商品详情图片地址：%s"%detail_image)
        self.newdata={"MAIN":main_img['default'],"DETAIL":detail_image,"id":self.id,}        

    def writeexcel(self,path,i,dealcontent):
             """
             将数据插入Excel   
             """
             
             workbook = wx.Workbook(path)
             top = workbook.add_format({'border':1,'align':'center','bg_color':'white','font_size':11,'font_name': '微软雅黑'})
##             red = workbook.add_format({'font_color':'white','border':1,'align':'center','bg_color':'800000','font_size':11,'font_name': '微软雅黑','bold':True})
             image = workbook.add_format({'border':1,'align':'center','bg_color':'white','font_size':11,'font_name': '微软雅黑'})
             formatt=top
             formatt.set_align('vcenter') #设置单元格垂直对齐
             worksheet = workbook.add_worksheet('csv'+str(sid))        #创建一个工作表对象
             width=len(dealcontent[0])
             worksheet.set_column(0,width,15)            #设定列的宽度为22像素
  
             for i in range(0,len(dealcontent)):
##                     if i==0:
##                             formatt=red
##                     else:
##                             formatt=top
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
                                             worksheet.write(i,j,' ',formatt)


             workbook.close()

           


if __name__ == '__main__':

##    sid = input("[+] 输入天猫宝贝ID：")
    sid = 528766269341 ## 这里输入天猫宝贝ID


    shop_row1 = [("version 1.00",""),
                 ("title","cid","seller_cids","stuff_status","location_state","location_city","item_type","price","auction_increment","num",
                  "valid_thru","freight_payer","post_fee","ems_fee","express_fee","has_invoice","has_warranty","approve_status","has_showcase","list_time",
                  "description","cateProps","postage_id","has_discount","modified","upload_fail_msg","picture_status","auction_point","picture","video",
                  "skuProps","inputPids","inputValues","outer_id","propAlias","auto_fill","num_id","local_cid","navigation_type","user_name",
                  "syncStatus","is_lighting_consigment","is_xinpin","foodparame","features","buyareatype","global_stock_type","global_stock_country","sub_stock_type","item_size",
                  "item_weight","sell_promise","custom_design_flag","wireless_desc","barcode","sku_barcode","newprepay","subtitle",""),
                 ("宝贝名称","宝贝类目","店铺类目","新旧程度","省","城市","出售方式","宝贝价格","加价幅度","宝贝数量",
                  "有效期","运费承担","平邮","EMS","快递","发票","保修","放入仓库","橱窗推荐","开始时间",
                  "宝贝描述","宝贝属性","邮费模版ID","会员打折","修改时间","上传状态","图片状态","返点比例","新图片","视频",
                  "销售属性组合","用户输入ID串","用户输入名-值对","商家编码","销售属性别名","代充类型","数字ID","本地ID","宝贝分类","账户名称",
                  "宝贝状态","闪电发货","新品","食品专项","尺码库","采购地","库存类型","国家地区","库存计数","物流体积",
                  "物流重量","退换货承诺","定制工具","无线详情","商品条形码","sku 条形码","7天退货","宝贝卖点","")]
																



    taobao = spider(sid,"宝贝详情/T")

    taobao.writeexcel("csv%s.xlsx"%(sid),1,shop_row1)
##    taobao.writeexcel("csv%s.xlsx"%(sid),2,shop_row2)
     
    taobao.matchs()
       
##    taobao.download()
    
