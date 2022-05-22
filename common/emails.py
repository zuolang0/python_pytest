import smtplib

from common.yaml_util import read_yaml
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
class Emails:
    def send_email(self,subject,filepath):
        message=MIMEMultipart('related')
        conf=read_yaml('/conf/conf.yaml')
        # fujian=MIMEText(open(filepath,'rb').read(),'html','utf-8')
        message['from']=conf['email']['username']

        message['to']=conf['email']['receiver']
        message['subject']=subject
        page = MIMEText(open(filepath, 'rb').read())
        page.add_header('Content-Disposition', 'attachment', filename=filepath)
        message.attach(MIMEText(page, 'html', 'utf-8'))

        smtp= smtplib.SMTP()
        smtp.connect(conf['email']['smtpserver'])
        smtp.login(conf['email']['username'], conf['email']['password'])
        smtp.sendmail(conf['email']['username'], conf['email']['receiver'], message.as_string())
        smtp.quit()


# if __name__ == '__main__':
#     em=Emails()
#     em.send_email('1','1')
