import datetime
import os
import time
import pytest
from common.emails import Emails
from common.requests_until import RequestsUtil
from common.yaml_util import write_yaml
def get_token():
    method = "get"
    url = "https://api.weixin.qq.com/cgi-bin/token"
    data = {
        "grant_type": "client_credential",
        "appid": "wxde6c7f73842fe0d6",
        "secret": "6a3af6156f86205146d1abcadc13dd8d"
    }
    res=RequestsUtil.send_requests(method,url,data)
    return res.json()

def report():
    pass
def send_email():
    pass
if __name__ == '__main__':
    token=get_token()
    write_yaml(token,'test_case/token.yaml')
    pytest.main()
    time.sleep(2)
    date=str(datetime.date.today())
    os.system("allure generate ./temps -o D:/Wamp64/www/"+date+" --clean")
    url="http://localhost/"+date
    em=Emails()
    em.send_email('测试报告',url)

