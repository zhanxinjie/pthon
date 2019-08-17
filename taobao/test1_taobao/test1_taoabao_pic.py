#!/usr/bin/python3.5
#eoding:utf8
 
import os
import requests
import re
import time
import json
 
now = time.strftime("%Y%m%d_%H%M%S")
keyword="test"
img = {} 
total = []
tmall = "tamll.com"
https = "https:"
detailPrixe = "https://img.alicdn.com/imgextra/i1/"
sellerId=""
 
#def __init__(self):
#return None
 
def get(url):
    try:
        ret = requests.get(url).text
        return ret
    except:
        return 1
 
def fiterData(text):
    urllist = []
    text=str(text)
    title = re.findall('<title>(.*)</title>',text)
    imgapi = re.findall('apiImgInfo[\s]*:[\s]*\'(.*)\'',text)
    stateID = re.findall('sellerId         : \'(\d+)\'',text)
    #sellerId = stateID[0]
    try:
        url = https+imgapi[0]
 
        imgdata = get(url).replace("\r","").replace("\n","").replace("\t","").replace("$callback","").replace(")","").replace("(","")
        imgdata = json.loads(imgdata)
        for i in imgdata:
            if len(i) >= 43:
                urllist.append(i)
            else:
                pass
        img[title[0].replace("-淘宝网","")] = urllist
    except:
        print("[!] Error")
     
def CreateDir(path,url):
    dedir = path+"/detail"
    if os.path.exists(path):
        if os.path.exists(dedir):
            pass
        else:
            os.mkdir(dedir)
    else:
        try:
            os.mkdir(path)
            if not os.path.exists(dedir):
                os.mkdir(dedir)
            else:
                pass
        except FileNotFoundError:
            print("[-] %s " % "FILE NOT FUOUND!")
    print("[*] download detatil %s" % url )
    try:
        ifile = open(dedir+"/"+str(int(time.time()))+".jpg","wb")
        data = requests.get(url).content
        ifile.write(data)
        ifile.close()
    except OSError as e:
        print("[!] OPS error "+e)
        pass
    except:
        print("req")
 
 
def ReadListFile():
    try:
        a=open("detail_url.txt","r").read()
        a=a.split("\n")
        return a
    except OSError:
        print("Unoblue file")
        return false
 
 
for uite in ReadListFile():
    if uite != "":
        print("[+] %s " %uite)
        html=requests.get(uite).text
        fiterData(html)
 
 
for key,value in img.items().__iter__():
    print(key)
    for j in range(len(value)):
        iname = value[j]
        try:
            sellerId=re.findall('(\d+).jpg',iname)[0]
            ImgUrl=detailPrixe+"%s/" % (sellerId) +iname
            path="%s/%s" %("公仔20170609_183403",key)
            CreateDir(path,ImgUrl)
        except IndexError:
            #print()
            pass
