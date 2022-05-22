import os
import time
import pytest
from common.emails import Emails
if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system("allure generate ./temps -o ./reports --clean")
    em=Emails()
    em.send_email('测试报告','./reports/index.html')

