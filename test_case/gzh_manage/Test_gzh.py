import re

import jsonpath as jsonpath
import pytest
import requests
from common.assertbase import AssertBase
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml


class TestApi:
    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/get_token.yaml'))
    @pytest.mark.run(order=1)
    def test_01_api(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        res=RequestsUtil.send_requests(method,url,data)
        myass=AssertBase()
        myass.assert_main(caseinfo['validate']['assert_str'],res)
        myass.assert_status(caseinfo['validate']['assert_code'],res.status_code)
        if 'access_token' in res.json():
            write_yaml(res.json(),'test_case/token.yaml')



