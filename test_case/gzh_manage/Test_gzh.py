
import pytest
from common.assertbase import AssertBase
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml
from common.logger import Logger

class TestApi:
    myass=AssertBase()
    log=Logger()
    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/get_token.yaml'))
    @pytest.mark.run(order=1)
    def test_get_token(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        self.log.log_request(caseinfo['request'])
        res=RequestsUtil.send_requests(method,url,data)
        self.myass.assert_main(caseinfo['validate']['assert_str'],res)
        self.myass.assert_status(caseinfo['validate']['assert_code'],res.status_code)
        if 'access_token' in res.json():
            write_yaml(res.json(),'test_case/token.yaml')



