def main():
    sendmail()


def sendmail():
    # 登录网页版网易邮箱，在【设置】-【POP3/SMTP/IMAP】中开启IMAP就可以了
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    from email.header import Header

    msg = MIMEText('学习python很重要，此代码为第一次尝试发送email的功能，2017年github需要传送很多东西，希望配合', 'plain', 'utf-8')
    msg['From'] = formataddr(['mao', 'clevermlx@163.com'])
    msg['To'] = formataddr(['CoolGuy', '27230476@qq.com'])
    msg['Subject'] = Header("Python开会脚本", 'utf-8')
    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('clevermlx@163.com', '授权码')
    server.sendmail('clevermlx@163.com', '27230476@qq.com', msg.as_string())
    server.quit()
    print('run complete')


if __name__ == '__main__':
    main()
