#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 14:46
# @Author  : Xuegod Teacher For
# @File    : 01_bs_test.py
# @Software: PyCharm
from bs4 import BeautifulSoup as BS

text = '''
<html>
<head>
    <meta = charset='UTF-8' >
    <title id =1 href = 'http://example.com/elsie' class = 'title'>Test</title>
</head>
<body>
   <div class = 'ok'>
       <div class = 'nice'>
           <p class = 'p'>
               Hello World
           </p>
            <p class = 'e'>
               风一般的男人
           </p>
       </div>
   </div>
</body> 
</html>
'''
soup = BS(text,'lxml')
# print(soup)
#更加细节化的修饰
# print(type(soup))
# print(soup.div)
#find_all() find()
# print(soup.find('p'))
# print(soup.find_all('p'))
import re
print(soup.find_all(re.compile(r'^p')))













