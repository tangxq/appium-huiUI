import smtplib,logging
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

logger=logging.getLogger('main.sendreport')


def sendreport(file_new):
    msg = MIMEMultipart()
    with open(file_new, 'rb') as f:
        mail_body = f.read()
    # 添加邮件正文
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    #添加附件
    att1 = MIMEText(mail_body, 'html', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att1)
    #设定邮件标题
    msg['subject'] = Header('Android App回归测试报告', 'utf-8')
    msg['From'] = 'XXXXXX'
    msg['From'] = Header('Tester', 'utf-8')
    #收件人,设置多个收件人时用;隔开
    msg['To'] = 'XXXXXX'
    try:
        smtp = smtplib.SMTP('smtp.qiye.163.com', '25')
        #smtp.set_debuglevel(1)
        smtp.login('XXXXXX', 'XXXXX')  #登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
        smtp.quit()
        print('report has send out!')
        logger.warning('report has send out!')
        return 0
    except smtplib.SMTPException:
        print("Error: report send fail!")
        logger.warning("Error: report send fail!")
        return 1
#if __name__=='__main__':
    #sendreport('E:\\huipeitongUI\\report\\16-08-03_13_47_49_result.html')
