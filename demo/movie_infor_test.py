import requests
import re
from bs4 import BeautifulSoup
from time import sleep

URL = "http://www.dytt8.net"
url_index = "http://www.dytt8.net/html/gndy/dyzz/list_23_"

def Get_index(number = 1):
    #传入索引页的页码，获取标题和对应的详情页的URL，将其构成字典返回
    url = url_index + str(number) + ".html"
    #传获取HTML源码
    res = requests.get(url)
    res.encoding = "gb2312"
    
    text = res.text
    
    #从索引页的源码中获取信息所在的部分并返回
    reg_name = r'《(.+?)》'
    reg_name = re.compile(reg_name)
    Soup = BeautifulSoup(text,'lxml')
    Soup = Soup.select('a["class=ulink"]')
    MyDict = dict()
    for s in Soup:
        try:
            name = re.findall(reg_name,s.text)[0]
        except:
            name = str(number)
            print("在%s中获取电影名失败" %s)
        url = URL + s['href']
        MyDict[name] = url
    
    if number == 1:
        reg_number = r'共(.+?)页/'
        reg_number = re.compile(reg_number)
        Max = re.findall(reg_number,text)[0]
        
        return Max,MyDict
    else:
        return MyDict
        

def Get_info(url):
    #传入详情页的URL获取电影的详细的信息
    res = requests.get(url)
    res.encoding = "gb2312"
    text = (res.text)
    #print(text)
    Soup = BeautifulSoup(text,'lxml')
    Soup = Soup.select('div["id=Zoom"]')
    Soup = Soup[0].select("td")[0]
    return Soup

def Get_info_2(text):
    reg_1 = r'(.+?)<br/>'
    reg_1 = re.compile(reg_1)
    
    reg_2 = r'(ftp:.+?)">'
    reg_2 = re.compile(reg_2)
    
    Xunlei = re.findall(reg_2,text)
    Xunlei = Xunlei[0]
    
    info = re.findall(reg_1,text)
    
    MyList = list()
    for i in info:
        
        i = i.replace('<br/>','')
        i = i.replace('◎','')
        i = i.replace('</table> ','')
        MyList.append(i)
    return Xunlei,MyList


def DownLoad(Dict):
        for d in MyDict:
            url_2 = MyDict[d]
            try:
                text= str(Get_info(url_2))
                [Xunlei,MyList] = Get_info_2(text)
                #print(Xunlei)
                f = open("电影.txt",'a')
                f.write(Xunlei+'\n')

                for i in MyList:
                    if '<' in i:
                        pass
                    else:
                        f.write(i+'\n')

                f.write("\n\n")
                f.close()
            except:
                print("电影%s的详情下载失败！" %d)
            #print("%s 的详情下载完成！" %d)

if __name__ == "__main__":
    
    [Max,MyDict] = Get_index()
    
    DownLoad(MyDict)
    
    sleep(2)
    
    for j in range(2,int(Max)+1):
        MyDict = Get_index(j)
        DownLoad(MyDict)
        print("第%d页下载完成！" %j)
        sleep(2)
