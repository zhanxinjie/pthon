#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 20:34
# @Author  : Xuegod Teacher For
# @File    : 02_email_send_data.py
# @Software: PyCharm
#todo:发送附件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#这是构造自己的邮箱系统的发件人，接受者
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd'
to_addr = '3403073998@qq.com'
#构造自己邮件
msg = MIMEMultipart()
msg['Subject'] = '这是主题'
msg['From'] = from_addr
msg['To'] = to_addr
#邮件正文文本
part = MIMEText('欢迎大家来打直播间')
msg.attach(part)

#构造自己的附件
part = MIMEApplication(open(r'E:\xuegod_code\3_1_Python_爬虫基础之urllib&requests详解\music\孤身.mp3','rb').read())
part.add_header('content-disposition', 'attachment', filename='孤身.mp3')
msg.attach(part)

try:
    #构造自己的服务器
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    #登录自己的服务器
    s.login(from_addr,password)
    #发送自己邮件
    s.sendmail(from_addr,to_addr,msg.as_string())

except Exception as e:
    print(e)
s.close()