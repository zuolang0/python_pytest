import pytest
import json
from common.assertbase import AssertBase
from common.requests_until import RequestsUtil
from common.yaml_util import read_yaml,write_yaml
from common.logger import Logger
class TestTag:
    assb=AssertBase()
    log=Logger()
    token=""

    def setup_class(self):
        self.token=read_yaml('test_case/token.yaml')
    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/get_tag.yaml'))
    def test_get_tag(self,caseinfo):
        # token=read_yaml('test_case/token.yaml')
        url=caseinfo['request']['url']+self.token['access_token']
        method=caseinfo['request']['method']
        data=caseinfo['request']['data']
        self.log.info("请求地址:"+url)
        self.log.info("请求方法:"+method)
        self.log.info("请求参数:"+str(data))
        self.log.log_request(caseinfo['request'])
        res=RequestsUtil.send_requests(method,url,data)
        self.assb.assert_main(caseinfo['validate']['assert_str'],res)
        if 'tags' in res.json():
            write_yaml(res.json()['tags'],'test_case/gzh_manage/tag.yaml')

    @pytest.mark.parametrize("caseinfo", read_yaml("/test_case/gzh_manage/create_tag.yaml"))
    def test_add_tag(self, caseinfo):
        method = caseinfo['request']["method"]
        url = caseinfo['request']["url"]+self.token['access_token']
        data = caseinfo['request']["data"]
        res = RequestsUtil.send_requests(method, url, data)
        self.log.info("请求地址:"+url)
        self.log.info("请求方法:"+method)
        self.log.info("请求参数:"+str(data))
        self.assb.assert_main(caseinfo['validate']['assert_str'],res)

    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/tag.yaml'))
    def test_del_tag(self,caseinfo):
        # token=read_yaml('test_case/token.yaml')
        base=read_yaml('test_case/gzh_manage/del_tag.yaml')
        url=base['request']['url']+self.token['access_token']
        method=base['request']['method']
        data={'tag':{'id':caseinfo['id']}}
        self.log.info("请求地址:"+url)
        self.log.info("请求方法:"+method)
        self.log.info("请求参数:"+str(data))
        # self.log.log_request(caseinfo['request'])
        # self.logging.info("请求结果:{}".format(res.json()))
        # print(data)


    @pytest.mark.parametrize('caseinfo',read_yaml('test_case/gzh_manage/tag.yaml'))
    def test_get_tag_user(self,caseinfo):
        base=read_yaml('test_case/gzh_manage/get_tag_user.yaml')
        # token=read_yaml('test_case/token.yaml')
        url=base['request']['url']+self.token['access_token']
        method=base['request']['method']
        data={'tagid':caseinfo['id']}
        self.log.info("请求地址:"+url)
        self.log.info("请求方法:"+method)
        self.log.info("请求参数:"+str(data))
        res=RequestsUtil.send_requests(method,url,data)
        # self.log.log_request(caseinfo['request'])
        self.assb.assert_main(base['validate']['assert_str'],res)


