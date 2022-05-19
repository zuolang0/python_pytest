import pytest
import requests
from common.assertbase import AssertBase
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml,load_yaml
class TestTag:
    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/get_tag.yaml'))
    def test_get_tag(self,caseinfo):
        url=caseinfo['request']['url']
        method=caseinfo['request']['method']
        data=caseinfo['request']['data']
        res=RequestsUtil.send_requests(method,url,data)
        assb=AssertBase()
        assb.assert_main(caseinfo['validate']['assert_str'],res)
        if 'tags' in res.json():
            write_yaml(res.json()['tags'],'test_case/gzh_manage/tag.yaml')


    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/tag.yaml'))
    def test_del_tag(self,caseinfo):
        base=read_yaml('test_case/gzh_manage/del_tag.yaml')
        url=base['request']['url']
        method=base['request']['method']
        data={'tag':{'id':caseinfo['id']}}
        # print(data)


    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/tag.yaml'))
    def test_get_tag_user(self,caseinfo):
        base=read_yaml('test_case/gzh_manage/get_tag_user.yaml')
        url=base['request']['url']
        method=base['request']['method']
        data={'tagid':caseinfo['id']}
        res=RequestsUtil.send_requests(method,url,data)
        assb=AssertBase()
        assb.assert_main(base['validate']['assert_str'],res)


