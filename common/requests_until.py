import requests
from common.logger import Logger
class RequestsUtil:
    session =requests.session()
    logging=Logger()
    @classmethod
    def send_requests(self,method,url,data,**kwargs):
        method=str(method).lower()
        try:
            if method == "get":
                res= RequestsUtil.session.request(method,url,params=data)
            elif method == "post":
                res= RequestsUtil.session.request(method,url,json=data)
            RequestsUtil.session.close()
            return res
        except requests.RequestException as e:
            self.logging.error("请求异常：" + str(e) + "请求失败url" + url)
            raise
