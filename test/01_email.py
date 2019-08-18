import smtplib
from email.mime.text import MIMEText #这是构造自己的中文文本的方法


#构建邮件正文文本
msg = MIMEText('hello 大家晚上好')
#todo：构造邮件正文文本
msg["Subject"] = '这是一个测试'
msg["From"] = from_addr
msg["To"] = to_addr
#腾讯服务器
smp_server = 'smtp.qq.com'
#构造自己的服务器
server = smtplib.SMTP(smp_server,25)
#登录自己的服务器
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,to_addr, msg.as_string() )
#关闭邮箱
server.close()