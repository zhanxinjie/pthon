#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 20:14
# @Author  : Xuegod Teacher For
# @File    : 01_email_test.py
# @Software: PyCharm
# user = '3403073998@qq.com'
# pwd = 'ihenvpgtjinqchbd'
# to = '3403073998@qq.com'
import smtplib
from email.mime.text import MIMEText#这是构造自己的中文文本的方法
#这是构造自己的邮箱系统的发件人，接受者
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd'
to_addr = '3403073998@qq.com'
#构造邮件正文文本
msg = MIMEText('hello 大家晚上好')
#腾讯服务器
smtp_server = 'smtp.qq.com'
#构造自己的 服务器
server = smtplib.SMTP(smtp_server,25)
#登录自己的服务器
server.login(from_addr,password)
#发送邮件，第一个参数发送者，接受者，邮件
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭邮箱
server.close()


