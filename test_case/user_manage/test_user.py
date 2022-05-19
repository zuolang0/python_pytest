import random

import pytest
import requests
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml,render_yaml
from common.function import get_rand_num


class TestYaml():
    token_path="/test_case/user_manage/token.yaml"
    tag_yaml='/test_case/user_manage/tag.yaml'
    def get_token(self):
        res= read_yaml(self.token_path)
        return res['access_token']
    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/get_token.yaml"))
    def test_get_token(self, caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        res = RequestsUtil.send_requests(method,url,data)
        try:
            assert res.json()['expires_in'] == caseinfo['validate']['expires_in']
            write_yaml(res.json(),self.token_path)
        except Exception as e:
            assert res.json()['errcode']>0


    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/create_tag.yaml"))
    def test_add_tag(self, caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        res = RequestsUtil.send_requests(method, url, data)
        if  caseinfo['validate']=='errcode':
            assert caseinfo['validate'] in res.json()
        else:
            assert caseinfo['validate'] in res.json()['tag']

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/get_tag.yaml"))
    def test_get_tag(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        res=RequestsUtil.send_requests(method,url,[])
        assert caseinfo['validate'] in res.json()
        write_yaml(res.json()['tags'],self.tag_yaml)

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/user_manage/del_tag.yaml"))
    def test_del_tag(self,caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]
        data = caseinfo['request']["data"]
        print(caseinfo)

if __name__ == '__main__':
    pytest.main()
