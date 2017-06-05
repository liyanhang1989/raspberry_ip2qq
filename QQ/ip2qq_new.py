# coding=utf-8
import smtplib
import httplib
from email.mime.text import MIMEText
import time
import threading
import MySQLdb


def printIP():
    # 从 Oray 网站取 IP 地址
    httpClient = httplib.HTTPConnection('ddns.oray.com', 80, timeout=30)
    httpClient.request('GET', '/checkip')
    response = httpClient.getresponse()
    ipline = response.read().split(' ')[5]
    ipAddress = ipline[0:ipline.index('<')]
    httpClient.close()

    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='ip')
    cursor = conn.cursor()
    sql_old = "SELECT * FROM ip_list"
    cursor.execute(sql_old)
    row = cursor.fetchone()
    if ipAddress == row[1]:
        sendEmail("IP地址没发生变化！")
    else:
        sql_new = "update ip_list set ip_name='" + ipAddress + "' where ip_id = '" + str(row[0]) + "'"
        cursor.execute(sql_new)
        conn.commit()
        sendEmail(ipAddress)
        cursor.close()
        conn.close()
    global timer
    timer = threading.Timer(3600.0, printIP)
    timer.start()

def sendEmail(message):
        # 如何登陆邮件
        # 按目的分为为发送邮件而登陆 还是为了读取邮件而登录
        # 发送邮件登录 一般来说登录使用 SMTP,接收邮箱用POP
        email_name="***@qq.com"
        _user = email_name
        _pwd = "***"  # qq邮箱为授权码(16位)
        sent = smtplib.SMTP_SSL('smtp.qq.com', 465)
        # 设置了SMTP服务器为stmp.qq.com 其端口号为465
        sent.login(_user, _pwd)
        # 登陆
        # 发送邮件
        # 刚才已经登录，现在需要设置发送内容，然后发送即可
        to = [email_name]
        content = MIMEText(message)
        # MIMEText表示邮件发送具体内容
        content['Subject'] = '新IP地址'
        # 设置邮箱标题
        content['From'] = ''
        # 设置邮箱有哪里发送
        content['To'] = ','.join(to)  # 这里设置了邮件要发送的地址，可以群发
        sent.sendmail(email_name, to, content.as_string())
        # 三个参数
        sent.close()
        # 关闭邮箱
        return

if __name__ == "__main__":
    timer = threading.Timer(3600.0, printIP)
    timer.start()















