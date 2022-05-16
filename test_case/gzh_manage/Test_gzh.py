import re

import jsonpath as jsonpath
import pytest
import requests
from common.assertbase import AssertBase
from common.yaml_util import read_yaml


class TestApi:
    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/get_token.yaml'))
    def test_01_api(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        res=requests.get(url,data)
        ass=AssertBase()
        ass.assert_main(caseinfo['validate'],res)
        # js_res=jsonpath.jsonpath(res.json(),'$.*')
        # print(js_res)
        # re_result=re.search('"access_token":"(.*?)"',res.text)
        # print(re_result.group(1))


