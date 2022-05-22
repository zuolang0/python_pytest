import random

import pytest
import requests
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml,render_yaml
from common.function import get_rand_num
from common.assertbase import AssertBase

class TestYaml():
    token_path="/test_case/token.yaml"
    tag_yaml='/test_case/user_manage/tag.yaml'
    ass=AssertBase()
    def get_token(self):
        res= read_yaml(self.token_path)
        return res['access_token']
    # @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/get_token.yaml"))
    # def test_get_token(self, caseinfo):
    #     method = caseinfo['request']["method"]
    #     url = caseinfo['request']["url"]
    #     data = caseinfo['request']["data"]
    #     res = RequestsUtil.send_requests(method,url,data)
    #     try:
    #         self.ass.assert_main(caseinfo['validate']['assert_str'],res)
    #         write_yaml(res.json(),self.token_path)
    #     except Exception as e:
    #         assert res.json()['errcode']>0


    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/create_tag.yaml"))
    def test_add_tag(self, caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        res = RequestsUtil.send_requests(method, url, data)
        print(res.json())
        self.ass.assert_main(caseinfo['validate']['assert_str'],res)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/get_tag.yaml"))
    def test_get_tag(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        res=RequestsUtil.send_requests(method,url,[])
        try:
            self.ass.assert_main(caseinfo['validate']['assert_str'],res)
            write_yaml(res.json()['tags'],self.tag_yaml)
        except Exception as e:
            raise

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/del_tag.yaml"))
    def test_del_tag(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]

        # print(caseinfo)
#
# if __name__ == '__main__':
#     pytest.main()
