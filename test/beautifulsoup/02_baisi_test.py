#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 15:04
# @Author  : Xuegod Teacher For
# @File    : 02_baisi_test.py
# @Software: PyCharm
# http://www.budejie.com/video/1
# http://www.budejie.com/video/2
# http://www.budejie.com/video/3
# http://www.budejie.com/video/4
# <a href="http://svideo.spriteapp.com/video/2019/.*?.mp4" target="_blank" download="" class="ipad-down-href" style="border:0;outline: none;">
from bs4 import BeautifulSoup
import requests
import re,time
#todo:传入url地址，就把你的video全部下载

def get_page(url):
    '''
    :param url: 要爬取的url
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    lists = soup.find_all('a',href=re.compile('http://svideo.spriteapp.com/video/2019/.*?.mp4'))
    for i in lists:
        url_href = i.get('href')
        req = requests.get(url_href)
        with open('./video/'+str(time.time())+'.mp4','wb') as file:
            file.write(req.content)
url = 'http://www.budejie.com/video/'
def get_more_page(start,end):
    '''
    :param start: 开启下载的页码
    :param end: 结束页码
    :return:
    '''
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(1)



if __name__ == '__main__':
    get_more_page(1,3)






