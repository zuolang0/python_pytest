import logging
import re
import jsonpath
from common.logger import Logger
class AssertBase:
    logging=Logger().logger
    def assert_main(self,valation,res):
        result= jsonpath.jsonpath(res.json(),'$.['+valation['assert_str']+']')
        if result == False:
            # 断言失败记录日志
            self.logging.info('断言失败:预期结果包含'+valation['assert_str']+',实际结果'+res.text)
            # print(valation['assert_str'])
            return False
        else:
            # 断言成功记录日志
            self.logging.info('断言成功:预期结果包含'+valation['assert_str']+',实际结果'+res.text)
            # print(valation['assert_str'])
            return True
