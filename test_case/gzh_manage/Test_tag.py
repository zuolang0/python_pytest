import pytest
from common.assertbase import AssertBase
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml,load_yaml
from common.logger import Logger
class TestTag:
    assb=AssertBase()
    log=Logger()
    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/get_tag.yaml'))
    def test_get_tag(self,caseinfo):
        url=caseinfo['request']['url']
        method=caseinfo['request']['method']
        data=caseinfo['request']['data']
        self.log.log_request(caseinfo['request'])
        res=RequestsUtil.send_requests(method,url,data)
        self.assb.assert_main(caseinfo['validate']['assert_str'],res)
        if 'tags' in res.json():
            write_yaml(res.json()['tags'],'test_case/gzh_manage/tag.yaml')


    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/tag.yaml'))
    def test_del_tag(self,caseinfo):
        base=read_yaml('test_case/gzh_manage/del_tag.yaml')
        url=base['request']['url']
        method=base['request']['method']
        data={'tag':{'id':caseinfo['id']}}
        # self.log.log_request(caseinfo['request'])
        # self.logging.info("请求结果:{}".format(res.json()))
        # print(data)


    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/tag.yaml'))
    def test_get_tag_user(self,caseinfo):
        base=read_yaml('test_case/gzh_manage/get_tag_user.yaml')
        url=base['request']['url']
        method=base['request']['method']
        data={'tagid':caseinfo['id']}
        res=RequestsUtil.send_requests(method,url,data)
        self.log.log_request(caseinfo['request'])
        self.assb.assert_main(base['validate']['assert_str'],res)


