#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 14:51
# @Author  : Xuegod Teacher For
# @File    : 01_session_test.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent
headers = {
    'Referer': 'https://passport.5i5j.com/passport/login?service=https%3A%2F%2Fbj.5i5j.com%2Freglogin%2Findex%3FpreUrl%3Dhttps%253A%252F%252Fbj.5i5j.com%252F&status=1&city=bj',
    'User-Agent':UserAgent().random
}
#form 表单  method post input中输入的数据
data = {
    'username': '17611100746',#你的账号
    'password': 'mama521',#你的秘钥
    'aim': 'pc',#指定pc
    'service': 'https://bj.5i5j.com/reglogin/index?preUrl=https%3A%2F%2Fbj.5i5j.com%2F',
    'status': '1'#状态
}
#回话状态为此维持
s = requests.session()
# print(s.cookies)
base_url = 'https://passport.5i5j.com/passport/sigin?city=bj'
res = s.post(url=base_url,headers=headers,data=data)
# print(res.text)
# print(s.cookies.get_dict())

response = s.get('https://bj.5i5j.com/user/index/')
import re
if data['username'] not in response.text:
    href = re.findall(r"<script>window.location.href='(.*?)';</script>",response.text,re.S)
    r = s.get(href[0])
    print(r.text)
else:
    print(response.text)










