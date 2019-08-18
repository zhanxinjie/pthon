import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#这是构造自己邮箱系统的发件人和收件人
from_addr = ''
password = ''
to_addr = ''
#构造自己的邮件
msg = MIMEMultipart()
msg["Subject"] = '这是主题'
msg["From"] = from_addr
msg[""] = to_addr
#邮件正文文本
part = MIMEText('欢迎大家来到这里！')
msg.attach(part)

part = MIMEApplication(r'','rd').read()
part.add_header('content-dispasition','attachment',filrname = 歌名.mp3)
msg.attach(part)

try:
    #构造自己的服务器
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(from_addr,password)
    s.sendmail(from_addr,to_addr, msg.as_string() )

except Exception as e:
    print(e)
s.close()

