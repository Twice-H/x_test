from config.Conf import ConfigYaml
from utils.logutil import my_log
import requests
from utils.assertutil import AssertUtil
import json

class Request:
    def __init__(self):
        self.url = ConfigYaml().get_conf_url()
        self.log = my_log("Requests")
        self.Assert = AssertUtil()

    def requests_api(self, data=None, headers=None, method="post"):

        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(self.url, data=data, headers=headers)
            print(r, '\n')

        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(self.url, data=data, headers=headers)
            print(r, '\n')
        else:
            self.log.error("请求错误")
        code = r.status_code
        self.Assert.assert_code(code, 200)
        # r["code"] = code
        return r

    def get(self, data=None, headers=None):
        res = self.requests_api(method="get", data=data, headers=headers).content
        return json.loads(res)

    def post(self, data=None, headers=None):
        res = self.requests_api(method="post", data=data, headers=headers).content
        return json.loads(res)

if __name__ == "__main__":
    res = Request()
    data = {'ac': 'userLogin',
    'username': 'banner',
    'password': 'a123456',
    'edition': 'v1.0.0',
    'vcode': '6666',
    'vid': '9F8DDDF6-5684-43FA-806D-05F1E850CF04',
    'client_type': '0'}
    r = res.post(data=data)
    print(r)