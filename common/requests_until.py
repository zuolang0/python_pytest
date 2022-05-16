import requests
class RequestsUtil:
    session =requests.session()
    @classmethod
    def send_requests(self,method,url,data,**kwargs):
        method=str(method).lower()
        if method == "get":
            res= RequestsUtil.session.request(method,url,params=data)
        elif method == "post":
            res= RequestsUtil.session.request(method,url,json=data)
        return res
