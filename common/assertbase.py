import logging
import re
import json
import jsonpath
from common.logger import Logger
class AssertBase:
    logging=Logger().logger
    def assert_main(self,assert_str,res):
        result= jsonpath.jsonpath(res.json(),'$.['+assert_str+']')
        try:
            assert result != False
            # 断言成功记录日志
            self.logging.info('请求结果断言成功:预期结果包含'+assert_str+',实际结果'+res.text)
            return False
        except Exception:
            # 断言失败记录日志
            self.logging.info('请求结果断言失败:预期结果包含'+assert_str+',实际结果'+res.text)
            raise
    def assert_status(self, code, assert_code):
        """
        请求响应状态码断言
        :data code:
        :data assert_code:
        :return:
        """
        try:
            assert code == assert_code
            self.logging.error("请求状态码对比成功,请求状态码为:{0},断言状态码为:{1}".format(code, assert_code))

            return True
        except Exception:
            self.logging.error("请求状态码对比失败,请求状态码为:{0},断言状态码为:{1}".format(code, assert_code))
            raise

    def assert_body(self, assert_body,body):
        """
        请求响应body断言
        :data body:
        :data assert_body:
        :return:
        """
        try:
            assert body == assert_body
            self.logging.error("响应body对比成功，响应body为:{0},断言body为:{1}".format(body, assert_body))

            return True
        except Exception:
            self.logging.error("响应body对比失败，响应body为:{0},断言body为:{1}".format(body, assert_body))
            raise

    def assert_in_body(self,  assert_text,body):
        """
        响应信息断言
        :data body:
        :data assert_text:
        :return:
        """
        try:
            # 字段转换为字符串，ensure_ascii参数为输出是否为ASCII编码(序列化时中文默认使用ASCII编码)
            text = json.dumps(body, ensure_ascii=False)
            assert assert_text in text
            self.logging.error("断言字符串在响应体中，断言字符串为:{0},响应信息为:{1}".format(assert_text, body))
            return True
        except Exception:
            self.logging.error("断言字符串不在响应体中，断言字符串为:{0},响应信息为:{1}".format(assert_text, body))
            raise

    def assert_time(self,  assert_time,time):
        """
        响应时间断言
        :data time:
        :data assert_time:
        :return:
        """
        try:
            assert time < assert_time
            return True
        except Exception:
            self.log.error("响应时间超时，断言时间:{0},响应时间:{1}".format(assert_time, time))
            raise
