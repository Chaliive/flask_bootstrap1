# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import smtplib
from email.mime.text import MIMEText



def mail():
    host = 'smtp.163.com'
    port = 25
    sender = 'ttt_988@163.com'
    pwd = '1qaz2wsx3edc432'

    receiver = 'zhoucy567@qq.com'
    # body = '<h1>Hi</h1><p>test</p>'

    f = open("show.html", 'rb')  #
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    # msg = MIMEText(body, 'html', 'utf-8')
    msg['subject'] = 'report'
    msg['from'] = sender
    msg['to'] = receiver
    try:
        s = smtplib.SMTP(host, port)
        s.login(sender, '1qaz2wsx')  # 163设置的密码，客户端授权码
        s.sendmail(sender, receiver, msg.as_string())
        print('success!!!')
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    mail()
