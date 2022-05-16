import smtplib

import pytest
from common.yaml_util import read_yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class TestEmail:
    @pytest.mark.parametrize('email',read_yaml('test_case/email_manage/config.yaml'))
    def test_email(self,email):
        message=MIMEMultipart('related')
        subject='邮件服务启用'
        fujian=MIMEText(open('./config.yaml','rb').read(),'yaml','utf-8')

        message['from']=email['username']
        message['to']=email['receiver']
        message['subject']=subject
        message.attach(fujian)
        smtp= smtplib.SMTP()
        smtp.connect(email['smtpserver'])
        smtp.login(email['username'],email['password'])
        smtp.sendmail(email['username'],email['receiver'],message.as_string())
        smtp.quit()

if __name__ == '__main__':
    pytest.main()
